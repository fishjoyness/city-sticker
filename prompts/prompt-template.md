# Landmark Sticker Prompt Template v0.1

Fill every bracket. Keep the `LANDMARK FIDELITY LOCK` and `STYLE LOCK` verbatim across candidates unless the user changes the version.

```text
ASSET STATUS:
STYLE TEST — NOT A PRODUCTION ASSET

ASSET:
City: [CITY_NAME]
Landmark: [LANDMARK_NAME]
Place slug: [PLACE_SLUG]
Candidate: [CANDIDATE_ID]

REFERENCE ROLES:
- Images [A...] are LANDMARK_REFERENCE. Use them only to preserve the real landmark's factual silhouette, signature structures, material/color relationships, and essential spatial context. Do not copy photographic lighting, weather, people, text, or exact composition.
- Images [B...] are STYLE_REFERENCE version [STYLE_VERSION]. Use them only for pen texture, line weight, wobble, line breaks, flat-fill behavior, saturation, negative space, simplification, border, shadow, and viewpoint tendency.
- If a STYLE_REFERENCE contains a person, do not transfer the person, face, hair, body proportion, clothing, pose, expression, or character palette into the landmark.

LANDMARK FIDELITY LOCK — DO NOT OMIT OR INVENT:
1. [PRIMARY SILHOUETTE]
2. [SIGNATURE STRUCTURE]
3. [RECOGNITION RHYTHM]
4. [CHARACTERISTIC COLOR OR MATERIAL, OR NONE]
5. [ESSENTIAL CONTEXT, OR NONE]

VIEW AND SIMPLIFICATION:
[PREFERRED VIEW]. Preserve the five locked features. Reduce low-value windows, ornament, vegetation, people, signs, cars, neighboring buildings, and temporary objects. The result must still be identifiable at 64–128 px.

STYLE LOCK [STYLE_VERSION] — REUSE VERBATIM:
[APPROVED STYLE LOCK]

COMPOSITION:
Exact 1:1, 1024×1024 transparent PNG master. Full landmark and bottom nameplate visible and centered by visual mass. Combined bounding box [SUBJECT_FOOTPRINT]. Minimum clear safe margin [SAFE_MARGIN] on every side. Abundant breathing room. No crop.

LINE:
[APPROVED PEN WEIGHT], rough hand-drawn pen contour, [APPROVED WOBBLE], natural non-uniform pauses and open gaps. Keep the primary silhouette readable. No vector-perfect curve, uniform dashed outline, fuzzy brush, crayon, watercolor, or polished commercial line art.

COLOR:
[APPROVED COLOR COUNT] simple flat colors with [APPROVED SATURATION]. [APPROVED FILL REGISTRATION]. No complex gradient, photographic shading, painterly texture, glossy highlight, or muddy vintage cast.

STICKER EDGE:
[WHITE BORDER DECISION — exact approved value]

SHADOW:
[SHADOW DECISION — exact approved value]

TEXT:
Render exactly `[LANDMARK_NAME_IN_CHINESE]` once in a compact shared bottom nameplate directly below the landmark. Use the approved simple Chinese sans-serif treatment, keep it legible and visually secondary, and do not cover the landmark. Do not render any other caption, abbreviation, pinyin, English, signage, logo, watermark, UI, or invented letters. Every Chinese character must be exact.

PERSONIFICATION:
NONE. No eyes, mouth, face, limbs, hands, feet, or character expression.

BACKGROUND:
Genuine transparency. No sky rectangle, paper texture, photo backdrop, city collage, extra landmark, or decorative filler without recognition value.

OUTPUT:
One candidate only. No contact sheet, mockup, packaging, map screenshot, or automatic variant batch.
```

## Research-only package

When image generation is not requested or the style lock is incomplete, return:

```text
STATUS: RESEARCH READY / GENERATION BLOCKED
CITY:
LANDMARK:
SOURCES:
RECOGNITION FEATURES:
UNRESOLVED STYLE FIELDS:
COPY-READY PROMPT:
```

Do not silently fill unresolved style fields.

## Targeted repair prompts

Use one correction at a time while retaining accepted dimensions.

### Landmark drift

```text
Preserve the accepted STYLE LOCK, canvas, palette, line, whitespace, border, and shadow. Repair only landmark identity: restore [EXACT FAILED FEATURE] according to LANDMARK_REFERENCE [SOURCE IDS]. Remove invented [WRONG FEATURE]. Keep every other accepted area unchanged.
```

### Style too polished

```text
Preserve the landmark geometry and composition. Repair only mark-making: reduce vector-perfect smoothness, introduce restrained irregular pen wobble and a few natural non-uniform contour gaps, and keep the main silhouette closed enough to read at 64 px. Do not add texture, grain, or uniform dashes.
```

### Too much detail

```text
Preserve all locked recognition features. Remove non-identifying ornament, tiny windows, incidental vegetation, people, signs, vehicles, and neighboring structures. Rebuild the remaining forms as simple flat color masses readable at 64 px. Do not enlarge the subject or change the accepted style.
```

### Marker unreadable

```text
Preserve the accepted style and factual silhouette. Strengthen only the [PRIMARY/SIGNATURE] feature, simplify competing interior details, and improve the separation between the main color masses. Keep the approved subject footprint, safe margin, border, shadow, and transparent background.
```

### False transparency

```text
Preserve the artwork exactly. Remove the rendered background and export genuine PNG alpha outside the sticker artwork. Do not draw a checkerboard, white square, paper texture, or cast-shadow floor.
```
