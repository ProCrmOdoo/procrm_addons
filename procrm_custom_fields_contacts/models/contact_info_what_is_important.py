from odoo import fields, models


class WhatIsImportant(models.Model):
    _name = "what.is.important"

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
