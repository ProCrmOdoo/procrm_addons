from odoo import fields, models


class PortalAddress(models.Model):
    _name = "portal.address"

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
