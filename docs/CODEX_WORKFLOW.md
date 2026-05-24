# Codex Workflow for Odoo 18 Project Customization

## 1) Inspect upstream behavior safely
1. Read files under `vendor/odoo18/addons/project` to understand baseline models, views, and flows.
2. Treat vendor files as read-only references.
3. Capture the upstream model/view external IDs before editing custom XML.

## 2) Decide where to implement changes
1. Route all functional changes to `custom_addons/qsteps_accreditation_project`.
2. Pick target files by change type:
   - Model field/logic: `models/`
   - Backend/portal view changes: `views/`
   - Access/security: `security/`
   - Printable outputs: `report/`
   - HTTP endpoints only if required: `controllers/`

## 3) Add a new field safely
1. Extend the target model with `_inherit`.
2. Add only the needed field attributes (label, help, tracking, required) with upgrade safety in mind.
3. If new business objects are introduced, add explicit minimal access rules.
4. Ensure manifest includes any new data files in correct load order.

## 4) Extend an XML view safely
1. Use inherited views with `inherit_id` and targeted `xpath`.
2. Avoid replacing whole upstream views unless absolutely necessary.
3. Prefer robust xpath anchors that are less likely to break during upgrades.
4. Keep portal template updates minimal and carefully scoped.

## 5) Avoid vendor edits
- Never modify `vendor/odoo18/**` files for normal feature work.
- If behavior differs from upstream, implement overrides in the custom addon.

## 6) Summarize after each task
1. Business summary first (what user-facing outcome changed).
2. Technical summary second (files, models, views, security).
3. Risks/assumptions last (especially portal/security impacts).

## 7) Prepare changes for review
1. Run static checks available in the environment (Python/XML/import sanity).
2. Confirm no vendor files were changed.
3. Verify manifest dependencies and data order are correct.
4. Include a clear file-by-file change list.
