# SP001 shared-Core defect — Draft self-contained validation across historical JSON serialization

Date: 2026-08-26 JST  
Edition: `SP001`  
Classification: `SHARED_CORE_DEFECT`  
Production status: `PAUSED_AFTER_CORE_SYNC_BEFORE_DRAFT_ARTIFACT_ADOPTION`

## Symptom

After Human-approved PR #465 was merged to reviewed `main` and synchronized into `special/SP001-v2-work`, the repaired Draft builder can derive the intended final cross-package synthesis inputs. Before adopting any Draft artifact, however, a second generic incompatibility was found in the self-contained Draft Package validator.

Historical accepted Evidence/Card/Matrix bytes in SP001 were produced by an earlier reviewed Core serializer as compact JSON. The current `core.write_json/json_bytes` serializer emits indented JSON. `survey_drafting_v2_base._object_sha()` reserializes the already-parsed embedded object using the *current* serializer and compares that SHA-256 to the historical accepted file SHA-256.

Therefore semantically identical Evidence objects fail solely because whitespace/serialization changed across reviewed Core versions. Example from the accepted Baichuan 2 Evidence Card:

- accepted raw byte count: `3012`
- accepted raw SHA-256: `1a68dc1c6dde9c60107180f808e8052414bf252aa85496b58d08ba20b491e48b`
- reserialized current pretty-JSON byte count: `3882`
- reserialized SHA-256: `eaae62dbe601caa943cd2a21332c9425a4a425c025c8838bb4f79b49925f8d23`

The same defect class applies to historical Candidate Matrix / Evidence Acceptance objects when their raw serialization predates the current serializer.

## Why this is a shared-Core defect

The accepted upstream artifacts remain exact, hash-verifiable, and semantically valid. Production State intentionally allows a later reviewed generic Core repair to resume an initialized edition without rewriting historical accepted authority. A self-contained Draft validator must therefore not infer historical raw bytes by reserializing parsed objects with the current serializer.

This is Profile-neutral and not SP001-specific.

## Required generic repair

Preserve exact historical raw authority while validating Draft Package semantics:

1. verify the current canonical Candidate Matrix and content-addressed Evidence Acceptance / Evidence Card files by their recorded raw SHA-256 bytes;
2. load those exact authoritative files and compare their parsed objects to the objects embedded in the Draft Package;
3. use the verified historical raw SHA values when the existing semantic validator checks Matrix / Acceptance / Card provenance;
4. reject any raw-byte drift or embedded-object drift;
5. do not rewrite or normalize previously accepted Evidence, Matrix, Selection, Architecture, or Human approval bytes.

The repair must cover both ordinary evidence-owning Draft packages and the final cross-package synthesis package introduced by PR #465.

## Production evidence and boundary

- Reviewed Core PR #465 merge: `d6bf08ab1a0276c979ef02ed05ea569ebb6a57ee`
- SP001 Core-sync merge: `3e3b5a30368ba9f847dc091b2a9d62dd30036bca`
- Lifecycle remains: `ARCHITECTURE_ESTABLISHED`
- Architecture Review remains: `approved` (r2)
- Next canonical action remains: `stage:drafting-synthesis`
- No Draft Package/Result/Synthesis artifact from this attempted resume is adopted as stage authority.

After a separately reviewed generic repair is merged and synchronized, rerun Draft Package/Result/Synthesis materialization cleanly from the unchanged approved Architecture.
