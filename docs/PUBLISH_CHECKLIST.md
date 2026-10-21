# Map overhaul source updates — publication and sign-off status

**October 20 link audit:** all existing root HTML and 2.1.1 ZIP assets are in GitHub; GitHub Pages is **disabled**, and the GitHub Releases collection initially contains **no releases**. Player instructions were updated to prefer an extractable repository archive, not a nonfunctional Pages or GitHub HTML source-view link. See [Owner publication steps](../OWNER_PUBLICATION_STEPS.md) and [Alpha notes](ALPHA_RELEASE_NOTES.md). A public [maps-only alpha ZIP](https://github.com/arch-drake/ActiveMatterGuide/blob/alpha/v2.2.0-alpha.1/downloads/ActiveMatter-SourceAtlas-v2.2.0-alpha.1-MAPS-ONLY.zip) now exists on the alpha branch and can be downloaded directly. **A formal GitHub prerelease remains blocked:** the Actions workflow runs failed before any steps (no runner executed). Pages also remains disabled. Do not claim either as live.
Checked: **20 October 2026** · Source branch: `main`

## Already present
- Existing root standalone guide `active_matter_solo_pve_field_guide.html` and `downloads/Active_Matter_Field_Operations_2_1_1_Community_Edition.zip` are both in GitHub. Preserve them as published baseline assets.
- Existing 14 illustrated map textures remain in `assets/maps/` and eleven original music tracks remain in `assets/music/`.
- New tools: `tools/map_reconciliation.html` (dual-image FIT/CHECK calibration, per-marker review status), `tools/map_fidelity_dashboard.html` (14-map board), and `tools/visual_upgrade_2_1_2.html` (optional 32-scene offline artwork installer).
- Evidence roadmap and machine-readable 14-map registry are in `docs/MAP_FIDELITY_MASTER_ROADMAP.md`, `docs/AIRPORT_BENCHMARK.md`, `docs/MAP_PRODUCTION_REGISTER.md`, `map-evidence/map_fidelity_register.v1.json`.
- README and landing page link to the current tools and disclose verification limits.

## Source code checks completed
- Workbench and dashboard inline JS **syntax compilation**: pass.
- Deterministic geometry, holdout control and import/review validation tests: pass in isolated JavaScript using in-memory fixtures.
- Visual upgrade installer: actual Chromium smoke against the earlier 2.0 HTML: pass, including all 20 monster dossiers and 14 location visuals; the exact 2.1.1 combination has only passed structural prerequisites, not browser acceptance.

## NOT YET released / verified
- **No exact game-geography basemap is complete.** All 14 existing textures remain illustrative. The patch-sensitive 275 legacy marker samples are not independently authenticated. No source rights or game screenshot evidence is implied by these commits.
- The current 2.1.1 release ZIP has not been repackaged with the newer dashboard/workbench/art installer source. GitHub main contains newer source files than the ZIP. A standalone combined 2.1.1+2.1.2 HTML upload was attempted but rejected as oversized; no combined file was published.
- No Windows file:// click/upload/restore acceptance of the new workbench; no source screenshot geometry/height validations; no GitHub Pages serving audit.

## Before tagging a new full release
1. Run `node tests/map_reconciliation_checks.test.cjs` and `node tests/map_fidelity_workflow.test.cjs` from a checked-out repository.
2. Open `tools/map_fidelity_dashboard.html` locally, click every map card, upload two test images through the workbench, record FIT and CHECK anchors and one marker decision, export/import evidence JSON. Verify no screenshots leave the page.
3. Test at least two aspect ratios and zoom levels, source/crop mismatch warning, reset and empty-map behavior, keyboard operation, and failure handling.
4. Test the 2.1.2 visual installer on the exact root `active_matter_solo_pve_field_guide.html`, including 20 monster portrait positions, 14 location scene cards, all existing map click/zoom behaviors, and old progress backup compatibility.
5. Obtain the current permissioned game-map screenshots, crop and orientation evidence per map; only then promote individual flat/height layers to accurately verified.
6. Rebuild a fresh audited offline release ZIP from the exact tested source, update preview images, manifest and release notes, and then tag a release.
7. Publish GitHub Pages only after visual/navigation/accessibility checks at actual deployment URL; do not assert Pages is live just because source files are committed.

Owner's [map production register](MAP_PRODUCTION_REGISTER.md) and [master roadmap](MAP_FIDELITY_MASTER_ROADMAP.md) are the source of truth for remaining items.

**Status policy:** `source merged` ≠ `browser verified` ≠ `game geographically authenticated` ≠ `bundled release published`.
