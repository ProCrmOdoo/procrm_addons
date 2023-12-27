from odoo import fields, models


class LicenseNow(models.Model):
    _name = "license.now"

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
