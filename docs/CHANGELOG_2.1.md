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
