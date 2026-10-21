# Active Matter // Field Operations 2.1 — Community Edition

Release: **20 October 2026**. Unofficial, free-of-subscription, standalone offline fan guide. No mods, memory reading, or automatic game interaction.

**New players:** read [docs/PLAYER_GUIDE.md](docs/PLAYER_GUIDE.md). GitHub Pages is currently disabled; download the [complete repo ZIP](https://github.com/arch-drake/ActiveMatterGuide/archive/refs/heads/main.zip), extract it, and open index.html for the Source Atlas. HTML views on github.com show source, not a running app.

## Quick start

1. Extract this ZIP. Open `active_matter_solo_pve_field_guide.html` directly in a modern Chrome or Edge browser. The single HTML embeds all required artwork and 11 original music tracks; separate assets are retained for reference and export.
2. Click **? Start here** for the six-step guided tour.
3. For actual source-grounded overhead references, open the **[primary Source Atlas](tools/all_maps_live_reference.html)**: 13 community raster reference areas (including Dalniy Island regional), plus a separate Gigastructure floor-only importer. Source tiles require opt-in and internet. The offline guide's **Maps** tab still contains 14 *illustrated legacy* panels, pseudo-isometric tilt, zoom and source-relative historic marker leads. These are **not** verified raid boundaries, surveyed elevations or authenticated current extraction pins.
4. Choose **PvP** for optional Solo Open Raid / Squad Open Raid planning and private after-action notes. The original Solo/Team PvE mode stays separate.
5. Choose **Homebase** for a beginner-friendly overview; **Signals** for cassette/recorder community leads and your personal collection journal.
6. Select from **12 themes** (including Field Notebook) and **3 layout densities**. The music dock has 11 original synth tracks, favorites, favorites-only shuffle/next, volume, and MP3 saving. No autoplay.
7. In **Backup**, export a full guide JSON backup **before switching from an older version**, moving the HTML to another path/browser, or clearing browser data. Restore from Backup as needed.

## Preservation and source-of-truth

- Retains the 53 documented investigation chains and 217 criteria, Solo/Team tracking, 20 monster/anomaly dossiers, the original 14 map artworks, all other legacy tools, and all 6 original music tracks.
- New storage uses separate `am_v21_*` keys, included in the existing complete backup export because it includes `am_` prefixed keys. Previous storage keys were deliberately not renamed or migrated.
- **Important:** Browser `file://` storage permissions and origins vary. Export and save the JSON backup from your older guide before switching. An HTML update does *not* carry the old browser's storage inside it.

## Accuracy limitations (must read)

- **Isometric is a presentation transform**, not a faithful 3D reconstruction. It does not provide real elevation, building heights, physical routes or surveyed geography.
- The 14 original tactical images and stylized terrain remain **illustrative artwork**; they are **NOT exact current game maps**. Community source markers and some polygons are source-relative and may be patch-sensitive. Same-crop in-game screenshots or appropriately licensed map assets are still needed for game-exact layouts and marker appearance.
- Gigastructure is Open-only in the documented guide; Dalniy is a regional overview. Map availability is patch-sensitive and must be checked against the in-game terminal.
- PvP tips are field-planning heuristics, not promises of successful tactics. Distinguish Open (rival players possible) from Isolated (PvE).
- Cassette recorder location hints are **anecdotal player reports**, not guaranteed cassette-track spawn locations. Do not confuse recorders with music cassettes.
- No guaranteed loot, speculative enemy damage multipliers, or unsupported quest completion promises have been added.

## Documentation

- `docs/CHANGELOG_2.1.md` — new features, fixes, and known gaps.
- `docs/MAP_PROVENANCE_AND_ACCURACY.md` — location and coordinate caveats.
- `docs/ORIGINAL_AUDIO_PERMISSIONS.md` — original synth music provenance.
- `docs/TEST_REPORT_2.1.md` — actual verification scope and untested environments.
- `source/README_DEV.md` — lasagna-layer code structure and reproducible patch notes.

No trademarks or third-party soundtrack are claimed by this unofficial guide. Game logos, map scans, and community images were not extracted or redistributed.


## Support

Optional one-time tips: https://buymeacoffee.com/elderdrake. The guide is completely free.

## October 20 source updates after 2.1.1 release

The [Map Reconciliation Workbench](tools/map_reconciliation.html) has been upgraded to compare a private reference map image and your in-game screenshot using named fixed physical landmarks. Historic candidate markers remain hidden during manually sourced calibration unless the source crop matches the historic dataset exactly. Marker-by-marker review results can be recorded in local evidence JSON. This newer workbench is **not guaranteed to be in the previously packaged release ZIP**.

The optional [Visual Upgrade 2.1.2 installer](tools/visual_upgrade_2_1_2.html) adds original conceptual artwork alongside encyclopedic records and location cards. It is a separate local browser tool, not a patch to current map geography and not yet an audited replacement 2.1.1 ZIP. Export a full guide backup before trying it. The current map-fidelity production status is in [the master plan](docs/MAP_FIDELITY_MASTER_ROADMAP.md) and [register](docs/MAP_PRODUCTION_REGISTER.md).
