import unittest

from scripts.postprocess_special_reader_facing_notes_v2 import (
    reader_taxonomy_findings,
    translate_machine_labels,
)


class SpecialReaderBenchmarkTypeTests(unittest.TestCase):
    def test_benchmark_type_is_reader_facing(self):
        source = "種別 & BENCHMARK \\\\\n"
        result = translate_machine_labels(source)
        self.assertIn("評価ベンチマーク", result)
        self.assertNotIn("BENCHMARK", result)
        self.assertEqual(reader_taxonomy_findings(result), [])


if __name__ == "__main__":
    unittest.main()
