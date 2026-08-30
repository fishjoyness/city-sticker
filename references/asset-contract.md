# Review Asset Contract v0.1

## Status boundary

Every generated v0.1 asset is `STYLE TEST`. This Skill does not copy files into the mini-program asset directory or update the production sticker manifest.

## Review output tree

```text
artifacts/
  sticker-tests/
    <city-slug>/
      <place-slug>/
        <style-version>/
          research.md
          landmark-lock.json
          style-lock.json
          manifest.json
          prompt.txt
          <place-slug>__style-test__<style-version>__c01.png
          <place-slug>__style-test__<style-version>__c01__marker-128.png
          <place-slug>__style-test__<style-version>__c01__inspect.json
          <place-slug>__style-test__<style-version>__c01__qa.md
```

Do not create the tree until an actual research or generation request needs it.

## Naming

- Use lowercase English kebab-case for folders: `nanjing/jiming-temple/`.
- Use deterministic place slugs: `nanjing-museum`, `jiming-temple`, `xuanwu-lake`, `terracotta-warriors`.
- Never use timestamps, hashes, random model filenames, Chinese filenames, `final-final`, or unversioned replacements.
- Candidate suffixes are stable: `c01`, `c02`.
- Increment the style version only after explicit review: `style-test-v0.1`, `style-v1`.

## Master image

- PNG with genuine alpha.
- Exact 1024×1024 canvas.
- sRGB color space when available.
- The exact Chinese landmark name is part of the visible sticker and always appears in the shared nameplate directly below the landmark.
- Safe margin, subject footprint, white border, and shadow come from the frozen style lock.
- Keep the master for review; do not load all 1024 px masters as map markers.

For public examples, keep two separate files:

- `<slug>_transparent.png`: genuine-alpha master suitable for downstream product preparation.
- `<slug>_preview.png`: the same artwork flattened only onto `#FFFFFF` for GitHub display.

Never ship a chroma-key, checkerboard drawing, white-backed preview, or other debug background as the transparent asset.

## Review thumbnails

- Generate at least 128 px; inspect 96 and 64 px during QA.
- Use high-quality Lanczos downsampling.
- Preserve alpha; do not add a white or checkerboard background to the saved thumbnail.
- Test visibility against temporary light and map-like mixed previews without baking those previews into the PNG.

## Future production handoff — disabled in v0.1

After the user approves the style and runtime sizes, a later workflow may:

1. promote an accepted master from `STYLE TEST` to a versioned production source;
2. export optimized 96/144/192 px variants as needed;
3. run lossless PNG optimization after resizing;
4. place runtime files under the mini-program sticker asset tree;
5. update the sticker manifest by `placeId`;
6. verify package size and marker rendering on device.

Do not perform these steps in v0.1.
