# AGENTS.md

## Project Overview
This repository is for **Odoo 18 Community** `project` module customization to support **accreditation preparation projects**. The upstream Odoo code is kept as a read-only reference, while all business-specific behavior is implemented in a dedicated custom addon.

## Repository Structure
- `vendor/odoo18/addons/project`  
  Reference-only copy of the upstream Odoo 18 Community `project` module. Use it to understand original behavior.
- `custom_addons/qsteps_project_custom`  
  Active customization addon where all project-specific changes must be implemented.
- `docs`  
  Team and Codex guidance, workflows, and review checklists.
- `THIRD_PARTY_LICENSES` (if present)  
  Third-party license texts. Keep these files intact.

## Very Important Rules
- Never edit files inside `vendor/odoo18/addons/project` unless explicitly requested.
- Treat `vendor/odoo18/addons/project` as read-only upstream reference.
- All custom Odoo changes must be implemented in `custom_addons/qsteps_project_custom`.
- Use Odoo inheritance instead of copying or replacing original Odoo files.
- Do not use Odoo Enterprise code.
- Do not remove license files.
- Do not rename Odoo core models.
- Do not create a custom module named `project` because it may conflict with Odoo's original project module.
- Keep changes simple and technically easy to maintain.

## Odoo Development Rules
- Python models should inherit from Odoo models using `_inherit`.
- XML views should extend existing views using `inherit_id` and `xpath`.
- Security changes should be added in the custom addon.
- Access rights should be explicit and minimal.
- Portal changes should be done carefully because portal templates are sensitive.
- Avoid hardcoding IDs when XML external IDs are available.
- Keep fields and views upgrade-friendly.

## Custom Addon Rules
- Main customization module path: `custom_addons/qsteps_project_custom`
- The module must depend on `project`.
- Add new fields in `models/`.
- Add inherited backend views in `views/`.
- Add portal templates in `views/` or portal-specific XML files.
- Add reports under `report/` when needed.
- Add access rules under `security/`.

## Planned Feature Map
| Feature | Likely model | Likely files to modify | Notes |
|---|---|---|---|
| Evidence Type | `project.task` | `models/project_task.py`, `views/project_task_views.xml` | Usually `selection`/`many2one` field plus form/tree visibility. |
| Evidence Attachment | `project.task` + `ir.attachment` links | `models/project_task.py`, `views/project_task_views.xml`, `security/ir.model.access.csv` (if new model) | Prefer Odoo-native attachment mechanisms and permissions. |
| Challenge Type | `project.task` | `models/project_task.py`, `views/project_task_views.xml` | Keep values maintainable and clearly labeled for users. |
| Project Buckets / Major Projects | `project.project` (and possibly helper model) | `models/`, `views/`, `security/` | Implement hierarchy via inheritance, not by replacing core models. |
| Leadership Dashboard | Likely aggregated from `project.task` / `project.project` | `views/`, optional `models/`, optional `controllers/` | Start with lightweight KPIs and safe access control. |
| Portal Improvements | Portal task views/templates | `views/` (portal XML), optional `controllers/` | Portal templates are sensitive; test carefully. |
| Printable Progress Report | Task/project report models | `report/`, `views/`, manifest data list | Prefer QWeb reports with clear grouping and status metrics. |

## Testing and Validation
- Validate Python syntax.
- Validate XML structure.
- Check manifest data file order.
- Check that custom addon imports are correct.
- Do not assume Odoo is running locally unless confirmed.
- If Odoo is not available, do static checks only.

## Git Rules
- Use small focused changes.
- Show `git status` before and after changes.
- Do not commit unless explicitly asked.
- Do not include secrets, passwords, database credentials, or server IPs.

## Communication Style
- Explain changes in simple business language first.
- Then provide technical details.
- Mention risks clearly.
- Prefer maintainable Odoo-native solutions.
