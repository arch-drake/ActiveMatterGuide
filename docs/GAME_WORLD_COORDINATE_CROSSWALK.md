# Game-coordinate crosswalk — source correlation, NOT live verification

As of **2026-10-20** · Reproducible derived coordinate transforms for the 12 playable raid maps that had a historic source coordinate sample.

## What changed
We compared 275 existing source-percentage map markers in Field Operations with [Portal Atlas' attributed Active Matter Help imports](https://github.com/rileyedward/portal-atlas/blob/main/docs/data-import.md). The importer retains `game_coords` triplets `[world X, elevation Y, world Z]` alongside normalized map percentages. The full game-derived coordinate system was not publicly validated against the current client.

**201 / 275** guide marker samples matched the imported world-coordinate metadata by source-image percentage to within **0.011 percentage points**; the other 74 were not direct matches under this test, often because they were conceptual zone labels, spatial polygons or differences in the imported record selection. Variant duplicate matches were accepted only if their world X/Z disagreed by less than 0.3 metres.

We derived two simple linear conversions **per map**:
`worldX = (a × normalizedMapX%) + b`; `worldZ = (c × normalizedMapY%) + d`.

The independently withheld source-record check validates internal transform consistency, **not** the location of a player, a building, an extraction point or a current game screenshot.

## Independent held-out test results

| Map | Direct source matches | Guide legacy sample count | Withheld controls | Source-coordinate RMS (metres) |
|---|---:|---:|---:|---:|
| airport | 22 | 22 | 6 | 0.02999 |
| cargo | 19 | 29 | 5 | 0.06646 |
| factory | 17 | 27 | 5 | 0.03990 |
| ozernoe | 14 | 20 | 4 | 0.03019 |
| dogorsk | 17 | 25 | 5 | 0.06346 |
| shegolskoe | 18 | 26 | 5 | 0.02829 |
| dam | 18 | 21 | 5 | 0.04308 |
| downtown | 20 | 29 | 5 | 0.03524 |
| headquarters | 11 | 21 | 3 | 0.04391 |
| military | 15 | 20 | 4 | 0.03541 |
| park | 19 | 22 | 5 | 0.05284 |
| scrapyard | 11 | 13 | 3 | 0.02083 |
| **Total** | **201** | **275** | — | *Per-map only* |

Highest map's held-out horizontal RMS: **0.06646 m**, measured against data imported from the same original community source. This small error must not be described as positional accuracy against the game.

## Responsible use in the guide

- The standalone [Reference Atlas](../tools/map_reference_atlas.html) now shows **source-inferred** world X/Z for selected legacy markers. It also accepts a world X/Z pair and returns the historic source-relative percentage location.
- Only when a **matching** actual game screenshot with 4 FIT / 2 CHECK anchors is loaded and explicitly approved may that point be drawn as a provisional crosshair on the screenshot.
- The 74 entries without a direct world-coordinate record are still inferred from the fitted regional transform; their marker identity and original placement are unverified.
- Gigastructure needs separate floor geometry; Dalniy Island regional overview needs a region-wide coordinate origin rather than mixing nine raid crops. Neither receives an invented 2D transform.
- World elevation `Y` is the **marker position's vertical coordinate**, not the building's height or floor count.
- The marker locations remain subject to patch/mode changes—particularly extraction relocation in Africa and Dalniy. The [official October 5 release](https://activematter.game/en/news/349) documented moved stationary extractions in Airport, Headquarters and Downtown.

## Reproducibility and provenance

The [JSON crosswalk](../map-evidence/world_coordinate_crosswalk_2026_10_20.json) includes per-map source blob SHA, matching method, 201/74 counts, 12 affine coefficients, training/withheld sample counts, and per-map horizontal residuals. It intentionally does **not** rehost whole third-party map rasters or third-party marker datasets.

**Accuracy states remain unchanged:** actual game-exact basemaps certified **0/14**, and independently current-game verified legacy marker positions **0/275**. This is a better mathematical bridge to current source screenshots, not a substitute for them.
