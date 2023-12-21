from odoo import fields, models


class WhatDepartments(models.Model):
    _name = "what.departments"

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
