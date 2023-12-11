from odoo import fields, models


class UseInWork(models.Model):
    _name = "use.in.work"

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
