from odoo import fields, models


class ProjectProject(models.Model):
    _inherit = "project.project"

    bucket_id = fields.Many2one("qsteps.project.bucket", string="Project Bucket")
