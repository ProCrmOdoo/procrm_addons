from odoo import fields, models


class WhatIsYourCms(models.Model):
    _name = "what.is.your.cms"

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
