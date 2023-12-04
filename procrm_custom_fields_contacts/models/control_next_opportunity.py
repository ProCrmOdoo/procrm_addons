from odoo import fields, models


class NextOpportunity(models.Model):
    _name = 'next.opportunity'

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
