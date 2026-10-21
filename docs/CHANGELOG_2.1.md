# Release delta — 2.1 Community Edition (2026-10-20)

## Added
- Optional **PvP Field Operations** tab for Open Solo / Open Squad planning, cover/retreat checklists, after-action notes, JSON export and separate PvP storage.
- **All 14 atlases switch between flat and pseudo-isometric**, with 15° rotation, zoom, pan and reset. Rotation uses a 2D affine projection; inverse mapping preserves manual pin placement. Preferences save locally.
- **Six-step guided tour** and **Homebase Systems** cards, maintaining source/recipe accuracy caveats.
- **Signal Archive**: personal music cassette journal, clearly labeled community anecdotes for cassette recorders, source links and local JSON export.
- **Five themes**: Soviet Terminal, Monolith Research, Containment Breach, Anomaly Field, Field Notebook (12 total).
- **Three layout densities**: Standard, Compact and Accessible.
- **Five original procedural MP3s**: Dead Relay, Monolith Dream, Red Zone, Glass Reactor, Dawn After Extraction (11 total). Favorite tracks and optionally shuffle/next favorites only.
- Modular `source/modules/` JS layers, original audio generator, browser smoke/deep tests, documentation updates.

## Preserved
- Prior source-relative marker coordinates, existing personal-note keys, investigation progress, Solo/Team PvE records and compendium data.
- All 14 original tactical images, six earlier synth loops and all original guide tools.
- Single-file HTML distribution and complete browser-side export/restore, including new `am_v21_*` keys.

## QA and known limits
- 6 script blocks pass JavaScript parse checks, zero duplicate IDs and all data-tab links resolve.
- Browser smoke 11/11 pass; extended 13/13 pass (56 map render combinations, marker selection and isometric-note placement, PvP, signal notes, theme/density, favorites, backup, original state preservation). No page errors observed.
- Browser testing used `page.set_content` plus simulated storage because real file:// and localhost navigation were administratively blocked; it does not prove actual persistence across PC browser restarts.
- The map backgrounds are artistic, not game-exact. All in-game marker artworks, 3D elevations, and precisely aligned variants require game screenshots and rights review. No sourced game-image assets are redistributed.

## 20 October 2026 — source follow-up (not a new full release)

- Added complete 14-map fidelity roadmap, Airport benchmark, per-map production register and machine-readable 275-sample candidate status.
- Added dual-image **physical landmark** calibration to the standalone map reconciliation tool (source + target in-game screenshots, FIT and CHECK points).
- Added same-coordinate-crop guard to prevent automatic historic marker overlays against differently cropped input source images.
- Added per-marker review status, evidence link, game build/variant and local export/import support. Original coordinates remain unchanged; user reviews are not independent certification.
- Added offline optional [2.1.2 concept-art installer](../tools/visual_upgrade_2_1_2.html) with 32 atmosphere scenes. The complete 2.1.1 bundled guide has not been rebuilt as a new downloadable release ZIP here.
- Expanded map-issue template, CONTRIBUTING instructions and deterministic regression checks. JS syntax plus geometry/import/review deterministic tests passed; real current-build screenshot and interactive browser acceptance are **not done**.
- Original basemaps still illustrative. Current screenshot-authenticated game geography 0/14; independently authenticated candidate markers 0/275.

- Added polished offline [map fidelity status board](../tools/map_fidelity_dashboard.html) showing the 14 original thumbnail illustrations with clear "not certified" status and deep links to map-specific calibration tools; no fabricated geometry or game texture was added.

## Online source-correlation follow-up — 20 October 2026

- Reviewed all 13 reference raid-map regions and all 30 named raid-variant pages; saved 30 unique, page-verified URLs in `map-evidence/online_source_correlation_2026_10_20.json`.
- Upgraded [14-map dashboard](../tools/map_fidelity_dashboard.html) with geographic classification, source-reported extraction-system candidate totals, patch warnings and expandable links for each variant.
- Added comprehensive [map-by-map research report](ONLINE_MAP_CORRELATION_2026_10_20.md), including official patch change crosswalk and independence caveats where fan atlases copy each other's marker datasets.
- New deterministic source-integrity test checks 14 views, 13 actual playable regions, all 30 unique source reference URLs, unchanged 275 legacy samples, and military Unstable Zone behavior. Passed locally in isolated JS with in-memory file fixtures. GitHub Actions runner remains separately unresolved.
- No authentic game baselayers or rehosted third-party map tiles bundled; no claim of 275 coordinate verification or correct isometric building heights.

## Reference Atlas and provenance gate — 20 October source update

- Added `tools/map_reference_atlas.html`: standalone screenshot-grounded cartographic viewer, 14 location selectors, 30 named raid-variant references, drag/zoom, searchable historic marker candidates, exact screenshot evidence compatibility gate and no remote image uploads.
- Workbench now records `raidVariant` and screenshot `screenshotSha256` (SHA-256 when browser crypto permits). Import/export retains backward compatibility with older evidence; exact name+size without hash is not sufficient for automatic projection.
- Old sample marker pins are hidden unless 4 FIT/2 independent CHECK, matching map, image, mode, patch and variant, and verified coordinate crop. The visitor must explicitly turn on provisional pins.
- These tools do **not** replace 14 historic illustrative backgrounds with authenticated source geography. New viewer shows a real image only after the reader supplies one locally.
