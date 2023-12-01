from odoo import fields, models


class Partner(models.Model):
    _name = 'partner'

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
