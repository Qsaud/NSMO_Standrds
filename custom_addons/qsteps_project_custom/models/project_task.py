from odoo import fields, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    evidence_type = fields.Selection(
        selection=[
            ("policy", "Policy"),
            ("procedure", "Procedure"),
            ("report", "Report"),
            ("meeting_minutes", "Meeting Minutes"),
            ("training_record", "Training Record"),
            ("audit_result", "Audit Result"),
            ("photo", "Photo"),
            ("other", "Other"),
        ],
        string="Evidence Type",
    )
    evidence_attachment_ids = fields.Many2many(
        comodel_name="ir.attachment",
        relation="project_task_evidence_attachment_rel",
        column1="task_id",
        column2="attachment_id",
        string="Evidence Attachments",
        help="Supporting evidence files linked to this task.",
    )
    challenge_type = fields.Selection(
        selection=[
            ("missing_evidence", "Missing Evidence"),
            ("incomplete_evidence", "Incomplete Evidence"),
            ("wrong_approval", "Wrong Approval"),
            ("wrong_dates", "Wrong Dates"),
            ("unclear_responsibility", "Unclear Responsibility"),
            ("access_issue", "Access Issue"),
            ("other", "Other"),
        ],
        string="Challenge Type",
    )
    accreditation_status = fields.Selection(
        selection=[
            ("not_met", "Not Met"),
            ("partially_met", "Partially Met"),
            ("fully_met", "Fully Met"),
        ],
        string="Accreditation Status",
        default="not_met",
    )
    evidence_evaluation_status = fields.Selection(
        selection=[
            ("accepted", "Accepted"),
            ("content_needs_improvement", "Content Needs Improvement"),
            ("wrong_approval", "Wrong Approval"),
            ("wrong_dates", "Wrong Dates"),
        ],
        string="Evidence Evaluation Status",
    )

    # TODO: Add responsible_department_id (Many2one to hr.department)
    # once/if the module should depend on `hr`.
