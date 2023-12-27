from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    deal_type = fields.Many2one(comodel_name="deal.type", string="Deal type")
    comment_to_payment = fields.Char(string="Comment to payment")
    payment_method = fields.Many2one(
        comodel_name="payment.method", string="Payment method"
    )
    form_of_payment = fields.Many2one(
        comodel_name="form.payment", string="Form of payment"
    )
    client_bonus = fields.Char(string="Client bonus", help="'-' if not available")
