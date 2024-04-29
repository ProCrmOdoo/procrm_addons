from odoo import fields, models


class HrPosition(models.Model):
    _name = "hr.position"

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
