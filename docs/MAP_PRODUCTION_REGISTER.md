# All-map production register — source-to-release
Last checked: 2026-10-20 · Accurate basemaps: **0 of 14 verified** · Current-screenshot-authenticated markers: **0 of 275**.
**Legend:** CANDIDATE = historic percent-coordinate source sample; CONCEPT = illustration with no comparable coordinate dataset. These are **not counts of all game POIs**.

| # | Map | Legacy sample markers | Basemap | Priority | Patch/variant risk | NEXT required artifact |
|---:|---|---:|---|---|---|---|
| 1 | Airport | 22 | Illustration | **P0 benchmark** | stationary exits relocated 0.4.0.173; gravity / vertical overlap | same-build map + 4 FIT / 2 CHECK |
| 2 | Headquarters | 21 | Illustration | P0 | exits relocated 0.4.0.173 | same-build Africa map + landmark set |
| 3 | Downtown | 29 | Illustration | P0 | exits relocated 0.4.0.173; Collapse variant | same-build city screenshot + variant mask |
| 4 | Dam | 21 | Illustration | P1 | water ladders / gravity stair fixed | current top-down dam and bridge/catwalk evidence |
| 5 | Cargo Port | 29 | Illustration | P1 | barge portals/teleport zones, 0.4.0.192 | current dock layout and source citation |
| 6 | Factory | 27 | Illustration | P1 | factory boundaries and fences patch-sensitive | building footprints with access tiers |
| 7 | Dogorsk | 25 | Illustration | P1 | dynamic exits; 0.4.0.192 scenery fix | screenshot + dynamic exit behavior |
| 8 | Military Base | 20 | Illustration | P1 | Unstable monster-artifact marker timing 0.4.0.192 | current PvE/Open/Unstable reference |
| 9 | Ozernoe | 20 | Illustration | P2 | green fences updated 0.4.0.192 | settlement geometry from real map |
| 10 | Park | 22 | Illustration | P2 | greenhouse / subterranean links | surface and underground level split |
| 11 | Scrapyard | 13 | Illustration | P2 | overlapping container/hangar interiors | exact hangar / junkyard footprints |
| 12 | Shegolskoe | 26 | Illustration | P2 | elevations and route cutoffs | current town geometry / route geometry |
| 13 | Gigastructure | 0 | Concept schematic | P3 | multi-floor traversal; no compatible coordinates | authenticated floor plans, one per level |
| 14 | Dalniy Island | 0 | Regional concept | P3 | region overview is not an individual raid | authenticated region outline; local raids separate |
| | **TOTAL** | **275** | | | | |

## Production checklist — repeat for every row
- [ ] Assign `map_id`, build, release mode, timestamp, coordinate system and orientation.
- [ ] Inventory potential source images; credit author and keep explicit publication rights record.
- [ ] Verify source is actual game overhead map, not another guide's imaginative redraw.
- [ ] Record screenshot dimensions + crop/orientation + SHA256.
- [ ] Identify stable fit landmarks; keep separate independent check points.
- [ ] Record geometry calibration metrics and disagreement reasons.
- [ ] Trace visible physical geometry; flag occlusion and unknown footprints.
- [ ] Evaluate legacy candidate pins one by one, in relevant variants.
- [ ] Audit changed extraction positions after official patch, record source version.
- [ ] Produce accurate **flat** reference layer first. Enhanced styling cannot shift measured geometry.
- [ ] Use height/volume only after oblique/measurement evidence; unknown remains 2D.
- [ ] QA markers, icons, legends, pan/zoom/rotation, local notes, dark-theme contrast, backup.
- [ ] Add per-map screenshots of test output and reviewer name/date.
- [ ] Update manifest/status from candidate to checked only after evidence signoff.

## Art and release separation
The offline visual addon contains category-level cinematic concept scenes for entries and location selector. It is **not** a geographic basemap replacement. Retain concept art as labelled editorial side panels and avoid letting it obstruct navigational icons.

## Updating status
Create a map correction issue with source build + raid variant and link to exported evidence JSON. Do not attach browser backup or authentication credentials. Update this table and audit manifest only when supporting proof is recorded. See [contributing](../CONTRIBUTING.md) and [fidelity standards](MAP_FIDELITY_EVIDENCE.md).

References: https://activematter.game/en/news/349 · https://activematter.game/en/news/356
