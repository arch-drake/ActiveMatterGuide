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