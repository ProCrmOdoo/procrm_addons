from odoo import fields, models


class ReceiveLeads(models.Model):
    _name = 'receive.leads'

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
