# City Sticker Skill Brief v0.1

## Contents

- Qualification and core contract
- Inputs, outputs, success, and scope
- Reference-project adaptation
- Representative requests and trigger examples
- Open decisions

## Qualification

- Decision: **A — Create one Skill**.
- Evidence: landmark-sticker production is recurring, has stable inputs and outputs, needs fixed style/reference rules, and benefits from deterministic asset checks.
- Existing Skill overlap: the reviewed `ip-illustration-character-system` solves personal-character identity across many asset families. It does not research landmark truth or create non-personified city markers.
- Recommendation: keep `city-sticker` separate. Reuse its reference-role, anchor, manifest, and targeted-repair patterns without copying its character routes.

## Core contract

When a user names a city landmark, this Skill helps the travel-product owner turn verified landmark features into a reviewable sticker candidate that follows a user-approved style anchor.

## Target users

- Primary: product owner or art director building the travel mini-program sticker library.
- Secondary: designer or Agent preparing consistent landmark assets after style approval.

## Inputs

### Required

- City.
- Exact landmark name.
- Permission to search the web or supplied factual landmark images.
- Approved `STYLE_REFERENCE`, or explicit permission to make a `STYLE TEST`.

### Optional

- Preferred viewpoint.
- Candidate count.
- White-border and shadow decision.
- Existing style version and output root.
- Additional source images or feature notes.

## Outputs

- `research.md`: sources and evidence.
- `landmark-lock.json`: three to five recognition features.
- `style-lock.json`: versioned visual rules and ordered references.
- `manifest.json` and `prompt.txt`.
- Candidate PNG files only when explicitly requested.
- 128/96/64 px thumbnail review and `qa.md`.
- Partial result: when generation is blocked, return the complete research and prompt package without claiming an image.

## Success and failure

- Complete when: the landmark is evidence-backed, style/content roles are isolated, all checks are recorded, and status is honest.
- Good result means: the landmark reads at marker size, the set stays visually consistent, and the output contains no text or personification.
- Fail when: core geometry is guessed, the style drifts, the subject becomes a generic building, alpha is false, or an undecided style choice is silently made.
- User-visible evidence: sources, locks, prompts, thumbnails, QA, and file paths.

## Scope

### IN SCOPE

- One or a few landmark sticker studies.
- Buildings, landmarks, and natural scenery.
- Web research and feature extraction.
- Style transfer from non-landmark reference art at the level of visual language.
- Candidate generation, deterministic inspection, and human-review packaging.

### OUT OF SCOPE

- Character/IP systems.
- Generic travel poster or illustration-page design.
- Production deployment or mini-program manifest edits in v0.1.
- Nationwide batch generation before approval.
- Automatic selection or evolution of final style.

## Reference-project adaptation

### Borrowed

- Separate reference roles and explicit precedence.
- Use one accepted anchor as the stable source of truth.
- Freeze a compact lock and repeat it verbatim.
- Plan a manifest before generation.
- Use the smallest useful reference set.
- Validate in a fixed order and repair only the failing item/dimension.
- Use deterministic scripts only for mechanical checks.

### Removed

- Hair, face, eyes, body proportions, outfits, accessories, gestures, expressions, and character identity.
- Q-version anatomy and all personification defaults.
- Multi-route outputs such as avatars, reaction packs, stationery, and photo fusion.
- Character-first composition percentages.
- Any rule that copies a person or palette from packaged style examples.

### Converted

- `character anchor` → `landmark fidelity lock` plus `style lock`.
- `identity reference` → verified landmark photography and official visual evidence.
- `character consistency` → silhouette, roof/tower rhythm, signature color/material, viewpoint, and marker-size consistency.
- `style reference geometry only` → visual-language-only extraction from人物参考图.
- `thumbnail reaction readability` → 128/96/64 px landmark recognizability.

## Representative requests

1. “用 city-sticker 研究南京鸡鸣寺，先出一个 STYLE TEST Prompt，不生成图片。”
2. “我上传了两张人物画风参考，请只提炼线条和色块，为南京博物院做一张实验贴纸。”
3. “沿用已经确认的 style-v1，为西安钟楼和大雁塔各做一个候选，保持同一画风。”

## Trigger examples

### Positive

1. 为鸡鸣寺做一张景点贴纸草案。
2. 用我的 STYLE_REFERENCE 生成南京博物院地图 Marker。
3. 先查真实图片，再提炼东方明珠的识别特征。
4. 审核这张城市地标贴纸是否跑偏。
5. 把人物参考图的钢笔线条迁移到建筑贴纸。
6. 给西安钟楼做一个 STYLE TEST。
7. 检查这批景点 PNG 的透明背景和缩小识别度。
8. 把已确认的景点贴纸画风固化成下一座城市可复用的 Prompt。

### Non-trigger

1. 画一个我的 Q 版人物头像。
2. 给旅行小程序接入地图 Marker 代码。
3. 设计一张城市旅游海报。
4. 把全国景点数据导入数据库。
5. 只帮我润色一段图片 Prompt。

## Open decisions for the next review

- Final approved `STYLE_REFERENCE` images and version name.
- Pen-line thickness and amount of line break.
- Allowed fill misregistration strength.
- Default subject footprint and exact safe margin.
- White-border treatment: none, thin, or sticker-cut border.
- Shadow treatment: none or restrained soft shadow.
- Default viewpoint for buildings and natural landscapes.
- Marker review sizes used by the actual mini-program.
