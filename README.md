# NSMO Standards Odoo 18 Project Reference and Customization Layout

- `vendor/odoo18/addons/project` is intended to hold the untouched original Odoo 18 Community `project` module as a reference copy.
- `custom_addons/qsteps_project_custom` is the dedicated addon for all future development and customizations.
- The customization addon depends on Odoo's `project` module.
- Do not edit the vendor reference copy directly.

## AI / Codex Instructions

This repository uses AGENTS.md files to guide Codex.
Main rules:
- Do not edit vendor Odoo reference files.
- Implement all customizations in custom_addons/qsteps_project_custom.
- See docs/CODEX_WORKFLOW.md and docs/CODE_REVIEW.md.
