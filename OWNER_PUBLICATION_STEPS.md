# Owner publication steps — verified October 20, 2026

Repository: https://github.com/arch-drake/ActiveMatterGuide

**Audit findings:** The root standalone HTML, existing 2.1.1 ZIP, docs and atlas files are already committed. **Do not upload duplicate old copies.** At audit time GitHub Pages is disabled and GitHub Releases has no published entries. Repository HTML links on GitHub are source previews; they are not web-app launches.

## Make the maps playable as a website

1. Visit [Settings → Pages](https://github.com/arch-drake/ActiveMatterGuide/settings/pages) while signed in as repository owner.
2. Choose **Deploy from a branch**, branch **main**, folder **/(root)** and **Save**.
3. After GitHub confirms publication, visit https://arch-drake.github.io/ActiveMatterGuide/ and test **Explore Source Atlas**, a reference area, local upload, external opt-in tiles, mobile viewport and download button.
4. If Pages is not yet enabled, the [repository archive](https://github.com/arch-drake/ActiveMatterGuide/archive/refs/heads/main.zip) already allows local use: extract and open index.html. Never ask players to click a GitHub HTML file-view link expecting it to execute as a page.

## Alpha prerelease

The proposed tag is **v2.2.0-alpha.1**. The branch **alpha/v2.2.0-alpha.1** is the candidate source; see [alpha notes](docs/ALPHA_RELEASE_NOTES.md). A dedicated workflow, .github/workflows/publish-alpha.yml, builds an extractable alpha ZIP and uses GitHub Actions to create a prerelease if the runner and token permissions allow. **A source branch is not proof a GitHub Release has been published.** Confirm an actual entry and attached ZIP under [Releases](https://github.com/arch-drake/ActiveMatterGuide/releases) before announcing formal publication.

If Actions cannot run, go to [Draft a release](https://github.com/arch-drake/ActiveMatterGuide/releases/new) as the owner, choose tag v2.2.0-alpha.1 from the alpha branch, set **This is a pre-release**, and attach the locally built dist ZIP and .sha256 produced by running python3 source/build_alpha_release.py in a checked-out repository. Do not claim release success until it exists.

Map notes: 13 source raster references, Dalniy regional overview, Gigastructure special floor mode; no verified legacy pins or surveyed heights. The separate offline 2.1.1 guide still includes old illustrated maps. The project's general license remains unselected; do not assume external community tile redistribution rights.
