from odoo import fields, models


class ClientType(models.Model):
    _name = 'client.type'

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
