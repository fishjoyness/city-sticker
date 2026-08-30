# Landmark Research Workflow

## Contents

- Goal and source priority
- Complementary views and evidence table
- Recognition-feature extraction
- Landmark fidelity lock
- Simplification, failure handling, and copyright boundary

## Goal

Confirm what makes the real place recognizable before drawing it. Research is evidence gathering, not a hunt for one photo to copy.

## Source priority

Use the highest available sources in this order:

1. landmark, scenic-area, museum, monument, or heritage-site official website
2. local culture-and-tourism authority or government page
3. official museum, archive, university, or heritage institution
4. official media or established news photography
5. reliable map POI or established travel reference for missing viewpoints

Search with the exact landmark name plus city, province, and view terms such as `正面`, `全景`, `航拍`, `入口`, `屋顶`, or `夜景` only when relevant.

Do not rely on AI summaries, generated images, unsourced reposts, fan art, or one low-resolution thumbnail as factual evidence.

## Collect two to four complementary views

Aim to cover:

- one overall silhouette or primary facade
- one angle that confirms the unique roof, tower, arch, dome, bridge, mountain, or shoreline
- one context view when the landmark depends on terrain, water, gate, plaza, or adjacent structure
- one detail view only when a small feature is genuinely recognition-critical

Record without downloading copyrighted files unless the use and license permit it. A source URL and observation are usually sufficient for research.

## Evidence table

Create `research.md`:

```markdown
# <城市> · <景点> 视觉研究

| Source | Publisher | Accessed | View | Evidence used |
|---|---|---|---|---|
| <direct URL> | <official body> | YYYY-MM-DD | front/oblique/context/detail | <what this proves> |

## Conflicts or uncertainty

- NONE, or a precise conflict that blocks generation.
```

Prefer direct pages that contain the image and context. Do not record search-result pages as final evidence.

## Extract three to five recognition features

Choose only features that survive simplification and marker reduction:

1. **Primary silhouette:** the largest recognizable mass or skyline.
2. **Signature structure:** roof stack, tower, dome, arch, gate, bridge span, mountain crest, shoreline, or similar unique geometry.
3. **Rhythm:** columns, windows, eaves, terraces, arches, spires, or repeated masses when they distinguish the place.
4. **Characteristic color/material:** only when consistent across reliable views and important to recognition.
5. **Essential context:** hill, lake, river, wall, plaza, or foreground object that people use to recognize the place.

Exclude tiny ornament, incidental people, temporary banners, weather, vehicles, scaffolding, decorative landscaping, and neighboring buildings that do not identify the landmark.

## Build the landmark fidelity lock

Create `landmark-lock.json`:

```json
{
  "city": "nanjing",
  "landmark": "鸡鸣寺",
  "placeSlug": "jiming-temple",
  "preferredView": "pending-research",
  "features": [
    {
      "priority": 1,
      "feature": "primary silhouette",
      "visualInstruction": "concise observable geometry",
      "evidence": ["source-01", "source-02"]
    }
  ],
  "mustNotInvent": [],
  "uncertainty": []
}
```

Each feature needs evidence. Do not use a feature because it “feels right.”

## Convert evidence into simplified art

- Preserve the primary silhouette first.
- Preserve the signature structure second.
- Compress repeated details into a readable rhythm rather than drawing every unit.
- Keep characteristic color blocks simple and factual.
- Include only essential context.
- Remove detail until the 64 px silhouette remains clear; never remove the feature that differentiates the landmark from a generic building or landscape.

## Failure handling

- Same-name ambiguity: ask for the exact city/site.
- Renovation or multiple historical appearances: show the alternatives and ask which era/view to use.
- Conflicting colors or structure: prefer official/current evidence and disclose the conflict.
- No authoritative overview: supplement with multiple reliable sources and label confidence.
- Identity-critical feature cannot be confirmed: stop before generation and state the missing evidence.

## Copyright boundary

Use photographs to identify factual appearance and structural features. Do not recreate one photographer's exact framing, lighting, weather, crowd arrangement, or distinctive artistic treatment. Combine factual observations into a simplified landmark study governed by the approved style anchor.
