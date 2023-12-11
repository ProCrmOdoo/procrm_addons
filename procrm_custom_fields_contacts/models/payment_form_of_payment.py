from odoo import fields, models


class FormPayment(models.Model):
    _name = "form.payment"

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
