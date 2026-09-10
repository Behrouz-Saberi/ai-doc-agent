# DESIGN.md Collection

A library of ready-to-use `DESIGN.md` design-system documents extracted from 74
real brands, vendored from [voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
(MIT, © 2026 VoltAgent — see `LICENSE`).

These follow Google Stitch's `DESIGN.md` specification and pair with the Stitch
skills in `.claude/skills/`: skills like `taste-design`, `extract-design-md`, and
`design-md` **produce** `DESIGN.md` files, while this folder is a catalog of
existing ones to reference.

## Usage

Copy a brand's `DESIGN.md` into your project (or point your AI agent at it) and
prompt "build me a page that looks like this" to generate UI consistent with that
brand's design language.

## Layout

- `<brand>/DESIGN.md` — the design system document
- `<brand>/README.md` — upstream notes for that brand
- `CATALOG.md` — upstream index of all brands (original repo README)
- `LICENSE` — upstream MIT license

To update, re-copy from upstream.
