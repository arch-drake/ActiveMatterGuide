# Field Operations 2.1 — QA report

## Validated in this build

- Structural: every JavaScript block (`node --check`), no duplicate HTML IDs, all navigation targets resolve.
- Browser (headless Chromium using `page.set_content`): 11/11 smoke cases, 13/13 extended cases, zero captured JavaScript page errors.
- Map: 14 choices × 4 supported artwork/coordinate views = 56 render checks; iso on/off, clockwise/anticlockwise rotation, zoom, reset, click-to-select marker, and centered personal pin creation under projection.
- PvP: independent Solo/Squad checklist key, text-safe after-action notes, export path exposed.
- Signals: journal entry saving and mark-collected; evidence links shown.
- Music: 11 track options, favorite/favorites-only option; 11 original MP3s separately included. All user activation; no autoplay.
- Themes: all 12 can be selected; three display densities.
- Backup: full export with seeded legacy keys and all new keys; original legacy values unchanged after feature interactions. The browser storage in this test was a JavaScript shim, NOT actual `file://` disk persistence.

## Explicit limits

- Full manual UI regression across 90+ historic tools was NOT performed; no claim of complete coverage.
- Genuine file:// or localhost navigation and browser-restart persistence could not be tested under browser administrator restrictions. Test manually on end-user PC.
- No official in-game map screenshots were available for 1:1 alignment, elevations or icon matching.
- Game patch-sensitive locations, resources and PvP mechanics remain labeled as source-derived/community and require in-game verification.

## Suggested acceptance run on Windows

1. **Export your old complete backup** before upgrading.
2. Open the included HTML from an extracted folder, load the old JSON backup using Backup, and inspect existing investigation/monster/personal map entries.
3. Open Maps, switch every location and view; rotate/zoom an isometric map, mark a test personal pin, switch Flat and back, and re-check location.
4. Try PvP, Signal Archive, themes, 11 music tracks and volume/favorites; check no autoplay.
5. Close/reopen the HTML in the same browser profile; verify progress and preferences. Export a new full backup; test restore on a clean browser profile.
