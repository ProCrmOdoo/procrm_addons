from odoo import fields, models


class LicenseBuy(models.Model):
    _name = "license.buy"

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
