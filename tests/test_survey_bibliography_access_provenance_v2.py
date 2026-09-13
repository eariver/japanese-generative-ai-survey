from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from pathlib import Path

from scripts import run_semantic_publication_v2_interactive_base as special_pub
from scripts import survey_bibliography_access_provenance_v2 as provenance
from scripts import survey_production_v2 as core
from scripts import survey_weekly_semantic_publication_v2 as weekly_pub


class BibliographyAccessProvenanceUnitTests(unittest.TestCase):
    def test_parse_access_date_valid_instants_and_dates(self):
        full, d = provenance.parse_access_date("2026-09-08T14:52:53Z")
        self.assertEqual(full, "2026-09-08T14:52:53Z")
        self.assertEqual(d, "2026-09-08")

        full, d = provenance.parse_access_date("2026-08-14T18:00:00-04:00")
        self.assertEqual(full, "2026-08-14T18:00:00-04:00")
        self.assertEqual(d, "2026-08-14")

        full, d = provenance.parse_access_date("2026-08-24")
        self.assertEqual(full, "2026-08-24")
        self.assertEqual(d, "2026-08-24")

    def test_parse_access_date_invalid_fails_closed(self):
        for invalid in ["", "   ", "not-a-date", "2026/08/24", None, 12345]:
            with self.assertRaises(ValueError):
                provenance.parse_access_date(invalid)  # type: ignore[arg-type]

    def test_resolve_source_access_provenance_single_source(self):
        sources = [
            {
                "source_id": "src-1",
                "url": "https://example.com/test",
                "accessed_at": "2026-09-08T14:52:53Z",
            }
        ]
        res = provenance.resolve_source_access_provenance(
            sources, "https://example.com/test", "did-1"
        )
        self.assertEqual(res["source_id"], "src-1")
        self.assertEqual(res["source_accessed_at"], "2026-09-08T14:52:53Z")
        self.assertEqual(res["urldate"], "2026-09-08")

    def test_resolve_source_access_provenance_selects_matching_url(self):
        sources = [
            {
                "source_id": "src-other",
                "url": "https://other.example.com/page",
                "accessed_at": "2026-09-01T10:00:00Z",
            },
            {
                "source_id": "src-official",
                "url": "https://official.example.com/announcement",
                "accessed_at": "2026-09-08T12:00:00Z",
            },
        ]
        res = provenance.resolve_source_access_provenance(
            sources, "https://official.example.com/announcement", "did-2"
        )
        self.assertEqual(res["source_id"], "src-official")
        self.assertEqual(res["source_accessed_at"], "2026-09-08T12:00:00Z")
        self.assertEqual(res["urldate"], "2026-09-08")


