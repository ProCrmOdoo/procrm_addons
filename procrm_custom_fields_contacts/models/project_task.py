from odoo import fields, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    creator_id = fields.Many2one(
        comodel_name="res.users", string="Creator"
    )
