from odoo import fields, models


class DocumentPage(models.Model):
    _inherit = "document.page"

    lead_id = fields.Many2one(comodel_name="crm.lead", inverse_name="document_page_ids")
