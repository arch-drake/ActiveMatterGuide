# Active Matter // Field Operations 2.1 — Community Edition

Release: **20 October 2026**. Unofficial, free-of-subscription, standalone offline fan guide. No mods, memory reading, or automatic game interaction.

**New players:** see `docs/PLAYER_GUIDE.md` for installation, maps, PvE/PvP, music, backup and troubleshooting.

## Quick start

1. Extract this ZIP. Open `active_matter_solo_pve_field_guide.html` directly in a modern Chrome or Edge browser. The single HTML embeds all required artwork and 11 original music tracks; separate assets are retained for reference and export.
2. Click **? Start here** for the six-step guided tour.
3. Choose **Maps** for 14 switchable atlases. **Isometric: ON** tilts the map using a 2D visual transform; use the ↶/↷ buttons to rotate by 15°, +/- to zoom, drag to pan, and ⟲ to reset the rotation. Switch to Flat if you prefer a north-up coordinate grid. All map source coordinates are unchanged.
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
