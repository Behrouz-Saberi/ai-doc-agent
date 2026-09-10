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

---

# Emil Kowalski — Design & Animation Skills

Animation and design-engineering skills, vendored from
[emilkowalski/skills](https://github.com/emilkowalski/skills) (MIT, see
`LICENSE-emilkowalski-skills`). Directory names match each skill's `name`.

- **Core** — `emil-design-eng`, `apple-design`, `pick-ui-library`, `prototype`
- **Animation** — `animate`, `animate-expo`, `review-animations`,
  `improve-animations`, `find-animation-opportunities`, `animation-vocabulary`
- **Libraries / native** — `ask-sonner`, `write-swift`

Self-contained; no MCP server required.

---

# Impeccable (full install — with hooks)

Design-fluency skill from [pbakaus/impeccable](https://github.com/pbakaus/impeccable)
(Apache-2.0; see `impeccable/LICENSE` and `impeccable/NOTICE.md`). Installed as a
**full install**, which is more than a plain skill:

- `.claude/skills/impeccable/` — the skill (SKILL.md, 20+ command references,
  scripts). `/impeccable <command>` (init, craft, audit, polish, critique, …).
- `.claude/agents/impeccable-*.md` — 4 sub-agents (asset-producer, documenter,
  finish-reviewer, manual-edit-applier).
- `.claude/settings.json` — **hooks** that run the impeccable detector engine:
  a `PostToolUse` pass after `Edit`/`Write` on UI files, and a full-rule deep
  pass on `Stop`.

**Binary:** the hooks and commands run a native Rust engine (`ENGINE_VERSION`
0.1.5) via the `scripts/impeccable` launcher. That binary is **not** vendored —
the launcher fetches it into `scripts/bin/<os>-<arch>/` (or `~/.impeccable/`) on
first use, or run `npx impeccable install` to fetch it ahead of time. Until the
binary is present each hook no-ops, so nothing breaks if it can't be fetched.

> The hooks execute this fetched binary automatically on every edit and on stop.
> This was an explicit choice; remove the `hooks` block from
> `.claude/settings.json` to disable that and keep the skill/commands only.
