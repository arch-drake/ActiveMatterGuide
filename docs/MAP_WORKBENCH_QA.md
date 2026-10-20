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