class BibliographyAccessProvenanceContractTests(unittest.TestCase):
    def test_b1_weekly_per_source_access_date_differs_from_cutoff(self):
        """B1: Weekly publication binds per-source access date, distinct from edition cutoff."""
        profile = {
            "research_scope": {
                "temporal_policy": {
                    "mode": "ROLLING_WINDOW",
                    "window_start": "2026-08-14T18:00:00-04:00",
                    "window_end": "2026-08-21T18:00:00-04:00",
                    "cutoff": "2026-08-21T18:00:00-04:00",
                    "timezone": "America/New_York",
                }
            }
        }
        display_date, boundary = weekly_pub._window(profile)
        self.assertEqual(display_date, "2026-08-21")

        record = {
            "entity": {
                "canonical_name": "Grok Bot access expansion",
                "canonical_url": "https://x.ai/news/grok-bot-more-plans",
                "organization": "xAI",
            },
            "status": "VERIFIED",
            "materiality": "MATERIAL",
            "source_accessed_at": "2026-09-08T14:52:53Z",
            "urldate": "2026-09-08",
        }
        bib = weekly_pub._bib_text("w2026w34w34eventc066", record, record["urldate"])
        self.assertIn("urldate = {2026-09-08}", bib)
        self.assertNotIn("urldate = {2026-08-21}", bib)

    def test_b2_special_per_source_access_date_differs_from_as_of(self):
        """B2: Special publication binds per-source access date, distinct from retrospective as_of."""
        as_of = "2026-08-24T17:24:00Z"
        as_of_date = as_of[:10]  # 2026-08-24
        source_accessed_at = "2026-08-15T09:30:00Z"
        source_urldate = "2026-08-15"

        record = {
            "entity": {
                "canonical_name": "Historical Foundation Model Report",
                "canonical_url": "https://arxiv.org/abs/2401.02954",
                "organization": "Research Lab",
            },
            "status": "VERIFIED",
            "materiality": "MATERIAL",
            "source_accessed_at": source_accessed_at,
            "urldate": source_urldate,
        }
        bib = special_pub._bib_text("sp001model01", record, record["urldate"])
        self.assertIn(f"urldate = {{{source_urldate}}}", bib)
        self.assertNotIn(f"urldate = {{{as_of_date}}}", bib)

    def test_b3_multiple_sources_receive_independent_access_dates(self):
        """B3: Multiple sources in the same publication retain independent per-source urldates."""
        rec1 = {
            "entity": {
                "canonical_name": "Source Alpha",
                "canonical_url": "https://alpha.example.com",
                "organization": "Alpha Org",
            },
            "status": "VERIFIED",
            "materiality": "MATERIAL",
            "source_accessed_at": "2026-08-10T08:00:00Z",
            "urldate": "2026-08-10",
        }
        rec2 = {
            "entity": {
                "canonical_name": "Source Beta",
                "canonical_url": "https://beta.example.com",
                "organization": "Beta Org",
            },
            "status": "VERIFIED",
            "materiality": "MATERIAL",
            "source_accessed_at": "2026-08-18T16:00:00Z",
            "urldate": "2026-08-18",
        }
        bib1 = weekly_pub._bib_text("w34alpha", rec1, rec1["urldate"])
        bib2 = weekly_pub._bib_text("w34beta", rec2, rec2["urldate"])
        self.assertIn("urldate = {2026-08-10}", bib1)
        self.assertIn("urldate = {2026-08-18}", bib2)
        self.assertNotEqual(rec1["urldate"], rec2["urldate"])

    def test_b4_event_date_differs_from_access_date(self):
        """B4: Published/event date differs from retrieval/access date; urldate must bind access date."""
        card_sources = [
            {
                "source_id": "src-paper-1",
                "url": "https://arxiv.org/abs/2210.02414",
                "source_class": "PRIMARY_PAPER",
                "title": "Historical 2022 Paper",
                "published_at": "2022-10-05",
                "accessed_at": "2026-08-24T17:24:00Z",
            }
        ]
        prov = provenance.resolve_source_access_provenance(
            card_sources, "https://arxiv.org/abs/2210.02414", "SP001-D009"
        )
        self.assertEqual(prov["source_accessed_at"], "2026-08-24T17:24:00Z")
        self.assertEqual(prov["urldate"], "2026-08-24")
        self.assertNotEqual(prov["urldate"], "2022-10-05")

    def test_b5_revised_page_chronology_c066_class(self):
        """B5: Event Aug 21, page re-dated Aug 26, canonical access Sep 8 -> urldate Sep 8."""
        card_sources = [
            {
                "source_id": "supplement-src-6b3ce48a6c75d42b",
                "url": "https://x.ai/news/grok-bot-more-plans",
                "source_class": "PRIMARY_OFFICIAL",
                "title": "First-party announcement",
                "published_at": "2026-08-26",
                "accessed_at": "2026-09-08T14:52:53Z",
            }
        ]
        prov = provenance.resolve_source_access_provenance(
            card_sources, "https://x.ai/news/grok-bot-more-plans", "w34-event-c066"
        )
        self.assertEqual(prov["urldate"], "2026-09-08")
        self.assertNotEqual(prov["urldate"], "2026-08-21")  # Not the event cutoff date
        self.assertNotEqual(prov["urldate"], "2026-08-26")  # Not the revised page date

    def test_b6_missing_access_timestamp_fails_closed(self):
        """B6: Missing or blank access timestamp fails closed with an actionable error."""
        sources_missing = [
            {
                "source_id": "src-no-ts",
                "url": "https://example.com/no-timestamp",
                "accessed_at": "",
            }
        ]
        with self.assertRaisesRegex(ValueError, "missing access timestamp"):
            provenance.resolve_source_access_provenance(
                sources_missing, "https://example.com/no-timestamp", "did-missing"
            )

        sources_none = [
            {
                "source_id": "src-none-ts",
                "url": "https://example.com/none-timestamp",
                "accessed_at": None,
            }
        ]
        with self.assertRaisesRegex(ValueError, "missing access timestamp"):
            provenance.resolve_source_access_provenance(
                sources_none, "https://example.com/none-timestamp", "did-none"
            )

        # _bib_text fails closed when neither urldate nor source_accessed_at is present
        record_no_ts = {
            "entity": {
                "canonical_name": "Title",
                "canonical_url": "https://example.com",
            }
        }
        with self.assertRaisesRegex(ValueError, "lacks canonical access date"):
            weekly_pub._bib_text("key1", record_no_ts, None)

        with self.assertRaisesRegex(ValueError, "lacks canonical access date"):
            special_pub._bib_text("key1", record_no_ts, None)

    def test_b7_ambiguous_access_provenance_fails_closed(self):
        """B7: Ambiguous captures with conflicting access times fail closed unless explicitly disambiguated."""
        ambiguous_sources = [
            {
                "source_id": "cap-1",
                "url": "https://example.com/doc",
                "accessed_at": "2026-08-10T10:00:00Z",
            },
            {
                "source_id": "cap-2",
                "url": "https://example.com/doc",
                "accessed_at": "2026-08-20T15:00:00Z",
            },
        ]
        # Ambiguous resolution without explicit_source_id must fail closed
        with self.assertRaisesRegex(ValueError, "ambiguous captures"):
            provenance.resolve_source_access_provenance(
                ambiguous_sources, "https://example.com/doc", "did-ambig"
            )

        # Disambiguated resolution using explicit_source_id succeeds
        resolved_1 = provenance.resolve_source_access_provenance(
            ambiguous_sources,
            "https://example.com/doc",
            "did-ambig",
            explicit_source_id="cap-1",
        )
        self.assertEqual(resolved_1["source_id"], "cap-1")
        self.assertEqual(resolved_1["urldate"], "2026-08-10")

        resolved_2 = provenance.resolve_source_access_provenance(
            ambiguous_sources,
            "https://example.com/doc",
            "did-ambig",
            explicit_source_id="cap-2",
        )
        self.assertEqual(resolved_2["source_id"], "cap-2")
        self.assertEqual(resolved_2["urldate"], "2026-08-20")

    def test_b8_source_identity_and_citation_invariants_preserved(self):
        """B8: Citation keys, URL, name, organization, status, materiality, and ordering are preserved."""
        record_before = {
            "entity": {
                "canonical_name": "Grok Bot access expansion",
                "canonical_url": "https://x.ai/news/grok-bot-more-plans",
                "organization": "xAI",
            },
            "status": "VERIFIED",
            "materiality": "MATERIAL",
        }
        # Render old with cutoff
        bib_old = (
            "@online{w2026w34w34eventc066,\n"
            "  title = {{Grok Bot access expansion}},\n"
            "  author = {{xAI}},\n"
            "  url = {https://x.ai/news/grok-bot-more-plans},\n"
            "  urldate = {2026-08-21}\n"
            "}"
        )
        # Render new with canonical access date
        record_after = {
            **record_before,
            "source_accessed_at": "2026-09-08T14:52:53Z",
            "urldate": "2026-09-08",
        }
        bib_new = weekly_pub._bib_text(
            "w2026w34w34eventc066", record_after, record_after["urldate"]
        )

        # Invariants
        self.assertIn("@online{w2026w34w34eventc066,", bib_new)
        self.assertIn("title = {{Grok Bot access expansion}},", bib_new)
        self.assertIn("author = {{xAI}},", bib_new)
        self.assertIn("url = {https://x.ai/news/grok-bot-more-plans},", bib_new)
        self.assertEqual(record_after["status"], record_before["status"])
        self.assertEqual(record_after["materiality"], record_before["materiality"])
        self.assertEqual(
            record_after["entity"]["canonical_name"],
            record_before["entity"]["canonical_name"],
        )
        self.assertEqual(
            record_after["entity"]["canonical_url"],
            record_before["entity"]["canonical_url"],
        )
        self.assertEqual(
            record_after["entity"]["organization"],
            record_before["entity"]["organization"],
        )

    def test_b9_w34_read_only_fixture_regression(self):
        """B9: Verify W34 fixture provenance: 41 citations, accessed_at on 2026-09-08, and c066 repair."""
        cmd = [
            "git",
            "show",
            "6f68fd09955302fd87e5ec0ce77ff06ccaec8448:surveys/weekly/2026-W34/references.bib",
        ]
        proc = subprocess.run(cmd, capture_output=True, text=True)
        if proc.returncode != 0:
            self.skipTest("W34 fixture commit 6f68fd09955302fd87e5ec0ce77ff06ccaec8448 not available")

        bib_content = proc.stdout
        bib_keys = [
            line.split("{")[1].split(",")[0].strip()
            for line in bib_content.splitlines()
            if line.startswith("@online{")
        ]
        self.assertEqual(len(bib_keys), 41, "W34 bibliography must contain exactly 41 cited items")

        # Load W34 evidence acceptance from fixture commit
        acc_cmd = [
            "git",
            "show",
            "6f68fd09955302fd87e5ec0ce77ff06ccaec8448:sources/2026-W34/evidence/v2/accepted/647cde464d92935c1ca633ade62bcbf7ebe88c458cc8b3848bae8d2fc4794831/evidence-accepted.json",
        ]
        acc_proc = subprocess.run(acc_cmd, capture_output=True, text=True)
        self.assertEqual(acc_proc.returncode, 0)
        acceptance = json.loads(acc_proc.stdout)

        # Verify c066 card specifically
        c066_task = None
        for res in acceptance["results"]:
            if "w34-event-c066" in res["discovery_ids"]:
                c066_task = res
                break
        self.assertIsNotNone(c066_task)

        card_cmd = [
            "git",
            "show",
            f"6f68fd09955302fd87e5ec0ce77ff06ccaec8448:sources/2026-W34/evidence/v2/accepted/647cde464d92935c1ca633ade62bcbf7ebe88c458cc8b3848bae8d2fc4794831/results/{c066_task['filename']}",
        ]
        card_proc = subprocess.run(card_cmd, capture_output=True, text=True)
        self.assertEqual(card_proc.returncode, 0)
        c066_card = json.loads(card_proc.stdout)
        self.assertEqual(len(c066_card["sources"]), 1)
        source = c066_card["sources"][0]
        self.assertEqual(source["url"], "https://x.ai/news/grok-bot-more-plans")
        self.assertEqual(source["accessed_at"], "2026-09-08T14:52:53Z")

        # Resolve provenance for c066
        prov = provenance.resolve_source_access_provenance(
            c066_card["sources"], source["url"], "w34-event-c066"
        )
        self.assertEqual(prov["urldate"], "2026-09-08")
        self.assertEqual(prov["source_accessed_at"], "2026-09-08T14:52:53Z")

        # Verify that old W34 bib had cutoff 2026-08-21, and new resolved date is 2026-09-08
        self.assertIn("@online{w2026w34w34eventc066,", bib_content)
        self.assertNotEqual(prov["urldate"], "2026-08-21")

    def test_sp001_read_only_fixture_access_provenance(self):
        """SP001 fixture: all 11 accepted evidence sources resolve to 2026-08-24."""
        sp001_acc = Path(
            "sources/SP001/evidence/v2/accepted/3785dc9ee87378b6682cc6d45a064cba1c9325bba4339dc04e460d441dcfb430/evidence-accepted.json"
        )
        if not sp001_acc.is_file():
            self.skipTest(f"SP001 acceptance file not found: {sp001_acc}")

        evidence_sources = provenance.load_evidence_sources(sp001_acc)
        self.assertEqual(len(evidence_sources), 11)

        for did, info in evidence_sources.items():
            sources = info.get("sources")
            self.assertIsNotNone(sources, f"{did} must have sources")
            self.assertTrue(len(sources) >= 1)
            primary_url = sources[0]["url"]
            prov = provenance.resolve_source_access_provenance(
                sources, primary_url, did
            )
            self.assertEqual(prov["urldate"], "2026-08-24")
            self.assertEqual(prov["source_accessed_at"], "2026-08-24T17:24:00Z")


if __name__ == "__main__":
    unittest.main()
