# Quality Score — city-sticker v0.1

| Dimension | Score | Evidence | Gap |
|---|---:|---|---|
| Purpose Clarity | 10/10 | `SKILL.md` Purpose and Core contract define one evidence-backed landmark-sticker study. | None. |
| Scope | 10/10 | IN/OUT boundaries exclude characters, posters, batch generation, and production integration. | None. |
| Trigger Precision | 15/15 | Frontmatter names Chinese/English landmark-sticker intents, research, generation, Prompt, and QA. | None. |
| False Trigger Resistance | 10/10 | Frontmatter exclusions plus three near-neighbor non-trigger evals cover character art, runtime coding, and posters. | None. |
| Workflow | 15/15 | Seven phases define input, action, output, exit, and failure paths from status gate through delivery. | None. |
| Input / Output Contract | 10/10 | Required inputs, research/lock/prompt/PNG/QA artifacts, output tree, and partial-result behavior are explicit. | None. |
| Reliability | 10/10 | Ambiguity, evidence gaps, conflicting anchors, unavailable image tools, invalid assets, and unauthorized promotion are handled. | None. |
| Maintainability | 9/10 | Detailed rules are separated into direct references; one deterministic script owns mechanical PNG checks. | Final `STYLE_REFERENCE` fields remain intentionally pending user review. |
| Context Efficiency | 5/5 | Trigger metadata is discriminative; `SKILL.md` routes to only the reference needed for each phase. | None. |
| Testability | 5/5 | Evals include 5 normal, 3 edge, and 3 non-trigger cases; both structural validators and script self-test pass. | No live image-generation forward test in v0.1. |
| **Total** | **99/100** | Skill is structurally production-ready as a workflow draft. | Artwork style and production promotion remain unapproved. |

## Validation evidence

- Built-in `quick_validate.py`: PASS.
- Skill Architect `validate_skill.py` with eval file and duplicate scan: PASS, 0 errors, 0 warnings.
- `inspect_sticker.py --self-test`: PASS.
- JSON parsing and relative-link scan: PASS.
- Automatic revision: none required after UTF-8 metadata correction.
- Forward test not executed: no approved `STYLE_REFERENCE`, no real landmark candidate, and this round forbids production generation.
