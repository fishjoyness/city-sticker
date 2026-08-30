# Visual Language v0.1

This is a provisional review draft, not a final house style. The user-approved `STYLE_REFERENCE` always decides the frozen production style.

## Contents

- Reference roles
- Provisional visual direction
- `STYLE_REFERENCE` card
- 人物参考图迁移规则
- Batch consistency lock

## Reference roles

### LANDMARK_REFERENCE

Controls only factual subject identity:

- outer silhouette and massing
- roof, tower, arch, dome, bridge, mountain, shoreline, or other signature structure
- landmark-specific spacing and repeated architectural rhythm
- characteristic material or color when consistently visible
- relationship to essential context such as a hill, lake, gate, or plaza

It does not control drawing medium, polish, color rendering, border, shadow, or canvas composition.

### STYLE_REFERENCE

Controls only visual language:

- pen texture, weight, pressure variation, wobble, and line breaks
- flat-fill behavior and possible slight registration offset
- color count, saturation, contrast, and shadow logic
- amount of negative space and subject footprint
- simplified geometry and detail density
- viewpoint tendency, white border, and shadow treatment when explicitly approved

If a style reference contains people, ignore face, anatomy, body proportion, hair, clothes, pose, expression, or character palette as subject rules.

## Provisional visual direction

### Line

- Use a rough thin-to-medium pen contour rather than vector-perfect strokes.
- Allow restrained wobble, pressure variation, natural pauses, and irregular open gaps.
- Keep gaps around secondary turns; preserve the main silhouette at marker size.
- Avoid uniform dashed outlines, fuzzy brush texture, broad crayon, watercolor, or polished commercial line art.

### Fill

- Use a small set of clean, flat color shapes.
- Avoid complex gradients, photographic lighting, painterly texture, and high-gloss rendering.
- Permit slight line/fill misregistration only when the approved style anchors show it.
- Preserve the landmark's characteristic color relationships; do not copy a人物参考图 palette blindly.

### Composition

- Use a 1:1 transparent canvas.
- Keep the full landmark inside the frame with generous breathing room.
- Start STYLE TEST planning around a 70–78% maximum bounding-box footprint, then freeze the accepted value in the style lock.
- Center visual mass while retaining necessary asymmetry such as a tower, hill, or shoreline.
- Remove low-value detail before changing the landmark's primary silhouette.

### Tone

- Cute, slightly awkward, handmade, and travel-journal-like.
- Not preschool cartoon, glossy merchandise art, photorealism, refined 3D, or heavy commercial illustration.
- Do not add eyes, mouth, face, limbs, or anthropomorphic gestures.

### Nameplate and environment

- Render the exact Chinese landmark name once in a compact shared bottom nameplate. Treat it as part of the sticker silhouette, not a floating caption.
- Keep the nameplate below the landmark, clear of recognition-critical architecture, visually secondary, and consistent across the set.
- Render no other caption, slogan, pinyin, English, logo, watermark, UI, or invented signage.
- Include only context that carries recognition value. A hill behind a temple or water below a bridge may be essential; generic clouds, stars, flowers, or extra buildings are not.

## STYLE_REFERENCE card

Freeze this card before generating a comparison set:

```yaml
styleVersion: style-test-v0.1
status: provisional
approvedByUser: false
referenceFiles:
  - path-or-id-in-fixed-order
extractOnly:
  - line texture and weight
  - fill registration
  - palette behavior and saturation
  - negative space and footprint
  - shadow logic
  - composition breathing room
neverTransfer:
  - person identity
  - anatomy or body proportions
  - face, hair, clothes, pose, expression
line:
  weight: pending-review
  wobble: restrained
  openGaps: natural-and-irregular
fill:
  mode: simple-flat-colors
  colorCount: pending-review
  misregistration: pending-review
composition:
  canvas: 1024x1024
  background: transparent
  subjectFootprint: pending-review
  safeMargin: pending-review
  viewTendency: pending-review
whiteBorder: pending-review
shadow: pending-review
text:
  mode: exact-chinese-landmark-name
  placement: shared-bottom-nameplate
  extraText: forbidden
personification: forbidden
```

`pending-review` blocks generation unless the user explicitly asks for a controlled STYLE TEST of that one variable.

##人物参考图迁移规则

Translate visual language, not subject construction:

| 人物参考中可观察内容 | 迁移到景点 | 不迁移 |
|---|---|---|
| 钢笔轮廓的粗细、抖动、断点 | 建筑与自然轮廓的线条处理 | 头发边缘、脸部或肢体画法 |
| 色块数量、饱和度、轻微错位 | 屋顶、墙体、水面、山体的简化色块 | 肤色、发色、服装配色本身 |
| 角色周围的留白 | 地标主体周围的呼吸空间 | 人物在画面中的比例 |
| 阴影的有无与软硬 | 地标底部或接触面的统一处理 | 人脚落地、肢体遮挡规则 |
| 稚拙程度和不对称感 | 轻微手绘偏差与简化几何 | Q 版大头、小短腿、表情夸张 |

## Batch consistency lock

- Use the same ordered style references for every candidate in one round.
- Reuse the exact style card and prompt style block without rewriting synonyms.
- Freeze one value for line, fill, saturation, footprint, border, shadow, and view tendency.
- Let only the landmark feature lock change across different sights.
- Increment `styleVersion` after explicit approval. Never mutate an accepted version in place.
- Reject a candidate that is individually attractive but visually incompatible with the accepted set.
