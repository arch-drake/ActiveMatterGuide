# Release delta — Field Operations 2.0.2 (2026-10-19)

## Changed

- **Map viewer defaults refined**: the offline atlas now opens in **Operational / coordinate** view rather than Tactical Detail, keeping the default closer to a game-map workflow and avoiding invented scenery when a same-crop in-game screenshot is not available.
- **Marker presentation tightened**: compact map pins now preserve more marker distinctions with explicit per-marker symbols/codes, including extraction, timed extraction, keys, documents, objectives, portals, anomalies, threats, caches, loot and landmarks.
- **Map UI polish**: clearer legend/status copy, cleaner compact pins, and a more readable operational presentation when labels are hidden.
- **Monster Compendium save safety**: observation notes now auto-save as you type in addition to the manual Save button, reducing data-loss risk during filter changes or card redraws.

## Not changed

- The 14 tactical-detail backgrounds remain **original artwork**, not verified in-game map captures.
- Exact geography and a claim of precise in-game visual fidelity still require same-crop current in-game screenshots or other licensable source imagery.

# Release delta — Field Operations 2.0 (2026-10-19)

## Added

- **14 integrated detailed tactical art maps**: new decorative building masses, roads and environmental identities. The documented source-coordinate polygons and pins retain their separate coordinates. Tactical Detail is now the default atlas background; Topographic, Coordinate, Illustrated and Personal Screenshot views remain accessible.
- **20-entry Monster & Anomaly Compendium** with searchable creature families, risk filters, Solo/Team engagement variants, practical/official vulnerability evidence, loot and remains caveats, map and investigation jumps. Manually record sightings, confirmed defeats, retrieved samples and field notes. Export local encounter journal to JSON.
- **Four new original synth ambience tracks**, joining Fracture Signal and Shelter Afterglow. Six tracks total. Next, Shuffle, volume, play/pause and Save MP3 work inside the embedded player; default player starts minimized and never autoplays.
- **Five additional color themes**: Reactor/Emerald, Rift/Violet, Blood Moon/Red, Obsidian/Steel, and Signal/High Contrast, joining Fracture/Amber and Shelter/Ice Blue. Saved theme preferences preserved.
- **Quick command palette** (Ctrl+K /), searchable destinations and favorite pages; Resume previous tab option.
- **Handoff tab** with browser-local progress summary, editable continuation prompt, copy/download controls and a shortcut to backups.
- Improved compendium layout and artwork-mode accuracy warnings. All pre-existing legacy tabs retained via All tools.

## Retained

- 53 researched investigations / 217 documented stage criteria, separate Solo/Team progression.
- Local map markers, optional full map data importer, source geometry, snapshot alignment, map filters, notes, quests, sleeves, loot, lore and prior journal modules.

## Validation evidence

- 5 JavaScript blocks pass `node --check`.
- No duplicate HTML IDs; 101 navigation tab targets resolve to sections; two legacy duplicate-topic sections deliberately remain off primary navigation.
- Browser set-content smoke suite: **20/20 passed** (all fourteen detailed map views, map filters, threat filters, local encounter notes under mocked browser storage, all six tracks, seven themes, command palette, backup visibility and handoff). No JS page errors in the test run.
- Full navigation on file:// and real persistence across browser restarts were **not** verified here due administrator browser navigation restrictions; test those on your PC. Local storage was simulated only for the browser suite.

## Unfinished/patch-sensitive

- Original illustrated geography is **not a verified screenshot of the game**. Replace with licensed/current official asset data or user screenshots and align before using for actual navigation.
- Compendium drop probabilities and damage multipliers intentionally not asserted where sources do not verify them.
- 53 researched investigation entries are not guaranteed to be exhaustive as the live game receives updates.
