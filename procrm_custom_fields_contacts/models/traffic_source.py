from odoo import fields, models


class TrafficSource(models.Model):
    _name = 'traffic.source'

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
