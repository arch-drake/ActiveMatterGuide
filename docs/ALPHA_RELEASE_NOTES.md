# Source Atlas v2.2.0-alpha.1

**Unofficial community-testing alpha.** This is not an official game map or a certified release.

**Publication reality (October 20):** A standalone [maps-only alpha ZIP](https://github.com/arch-drake/ActiveMatterGuide/blob/alpha/v2.2.0-alpha.1/downloads/ActiveMatter-SourceAtlas-v2.2.0-alpha.1-MAPS-ONLY.zip) is available directly in the public alpha branch and the [full alpha branch source archive](https://github.com/arch-drake/ActiveMatterGuide/archive/refs/heads/alpha/v2.2.0-alpha.1.zip) is available. The separate GitHub Actions **formal prerelease** attempt failed before any runner steps; the [GitHub Releases listing](https://github.com/arch-drake/ActiveMatterGuide/releases) still has no published release. This note doubles as the planned formal release notes once runner access is restored. The maps-only ZIP intentionally omits the 2.1.1 companion and includes a link to obtain it separately.

## Included
- 13 real-source community-hosted overhead raster *reference windows*: Airport, Headquarters, Downtown, Dam, Cargo Port, Factory, Dogorsk, Military Base, Ozernoe, Park, Scrapyard, Shegolskoe, Dalniy Island regional overview.
- Gigastructure under **Special / In progress**, using your own floor screenshot; no fictional finished flat map.
- Dedicated online-opt-in Source Atlas; screenshot evidence viewer; image alignment workbench; source status board.
- Existing 2.1.1 offline PvE/PvP guide, monsters, investigations, music and legacy illustrated map pages. Its old map pins have NOT been certified or rebuilt.
- An offline landing page (index.html) and ALPHA_START_HERE.txt in the ZIP.

## Install/test
1. Download ActiveMatter-SourceAtlas-v2.2.0-alpha.1.zip from this release's Assets and extract EVERYTHING.
2. Open index.html in Chrome or Edge and choose **Explore Source Atlas**.
3. Select a geographic reference and click **Load overhead map** to opt into online community raster requests.
4. Choose Gigastructure for local floor images only; use floor labels to prevent confusion.
5. Export your backup before opening or replacing a previous standalone offline companion.

## Critical limitations
- Tile windows are NOT certified raid boundaries or game-exact geography. No third-party map tiles are redistributed in the package; their source host and permissions remain external.
- The primary atlas displays NO unreconciled markers. All 275 legacy coordinate candidates are research leads only.
- Extraction points, timed exits, anomalies, moving events, Unstable Zone mechanics and spawn groups are patch/variant sensitive.
- Gigastructure has no verified flat map, and real building heights remain unknown.
- The 2.1.1 companion STILL contains older illustrative map backgrounds and provisional marker positions.
- Live tile delivery, Pages hosting, Windows file:// behavior, and every game mode have not received full acceptance testing. This is precisely why the package is an alpha.

## Feedback
Use the [map correction issue form](https://github.com/arch-drake/ActiveMatterGuide/issues/new/choose). Include exact game build, raid variant and permissioned evidence. Never upload private saves.

## Verify integrity
A matching SHA-256 file is attached. On Windows use Get-FileHash; on macOS/Linux run sha256sum -c against the .sha256 file.
