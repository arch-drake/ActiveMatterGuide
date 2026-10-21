# Active Matter — geographic fidelity development checkpoint (20 October 2026)
Status: **tools and research complete for this iteration; geographic basemap replacement remains blocked by unavailable authentic source images / crop metadata.** Main public guide remains v2.1.1. These changes are source-level improvements on main, not a separately QA-certified 2.2 full-guide ZIP.

## Shipped into GitHub main
- Standalone [Reference Atlas](../tools/map_reference_atlas.html): 14 selectable views, 30 raid variants, 275 searchable historical source marker samples; load **player-owned real in-game map capture** locally, zoom/pan, mode/build/variant and SHA-256 gating, strict 4 FIT/2 CHECK before optional provisional pin rendering, and engine X/Z lookup and per-map CSV export.
- [Map Reconciliation Workbench](../tools/map_reconciliation.html): dual-image physical landmark matching, independent holdout geometry, per-marker user reviews, build/variant/source fields, screenshot identity digest where supported, JSON import/export.
- [Map Fidelity Board](../tools/map_fidelity_dashboard.html): source variant links, geo region labels, patch risks, per-map coordinate match coverage.
- [World coordinate crosswalk](../map-evidence/world_coordinate_crosswalk_2026_10_20.json): separate 12-map game-world X/Z affine transforms from 201 direct third-party-source matches; 74 older samples have only inferred source-world coordinates. [Detailed match register](../map-evidence/legacy_marker_world_estimates_v1.json).
- [Source correlation](../map-evidence/online_source_correlation_2026_10_20.json): covers all 30 named variant source pages; original 275 guide sample values preserved.
- Existing 2.1.2 [editorial art installer](../tools/visual_upgrade_2_1_2.html) still available as separate optional artwork, not a geographic image.

## Validation carried out
Six deterministic / simulated-DOM suites executed against current repository content and all passed:
`map_reference_atlas.test.cjs`,
`map_reconciliation_checks.test.cjs`,
`map_fidelity_workflow.test.cjs`,
`map_online_correlation.test.cjs`,
`map_world_coordinates.test.cjs`,
`map_reference_dom_smoke.test.cjs`.

Tests include fit/check geometry, wrong game build/mode/variant, screenshot identity mismatch, source crop incompatibility, 14-map selector/marker display wiring, original marker preservation and invertible world-coordinate transforms. These test simulations are **not** browser permission checks, actual gameplay validation or visual comparison with the real game.

GitHub Actions returned repeated jobs with no steps or logs before test execution. Auto-triggering was temporarily disabled (manual dispatch remains) to avoid spamming failed runs. This is not a green CI or a claim of test failure within Node.

## Actual geography acceptance remains incomplete
- Authenticated game-exact and copyright-permitted basemap replacements: **0/14**.
- Independently in-game-confirmed current marker placements: **0/275**.
- The 12 world-coordinate conversions are internally consistent against **shared source data**, not independently certified location/patch accuracy.
- Building actual height / floor footprints and tunnel routes are not surveyed. World game Y coordinate of a marker is not the height of a building.
- Region Dalniy is a regional view, not a separate raid. Gigastructure needs independent floor topology; Park needs underground floor plans. Steam developer [confirms underground Park maps](https://steamcommunity.com/app/2887580/discussions/0/591813437999457670/).
- The source third-party game-derived raster tiles are externally linked only. Exact image licensing/rehosting terms, whole-pyramid bounds/zoom, and crop alignment are not established.

## Next authentic-data intake (this is the actual blocker)
To replace the fabricated basemap backgrounds honestly, supply either:
1. current-build flat, full screen in-game map captures for each raid/variant with orientation/legend, or
2. a permissioned complete tile raster pyramid with region bounds, projection, raid crop polygons and build provenance.

Airport is the benchmark. Use a current-build capture including runway, hangars, taxiway junctions and gravity/aircraft landmark. Four dispersed fixed FIT points and two independent CHECK points are minimum; review its 22 historic markers with the post-0.4.0.173 exit changes. Do not publish a polished inaccurate rendition.

After authentic geography is cleared, trace true coastlines/roads/roofs for a flat navigational layer, then add controlled rendering improvements. Buildings get height only when supported by multiple views or actual measurements. Test the whole shipping HTML backup/restore separately; the source-only atlas does not alter existing player progress.

## Support
The guide is free and independent. Avoid falsely claiming developer endorsement, exact map imagery, or guaranteed loot. Full screenshots and private browser backups stay local; do not attach credentials to public GitHub issues.
