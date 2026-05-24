# Codex Change Review Checklist

Use this checklist before approving any Codex-generated change.

## Scope and Safety
- [ ] Vendor files were not modified (`vendor/odoo18/**` unchanged).
- [ ] No Odoo Enterprise code is used.
- [ ] No secrets, passwords, credentials, or server IPs are committed.

## Odoo Architecture
- [ ] Feature is implemented using Odoo inheritance (`_inherit`, `inherit_id`, `xpath`).
- [ ] Change stays simple and maintainable.
- [ ] Original `project` module is not duplicated or replaced.

## Module Integrity
- [ ] Custom addon manifest is valid and depends on `project` as needed.
- [ ] Manifest data file ordering is correct.
- [ ] Python imports are valid.
- [ ] XML files are structurally valid.

## Security
- [ ] Security files are updated if new models are added.
- [ ] Access rights are explicit and minimal.
- [ ] Portal-facing changes were reviewed carefully.
