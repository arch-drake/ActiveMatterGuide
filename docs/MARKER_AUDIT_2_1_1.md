# Embedded marker-data audit — 20 October 2026

**Scope:** Read-only structural inspection of the 2.1.1 offline HTML built-in `geoOffline` sample. This is **not** an in-game accuracy certification.

| Map | Source-positioned sample markers | Traced source polygons |
|---|---:|---:|
| Airport | 22 | 0 |
| Cargo Port | 29 | 10 |
| Factory | 27 | 10 |
| Ozernoe | 20 | 6 |
| Dogorsk | 25 | 8 |
| Shegolskoe | 26 | 8 |
| Dam | 21 | 3 |
| Downtown | 29 | 9 |
| Headquarters | 21 | 10 |
| Military Base | 20 | 5 |
| Park | 22 | 3 |
| Scrapyard | 13 | 2 |
| **Total** | **275** | **74** |

All 275 built-in marker x/y values were finite and within the 0–100 percent source-map bounds. There were zero exact duplicate records by marker code + normalized label + x/y. This does **not** prove the coordinates coincide with current game geography, match the correct crop, or are valid for every raid variant.

**Missing independent evidence:** exact current in-game icon artwork, source image calibration, live extraction positions, floors, structure height measurements, and surveyed geographic coordinates. Gigastructure and Dalniy Island have no verified local in-guide coordinate sets.

The E/T/K/D/Q/P/A/M/C/L/S letter markers are **guide-made category glyphs**, not verified reproductions of in-game icons. Official changes to objective/map presentation (e.g. 0.4.0.76) mean an old screenshot can be inaccurate for current icons: https://activematter.game/en/news/306.

## To complete reconciliation

For each map, obtain a current game-build screenshot with north/orientation and the full boundaries visible, record raid variant and image reuse rights, then register at least three non-collinear control landmarks. Measure transform fit error and review all relevant marker categories against live game displays. Do not assign 3D structure heights until floor counts or camera references support them.

See [Map Fidelity Evidence](MAP_FIDELITY_EVIDENCE.md). Known data provenance: https://github.com/rileyedward/portal-atlas/blob/main/docs/data-import.md (some Active Matter Help data has separate rights).
