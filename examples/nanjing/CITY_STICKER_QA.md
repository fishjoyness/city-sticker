# 南京 City Sticker QA

Status: **PASS**  
Count: **15 / 15**  
Style: `pen-travel-v0.1`

## Reused assets

- 南京博物院
- 鸡鸣寺
- 玄武湖
- 中山陵

All four inherited transparent masters were retained and rerun through the current PNG inspector.

## New assets

- 明孝陵
- 南京总统府
- 夫子庙
- 秦淮河
- 老门东
- 牛首山
- 美龄宫
- 阅江楼
- 中华门城堡
- 朝天宫
- 南京长江大桥

## QA summary

- 1024×1024 PNG: PASS 15 / 15
- RGBA / genuine alpha: PASS 15 / 15
- Safe margin / footprint: PASS 15 / 15
- Exact Chinese bottom nameplate: PASS 15 / 15 — rendered deterministically by `build_examples.py`
- 128 px generated review: PASS 15 / 15
- 96 / 64 px visual reduction: PASS — primary silhouette and signature structure remain visible in the city showcase review
- Landmark identity: PASS — checked against `LANDMARK_RESEARCH.md` and inherited research
- Style consistency: PASS — same pen, fill, white contour, footprint, and nameplate system
- Personification / extra text / logo: PASS
- Blocking issue: NONE

## Repair record

- 阅江楼 first candidate: FAIL — excessive pagoda-like exterior floor stack.
- 阅江楼 repaired candidate: PASS — four visible exterior storeys, broad pavilion massing, green glazed eaves, red columns, Lion Hill and restrained river context.

