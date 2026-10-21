# Cross-source reconciliation register — 20 October 2026

**Scope:** the entire 14-view guide. The source wiki's [map index](https://activematterhelp.ru/wiki/maps) lists **13 playable regions / 30 named variants**: 9 Dalniy raid regions, 2 Africa (Airport and Headquarters), Downtown in Abandoned America, plus Gigastructure. The guide's extra Dalniy Island view is a **regional overview**, not an extra queue entry.

**State:** all 30 current wiki-listed variant links resolved and written to [JSON](../map-evidence/online_source_correlation_2026_10_20.json), and every visual map card now links directly to its specific variant(s). The 275 historic candidate markers remain unchanged; **none were authenticated against an actual current game capture by this research pass**.

## Comparison — source-reported extraction system (default/reference variant only)

| Guide view | Geography | Wiki-reported permanent / timed / final *candidate exits* | Historical guide samples (all types) | Source and immediate concern |
|---|---|---|---:|---|
| Airport | Africa | 8 / 11 / 1 | 22 | [Airport](https://activematterhelp.ru/wiki/maps/africa_airport) — Track the October 5 relocated stationary exits and Devourer spawns. |
| Headquarters | Africa | 23 / 15 / 1 | 21 | [Headquarters](https://activematterhelp.ru/wiki/maps/africa_headquarters) — Spawn-group-specific permanent exits; October 5 relocation; counts do not mean all players access all 23. |
| Downtown | Abandoned America | 5 / 7 / 1 | 29 | [Downtown](https://activematterhelp.ru/wiki/maps/america_abandoned_city) — October 5 relocation; variant-specific Downtown Collapse and Unstable Zone separate. |
| Dam | Dalniy Island | 6 / 5 / 1 | 21 | [Dam](https://activematterhelp.ru/wiki/maps/dalniy_island_dam) — October 5 water ladder and gravity-zone staircase fixes. |
| Cargo Port | Dalniy Island | 8 / 15 / 1 | 29 | [Cargo Port](https://activematterhelp.ru/wiki/maps/dalniy_island_cargoport) — October 15 barge portal geometry/safe teleport fix. |
| Factory | Dalniy Island | 9 / 12 / 1 | 27 | [Factory](https://activematterhelp.ru/wiki/maps/dalniy_island_factory_adv) — October 15 destructible green fences; Factory Hive/Bloodbath separate. |
| Dogorsk | Dalniy Island | 11 / 6 / 1 | 25 | [Dogorsk](https://activematterhelp.ru/wiki/maps/dalniy_island_dogorsk) — September 18 dynamic extractions, September 30 Escape vehicle delivery points, October 15 extraction scenery fix. |
| Military Base | Dalniy Island | 7 / 10 / 1 | 20 | [Military Base: Silent Witnesses](https://activematterhelp.ru/wiki/maps/dalniy_island_military_base_statues) — Default source is Silent Witnesses, NOT Unstable Zone. Unstable Zone has 40 possible final extraction locations, one selected, and patch changed artifact marker timing. |
| Ozernoe | Dalniy Island | 11 / 7 / 1 | 20 | [Ozernoe](https://activematterhelp.ru/wiki/maps/dalniy_island_ozernoe_adv) — September 30 ladder/gravity platform fixes; October 15 destructible fences. |
| Park | Dalniy Island | 8 / 9 / 1 | 22 | [Park](https://activematterhelp.ru/wiki/maps/dalniy_island_park) — Surface and underground routes require separate levels. September 30 stuck-location fix. |
| Scrapyard | Dalniy Island | 2 / 0 / 1 | 13 | [Scrapyard: Midnight](https://activematterhelp.ru/wiki/maps/dalniy_island_scrapyard) — Midnight raid, fixed 00:00 time; not a generic day/night selectable raid. |
| Shegolskoe | Dalniy Island | 6 / 12 / 1 | 26 | [Shegolskoe](https://activematterhelp.ru/wiki/maps/dalniy_island_shegolskoe_adv) — Overgrowth and Distortion variants must retain their own markers and terrain visibility. |
| Gigastructure | Gigastructure | 1 / 0 / — | 0 | [Gigastructure](https://activematterhelp.ru/wiki/maps/gigastructure) — Standalone multi-level structure; elevator/purge logic; no adequate flat raid coordinates in current guide. |
| Dalniy Island | Dalniy Island | — | 0 | [regional overview](https://activematterhelp.ru/maps?map=dalniy) — Regional overview only, NOT a separately queued raid. Reference wiki lists nine named Dalniy raid-map regions; Headquarters/Airport are Africa, Downtown is Abandoned America and Gigastructure is separate. |

**Meaning of the numbers:** Community wiki listings describe the potential extraction system for one named raid variant. They are *not* simultaneous usable exits and *not* a count of extracted marker coordinates. Headquarter/Dogorsk permanent exits may be spawn-group restricted. For Unstable Zone, final exits are server/zone-dependent. Gigastructure operates differently and should not be mapped as a standard flat raid. Values and conditions may change after a patch; exact positions are not certified.

## Confirmed from actual official developer changelog

- **27 Aug 2026 — major 250 Shades of Liberty:** first-party adds Airport (Africa) and Downtown, Downtown: Unstable Zone, Downtown: Collapse; rare-loot regions gain color-coded icon markers. [Official update](https://activematter.game/en/news/291).
- **18 Sep 2026 — 0.4.0.122:** Dynamic Dogorsk extraction points were introduced. [Official update](https://activematter.game/en/news/324).
- **30 Sep 2026 — 0.4.0.163:** Dalniy Island stationary exit placement and cover changed; Dogorsk escape vehicle delivery points added; Ozernoe ladders/platforms and Park trapping spots fixed. [Official update](https://activematter.game/en/news/341).
- **5 Oct 2026 — 0.4.0.173:** Stationary exits shifted in Airport, HQ and Downtown; Airport Devourer spawns moved away from Investigation points; Dam ladder/gravity stairs fixed. [Official update](https://activematter.game/en/news/349).
- **15 Oct 2026 — 0.4.0.192:** Military Base: Unstable Zone artifact marker timing changed; Dogorsk extraction scenery fixed; Factory/Ozernoe small green fences destructible; Cargo Port barge portals repaired. [Official update](https://activematter.game/en/news/356).
- **16 Oct 2026 — 0.4.0.199:** Current listed patch reviewed for obvious map additions; source notes mostly equipment/lighting/contract tracking. Do **not** infer that earlier map marker issues are automatically resolved. [Official update](https://activematter.game/en/news/361).

## High-risk semantic mismatches uncovered

1. **Headquarters geographic classification:** The indexed HQ and Airport maps are in **Africa**, not Dalniy. Some community English overview prose groups Headquarters with Dalniy in a way that can mislead navigation. Use individual raid-region classification rather than a broad prose list.
2. **Military Base: Unstable Zone versus Silent Witnesses:** The guide's default Military Base wiki page is the **Silent Witnesses** raid (7 / 10 / 1 candidate exits). The Unstable Zone source describes **40 possible final-exit locations, exactly one selected**. Render the latter as potential spawn set, not 40 simultaneous live extraction icons.
3. **Airport total marker mismatch:** The wiki reports 8 permanent + 11 timed + 1 final. The old sample has only **22 total mixed-category records**, not the entirety of the wiki exit catalogue. We cannot infer a location is absent simply because it is not in the 22.
4. **Dalniy regional overview versus raid-specific maps:** Dalniy regional map markers should not be mapped directly into park/dam/etc without a documented regional-to-raid transform.
5. **Gigastructure vertical topology:** The 2D percent-coordinate template and pseudo-isometric building heights cannot represent verified multi-floor routes. Each floor requires an independent plan and height evidence.
6. **Cross-source independence:** [Portal Atlas data import documentation](https://github.com/rileyedward/portal-atlas/blob/main/docs/data-import.md) explicitly describes importing Active Matter Help marker datasets. Agreement between those datasets is replication, **not independent corroboration**.
7. **Licence and source attribution:** Game screenshots and tiled game renders can guide original traced geometry, but public online hosting does not by itself give us carte blanche to rehost third-party annotated tiles, logos or datasets. Keep exact source-rights record before distribution.

## How to turn this into *accurate* map replacements

Use [Airport benchmark](AIRPORT_BENCHMARK.md) first, then Headquarters and Downtown, then the nine local Dalniy raids, then separately the Gigastructure floor system and Dalniy overview. For each map: obtain an authoritative same-build screenshot/rights-cleared source, record zoom/orientation/crop, correlate at least 4 stable FIT landmarks + 2 independent CHECK controls, reconcile named source markers one by one, and preserve mode and patch provenance. The updated [map workbench](../tools/map_reconciliation.html) supports both image calibration and per-marker review. Its [14-map dashboard](../tools/map_fidelity_dashboard.html) now links to all verified URLs for 30 named raid variants.

## Remaining evidence required

- 1:1 source raster extents / tile projection; game-raid crop and orientation per build.
- Player screenshots/current build evidence to validate the marked geography and actual extraction locations.
- Publication rights (or original source image permissions) for rehosting original map baselayers.
- Independent cross-check of geometry (a screenshot of current in-game map is more useful than an additional site that copied the same data).
- Measured heights, multi-level accessibility and indoor geometry separately from flat top-down positions.

**Release truth:** technical source correlation complete for the 30 listed variant links; *geographic reconciliation and 275 legacy marker validation are not complete*.
