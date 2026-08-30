# Landmark Sticker Quality Checklist

Review in this order. A failure in a critical item blocks acceptance.

## Contents

- Output integrity
- Landmark and style fidelity
- Composition and marker-size readability
- Set consistency, provenance, and QA record

## 1. Output integrity — critical

- [ ] Exact 1024×1024 PNG master.
- [ ] Genuine alpha exists outside the artwork; no white square or checkerboard drawing.
- [ ] Full subject is visible; no roof, tower, arch, mountain, tree line, or border is cropped.
- [ ] Safe margin and subject footprint match the frozen style lock.
- [ ] Exact Chinese landmark name appears once in the bottom nameplate; every character is correct and readable.
- [ ] No extra caption, pinyin, English, logo, watermark, UI, photo background, or extra landmark.

Run:

```text
python scripts/inspect_sticker.py --input candidate.png --thumbnail candidate__marker-128.png --report candidate__inspect.json
```

The script checks file geometry, alpha, visible bounds, margin, footprint, and produces the 128 px review image. It cannot judge landmark identity or style.

## 2. Landmark fidelity — critical

- [ ] The primary silhouette matches reliable reference views.
- [ ] All three to five locked recognition features are present and readable.
- [ ] Unique roof, tower, dome, arch, bridge, mountain, shoreline, or facade rhythm is not replaced by a generic equivalent.
- [ ] Characteristic colors/material relationships are plausible and evidence-backed.
- [ ] Essential context is present when it carries identity; incidental context is absent.
- [ ] No invented roof, spire, sign, color, neighboring building, or natural feature.

Fail when the image is “a cute temple/tower/building” but not the named place.

Record `LANDMARK_VISUAL_IDENTITY = PASS | FAIL`. The label cannot rescue a generic or incorrect landmark drawing.

## 3. Style fidelity — critical

- [ ] The exact approved `styleVersion` and ordered references were used.
- [ ] Pen weight, wobble, pauses, and gaps match the style lock.
- [ ] Lines feel hand-drawn without becoming fuzzy, sketchy, or uniformly dashed.
- [ ] Color count, saturation, and fill registration match the lock.
- [ ] Shapes are slightly awkward and handmade, not vector-perfect or commercially polished.
- [ ] Rendering is flat and simple: no complex gradient, photographic lighting, glossy 3D, painterly texture, or muddy vintage filter.
- [ ] White border and shadow follow the explicit approved choice.
- [ ] No human anatomy or personification leaked from人物参考图.

## 4. Composition and breathing room — critical

- [ ] Subject footprint matches the approved range.
- [ ] Negative space reads as intentional breathing room, not accidental empty imbalance.
- [ ] Visual mass is centered while landmark-specific asymmetry remains intact.
- [ ] The silhouette is clear before inspecting interior detail.
- [ ] Decorative filler does not compete with the landmark.

## 5. Marker-size readability — critical

Inspect at 128, 96, and 64 px on both light and map-like mixed backgrounds:

- [ ] The landmark remains distinguishable from a generic object.
- [ ] At least the primary silhouette and signature structure survive at 64 px.
- [ ] Thin line gaps do not erase the silhouette.
- [ ] Interior details do not merge into noise.
- [ ] Main color masses remain separated.
- [ ] Border/shadow, if approved, does not swallow linework or create a heavy blob.
- [ ] Bottom nameplate remains recognizable as a label and its Chinese name remains readable at the approved marker size.

Record `LANDMARK_NAME_LABEL = PASS | FAIL`. Any wrong, missing, malformed, duplicated, or dominant name is a blocking failure.

If the 64 px test fails, simplify competing detail before enlarging the subject or thickening every line.

## 6. Set consistency

When comparing two or more candidates:

- [ ] Same canvas, footprint, safe margin, border, shadow, and viewpoint tendency.
- [ ] Same line-weight family and amount of wobble/open gaps.
- [ ] Same palette logic and saturation range, without forcing identical colors.
- [ ] Similar simplification depth and detail density.
- [ ] No candidate appears glossier, more 3D, more polished, more childish, or more crowded than the set.
- [ ] Only landmark-specific content changes.

## 7. Status and provenance — critical

- [ ] Candidate is labeled `STYLE TEST` until explicit user approval.
- [ ] Research sources, access date, feature lock, style version, prompt, and candidate ID are recorded.
- [ ] Copyrighted reference photographs are not redistributed as project assets without permission.
- [ ] Production manifest was not changed in v0.1.

## QA record

Create `qa.md`:

```markdown
# QA — <candidate id>

- Status: STYLE TEST
- Geometry/alpha: PASS | FAIL — evidence
- Landmark fidelity: PASS | FAIL — evidence per feature
- Style fidelity: PASS | FAIL — evidence
- Composition: PASS | FAIL — evidence
- 128 px: PASS | FAIL — evidence
- 96 px: PASS | FAIL — evidence
- 64 px: PASS | FAIL — evidence
- Set consistency: PASS | FAIL | NOT APPLICABLE
- Blocking issue: NONE | exact issue
- Next action: ACCEPT FOR REVIEW | TARGETED REPAIR | NEED BETTER REFERENCE
```

Do not convert an overall impression into a pass. Cite the exact lock or image evidence for each decision.
