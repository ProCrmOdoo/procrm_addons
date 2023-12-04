from odoo import fields, models


class PaymentMethod(models.Model):
    _name = 'payment.method'

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
