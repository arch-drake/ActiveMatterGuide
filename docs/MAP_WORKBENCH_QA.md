# QA report — 20 October 2026

- Verified 14 map selection entries; 12 coordinate-sample maps + 2 conceptual-only maps.
- Source marker total: 275; Airport count: 22.
- Standalone JavaScript syntax: `node --check` PASS.
- Actual headless Chromium interactive test, with `page.set_content()` because this runtime blocks direct local file/browser navigations: PASS.
- Generated a synthetic 1240×800 screenshot, matched five dispersed known points using a manufactured affine matrix, and fitted RMS 0.030% (browser click rounding).
- Verified projected pins: 22 visible for Airport (subject to in-image bounds).
- Evidence-height form, JSON export, reimport, per-map separation, and unsupported map no-anchor behavior: PASS.
- Zero browser JavaScript exceptions during test.

### Not verified

- No native `file://` reload/restart persistence test; behavior may differ by browser security context.
- No real user/game screenshot was available; no geography, building height or icon style validated.
- Browser performance with thousands of full source markers is outside the present 275-sample tool.
- No API or online services are used; screenshot and evidence remain local unless you explicitly export/share.
## Follow-up source audit — 20 October 2026 (commit be922716)

Changes to the published **source workbench**, after the above headless-browser report:

- Fit points and independent check points are now stored with distinct roles. Checks are excluded from affine least-squares calibration and reported as a separate holdout RMS. Existing evidence without a role stays compatible as a FIT point.
- Import validation now rejects duplicate/altered source marker coordinates and nonnumeric building-height entries. This also closes an HTML-injection risk from imported height values.
- The interface explicitly flags potentially mobile extraction/anomaly controls and the 0.4.0.173 extraction changes.
- The edited JavaScript compiled successfully in the connected source runner. **Four deterministic geometry cases passed:** exact affine training plus held-out validation, displaced holdout detected (5.657% RMS), insufficient controls rejected, collinear controls rejected.
- **Not retested here:** actual browser clicking, upload/download dialogs, GitHub Pages rendering or local file persistence after this edit. The prior browser report applies only to the earlier code. No real in-game screenshot was evaluated. An updated ZIP was **not** built by this source commit; downloaders of the 2.1.1 ZIP may still have the earlier workbench.

Official patch source for extraction changes: https://activematter.game/en/news/349 (5 Oct 2026).

## Supplemental deterministic check — 20 October 2026 (dual-image source revision)
- GitHub source JavaScript compiled successfully after the dual-image physical-landmark addition.
- New `tests/map_fidelity_workflow.test.cjs` checks the 14-map/275-marker register, required DOM control names, legacy-coordinate-crop overlay guard, affine alignment from four named FIT controls, independent two-point CHECK, detection of a displaced holdout, and import rejection for invalid/duplicate/spoofed coordinates.
- The Node test's logic also ran in an isolated JavaScript environment with in-memory file fixtures: PASS. **Not equivalent to a real Node filesystem run or browser manual-upload test.**
- Manual physical anchors have ID format `manual-<digits>-<digits>`, source and target coords in 0–100%, labels escaped in UI, and FIT/CHECK role in v1 evidence JSON. Existing historic marker imports stay supported.
- The reference image's height limit was changed to scroll instead of object-fit letterboxing, so clicks map to the image rectangle.

**Remaining:** interactive Chrome/Edge target/source upload, click accuracy at different aspect ratios, same-build real screenshots, evidence review, and correct legal approval for redistributed map art. No 1:1 basemaps were released by these changes.

## Map-fidelity board source review (20 Oct)
- Added a self-contained map status board for all 14 entries, 275 historic samples total, concept vs source-sample distinction, search/priority/coverage filters and offline local per-map marker review counts.
- Map links pass a validated `map` query parameter to the workbench; unknown values are ignored.
- Dashboard JavaScript parsed successfully; its output and responsive layout have not been manually reviewed on Windows. No basemap geometry was imported.

## GitHub Actions CI status (21 October UTC)
- Added `.github/workflows/map-fidelity-ci.yml` to run dependency-free Node checks on map changes.
- First job [run 39519786878](https://github.com/arch-drake/ActiveMatterGuide/actions/runs/39519786878) completed **failure** approximately two seconds after starting; GitHub API lists no individual steps, and the job-log endpoint returned a missing blob.
- **Root cause not confirmed.** Do not claim CI passed or that this was a specific test failure. In-container and isolated-JavaScript deterministic checks passed separately. Confirm Actions is enabled/runners are usable, retry, then investigate logs.
