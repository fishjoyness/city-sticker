# Guangzhou City Sticker QA

Overall: **PASS — 15/15**

## Automated checks

- 15/15 formal files are 1024×1024 RGBA PNG with a real transparent background.
- 15/15 pass the 10% safe-margin and 80% maximum-footprint checks.
- 15/15 standard Chinese nameplates were added by the deterministic builder.
- 15/15 128 px markers and inspection reports were generated successfully.

## Semantic / small-size review

All assets were reviewed at full size and at 128/96/64 px against the locked research anchors. Names are accurate and no asset relies on the label for primary recognition.

| Landmark | Main recognition anchor | Result |
|---|---|---|
| 广州塔 | twisting hyperboloid lattice and antenna | PASS |
| 陈家祠 | ornate Lingnan ridge sculpture and three-bay hall | PASS |
| 沙面 | banyan boulevard and arcaded European façades | PASS |
| 石室圣心大教堂 | granite Gothic twin towers and rose window | PASS |
| 越秀公园五羊雕像 | five-rams monument group | PASS |
| 镇海楼 | five-storey red tower with green roofs | PASS |
| 白云山 | broad forest ridge, cloud belt and city below | PASS |
| 广东省博物馆 | carved-box red-brown façade | PASS |
| 永庆坊 | Xiguan lane, canal and Moon Bridge | PASS |
| 大佛寺 | stacked golden-lit urban temple frontage | PASS |
| 南越王博物院 | red-sandstone stepped burial-mound geometry | PASS |
| 海心桥 | asymmetric pedestrian arch and cable ribs | PASS |
| 花城广场 | long civic axis, opera house and supertalls | PASS |
| 黄埔军校旧址 | white barracks, green shutters and parade ground | PASS |
| 广州长隆旅游度假区 | roller-coaster loop, drop tower and wheel | PASS |

No formal asset is marked `NEEDS_REVIEW`.
