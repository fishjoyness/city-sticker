# Guilin City Sticker QA

Overall: **PASS — 15/15**

## Automated checks

- Canvas: 15/15 are 1024×1024 PNG.
- Color mode: 15/15 are RGBA with a real alpha channel.
- Transparency: 15/15 contain fully transparent background pixels.
- Safe margin: 15/15 pass the 10% minimum on every side.
- Visible footprint: 15/15 remain within the 80% maximum.
- Standard Chinese nameplate: 15/15 added by the deterministic asset builder.
- 128 px markers: 15/15 generated successfully.

## Semantic and small-size review

All formal assets were compared against the locked anchors at full size and at 128/96/64 px. The primary silhouettes remain readable and the labels are spelled correctly.

| Landmark | Alpha / margin | 128·96·64 | Landmark fidelity | Result |
|---|---|---|---|---|
| 象鼻山 | PASS | PASS | elephant-trunk arch and river | PASS |
| 漓江 | PASS | PASS | broad river and layered needle karst | PASS |
| 日月双塔 | PASS | PASS | paired gold/silver towers | PASS |
| 两江四湖 | PASS | PASS | linked waterway and ornamental bridge | PASS |
| 芦笛岩 | PASS | PASS | colored cavern and dense formations | PASS |
| 独秀峰 | PASS | PASS | solitary pinnacle above prince-city roofline | PASS |
| 七星景区 | PASS | PASS | Flower Bridge as the accurate stable anchor | PASS |
| 伏波山 | PASS | PASS | riverside cave, cliff and pavilion | PASS |
| 叠彩山 | PASS | PASS | folded strata, wind cave and summit pavilion | PASS |
| 龙脊梯田 | PASS | PASS | contour terraces and timber village | PASS |
| 遇龙河 | PASS | PASS | intimate river, raft, old bridge and weir | PASS |
| 阳朔西街 | PASS | PASS | enclosed old street and karst terminus | PASS |
| 十里画廊 | PASS | PASS | long cycling corridor and distant Moon Hill | PASS |
| 兴坪古镇 | PASS | PASS | old street, landing and Xingping karst wall | PASS |
| 银子岩 | PASS | PASS | bright silver calcite and mirror pool | PASS |

## Repair log

- 七星景区 v1: rejected because a fabricated mountain opening replaced the Camel Hill/Flower Bridge anchors.
- 七星景区 v2: rejected because the hill was anthropomorphized into a literal camel head.
- Final: uses the historic multi-span Flower Bridge as the dominant verifiable anchor with ordinary non-fantasy karst behind it. The two rejected source images are retained and excluded from the manifest/formal outputs.

No formal asset is marked `NEEDS_REVIEW`.
