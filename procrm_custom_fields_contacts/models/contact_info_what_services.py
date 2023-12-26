from odoo import fields, models


class WhatServices(models.Model):
    _name = "what.services"

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
