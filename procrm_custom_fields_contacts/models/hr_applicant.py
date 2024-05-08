from odoo import fields, models


class HrApplicant(models.Model):
    _inherit = "hr.applicant"

    position = fields.Many2one(comodel_name="hr.position", string="Position")
    experience = fields.Text(string="Experience")
    recommendation = fields.Text(string="Recommendation")
    candidate_questionnaire = fields.Text(string="Candidate questionnaire")
    interview_file = fields.Text(string="Interview file")
