# Architecture: lasagna-style development

This repository prioritizes clear boundaries, focused modules and reversibility.

1. **Core and persistence** — storage key compatibility, serialization, migrations, full local backup.
2. **Data and validation** — map provenance, schema and version tags, source confidence.
3. **Application services** — navigation, selection, state transitions, imports and exports.
4. **Feature modules** — atlas, PvE/PvP, investigations, monsters, music and collectibles.
5. **Presentation** — accessible components, responsive layouts and themes.

Each feature should have its own data, UI, and tests. Dependency direction is inward: presentation calls services, not vice versa. Avoid hidden global mutations and overlapping event handlers. Do not refactor unrelated code without need.

**Release flow:** test modular sources → build the self-contained HTML → validate JS/HTML + all major controls → verify exported backups → update manifest and docs → bundle one complete offline ZIP. Changes to browser storage require a compatibility plan.

The standalone HTML and 2.1.1 release ZIP are present in this repo. The map calibration and visual installer source files may be newer than that packaged ZIP; never assume source-only workbench updates are included in the 2.1.1 download. Ship a refreshed ZIP only after guide integration and browser acceptance.
