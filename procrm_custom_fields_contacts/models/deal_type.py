from odoo import fields, models


class DealType(models.Model):
    _name = "deal.type"

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
