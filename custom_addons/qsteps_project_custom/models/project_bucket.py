from odoo import fields, models


class QstepsProjectBucket(models.Model):
    _name = "qsteps.project.bucket"
    _description = "Project Bucket"
    _order = "name"

    name = fields.Char(required=True)
    partner_id = fields.Many2one("res.partner", string="Customer")
    project_ids = fields.One2many("project.project", "bucket_id", string="Projects")
    description = fields.Text()
    active = fields.Boolean(default=True)
    company_id = fields.Many2one(
        "res.company", default=lambda self: self.env.company, required=True
    )
    user_id = fields.Many2one("res.users", string="Responsible")
    state = fields.Selection(
        [("draft", "Draft"), ("active", "Active"), ("closed", "Closed")],
        default="draft",
        required=True,
    )
