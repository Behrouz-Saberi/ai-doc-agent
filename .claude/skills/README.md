# Stitch Skills

Agent skills for [Google Stitch](https://stitch.withgoogle.com), vendored from
[google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills)
(Apache-2.0) so they load as project skills without depending on plugin-marketplace resolution.

Skill `name` fields were normalized to plain kebab-case slugs (matching each
directory) so Claude Code loads them as project skills; upstream ships them as
`stitch::<name>` plugin skills.

## Groups

- **Design** — `code-to-design`, `generate-design`, `manage-design-system`,
  `extract-design-md`, `extract-static-html`, `upload-to-stitch`
- **Build** — `react-components`, `react-native`, `react-vite-dashboard`,
  `remotion`, `shadcn-ui`
- **Utilities** — `design-md`, `site-md`, `enhance-prompt`, `stitch-loop`, `taste-design`

## Note

The design/build skills call a **Stitch MCP server** (`stitch*:*` tools). Those
skills need that MCP server configured to be fully functional; the utility
skills (e.g. `enhance-prompt`, `taste-design`, `design-md`) work standalone.

To update, re-copy from upstream and re-normalize the `name:` frontmatter.

---

# Taste Skills

Frontend design-taste and image-generation skills, vendored from
[leonxlnx/taste-skill](https://github.com/leonxlnx/taste-skill) (MIT, see
`LICENSE-taste-skill`). Each skill directory is named after the skill's own
`name` frontmatter (its canonical identity), which is why some directories differ
from the upstream folder names.

## Groups

- **Design taste** — `design-taste-frontend`, `design-taste-frontend-v1`,
  `high-end-visual-design`, `minimalist-ui`, `industrial-brutalist-ui`,
  `redesign-existing-projects`, `gpt-taste`, `stitch-design-taste`
- **Image generation** — `imagegen-frontend-web`, `imagegen-frontend-mobile`,
  `brandkit`, `image-to-code`
- **Output control** — `full-output-enforcement`

Most carry adjustable design dials (1–10) — `DESIGN_VARIANCE`, `MOTION_INTENSITY`,
`VISUAL_DENSITY`. These skills are self-contained and need no MCP server.
