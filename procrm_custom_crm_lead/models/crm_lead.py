from odoo import fields, models


class CrmLead(models.Model):
    _inherit = "crm.lead"

    document_page_ids = fields.One2many(
        string="Wiki", comodel_name="document.page", inverse_name="lead_id"
    )

    knowledge = fields.Integer(
        string="Knowledge", compute="_compute_document_page_count"
    )

    def _compute_document_page_count(self):
        for rec in self:
            rec.knowledge = len(rec.document_page_ids)

    def action_knowledge_count(self):
        return {
            "type": "ir.actions.act_window",
            "name": "Knowledge",
            "res_model": "document.page",
            "context": {
                "default_lead_id": self.id,
            },
            "domain": [("lead_id", "=", self.id)],
            "view_mode": "tree,form",
            "target": "current",
        }
