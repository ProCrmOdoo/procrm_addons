from odoo import fields, models


class ProjectProject(models.Model):
    _inherit = "project.project"

    sales_manager_id = fields.Many2one(comodel_name="res.users", string="Sales manager")
    test = fields.Char()
