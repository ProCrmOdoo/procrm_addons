from odoo import fields, models


class BonusForRecom(models.Model):
    _name = 'bonus.for.recom'

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
