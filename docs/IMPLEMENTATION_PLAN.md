# Implementation Plan - Phase 1 Foundation

## What Phase 1 implemented
- Extended `project.task` with accreditation-support fields:
  - `evidence_type`
  - `evidence_attachment_ids`
  - `challenge_type`
  - `accreditation_status`
  - `evidence_evaluation_status`
- Created a new `qsteps.project.bucket` model as the Major Project / Bucket foundation.
- Extended `project.project` with `bucket_id` linking each project to a bucket.
- Added backend inherited views for:
  - task form/list accreditation fields
  - project form/list/search bucket field
- Added base bucket views (tree, form, search), action, and menu entry.
- Added simple ACLs for bucket:
  - project users: read only
  - project managers: full CRUD

## What was intentionally not implemented yet
- Leadership Dashboard
- Printable progress reports
- Complex portal redesign
- Reminder logic and evaluator role design

## Files changed
- `custom_addons/qsteps_accreditation_project/__manifest__.py`
- `custom_addons/qsteps_accreditation_project/models/__init__.py`
- `custom_addons/qsteps_accreditation_project/models/project_task.py`
- `custom_addons/qsteps_accreditation_project/models/project_project.py`
- `custom_addons/qsteps_accreditation_project/models/project_bucket.py`
- `custom_addons/qsteps_accreditation_project/security/ir.model.access.csv`
- `custom_addons/qsteps_accreditation_project/views/project_task_views.xml`
- `custom_addons/qsteps_accreditation_project/views/project_project_views.xml`
- `custom_addons/qsteps_accreditation_project/views/project_bucket_views.xml`

## Data model shape
- Customer (`res.partner`)
  -> Project Bucket / Major Project (`qsteps.project.bucket`)
  -> Odoo Project (`project.project` via `bucket_id`)
  -> Tasks (`project.task`) with accreditation evidence and status fields

## Responsible Department note
- `responsible_department_id` was **not** added in Phase 1 to avoid forcing `hr` dependency.
- A TODO note was left in `project.task` extension to add it once dependency decision is approved.

## Future phases
- Portal improvements
- Leadership Dashboard
- Printable progress report
- Evaluator user type and permissions
- Reminder logic
