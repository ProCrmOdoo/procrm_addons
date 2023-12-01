from odoo import fields, models


class CooperTerm(models.Model):
    _name = 'cooper.term'

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
