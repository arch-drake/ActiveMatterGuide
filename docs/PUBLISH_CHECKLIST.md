# Publish the 2.1 release — remaining steps

The repository text files and temporary landing page can be pushed through the current GitHub connection, but the large binary ZIP and bundled self-contained HTML must be added using a file-capable Git client or GitHub website.

## Required release files

1. Upload **`active_matter_solo_pve_field_guide.html`** to the repository root (7.8 MB).
2. Upload **`Active_Matter_Field_Operations_2_1_Community_Edition.zip`** to `downloads/` (9.7 MB).
3. Upload remaining prepared folders from the locally available **Active_Matter_Field_Operations_GitHub_Ready.zip**: `assets/`, `source/`, `previews/`, `docs/`, `README_START_HERE.md`, and `manifest.json`. Do not overwrite README.md/index.html without checking whether the release links stay correct.
4. In **Settings → Pages**, select **Deploy from a branch**, branch **main**, folder **/(root)**; save.
5. Check that both launch/download buttons become active at https://arch-drake.github.io/ActiveMatterGuide/ .
6. In **Releases → Draft a new release**, tag `v2.1.0`, attach the release ZIP and publish. Releasing is optional; the repository download already works once the ZIP is committed.

**Before public announcement:** manually check an actual downloaded ZIP, a fresh browser open, all map controls, PvE/PvP progress isolation and backup export/import. The isometric viewer is a 2D projection, not an authentic heightmap. Respect the rights/provenance notes.

## Quick upload option

Use [GitHub's file uploader](https://github.com/arch-drake/ActiveMatterGuide/upload/main), drag the prepared files and folder contents into the upload area, then **Commit changes**. If directory upload is awkward, clone the repo using GitHub Desktop, copy the ZIP contents into the clone, and push one commit. A GitHub release cannot be marked complete while required files are missing.
