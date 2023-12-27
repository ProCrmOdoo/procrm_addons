from odoo import fields, models


class Motives(models.Model):
    _name = "motives"

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
