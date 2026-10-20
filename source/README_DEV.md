# Developer notes — lasagna architecture

The **shipped offline HTML** is the runtime source of truth and embeds all art/music. Modules are also available individually under `source/modules` for review and focused testing:

- `01_core.js`: namespaced utility, typed JSON persistence and safe text rendering.
- `02_pvp.js`: PvP controller and independent data model.
- `03_music_collectibles.js`: cassette journal, community references and music dock entry.
- `04_homebase_tour.js`: onboarding and homebase explainer.
- `05_accessibility_music.js`: density presets and favorite-track handling.

The legacy map application is a large existing closure. Isometric support was integrated with a **small, targeted patch** using invertible 2D math, keeping all original progress keys, marker IDs, and map content stable. New features do not import or monkey-patch unrelated functions.

For historical reproducibility, `build_v21.py` and `polish_v21.py` are the two staged patchers applied to the **verified 2.0.2 HTML**; they are not re-run against the compiled 2.1 HTML. Additional final style/music refinements are reflected in the compiled release and modules (see changelog). Do not run patchers blindly or more than once; begin with a pristine verified 2.0.2 source copy.

Audio generation is optional for developers: requires NumPy, FFmpeg, and Python; end-user HTML works with no dependencies or network. The procedural generator uses deterministic seeds and no external samples.

Browser tests are under `source/tests`. They require Playwright and a Chromium binary. This testing environment blocks page navigation for local/localhost URLs, so the tests use in-memory `set_content`; `qa_deep.py` stubs browser localStorage only for test isolation. Do not imply that these prove file:// browser restart persistence.

Rules for future work: keep one layer per concern, no broad refactors without acceptance, preserve storage contracts and coordinate provenance, and require tests with every new public release.
