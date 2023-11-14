# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) Sitaram Solutions (<https://sitaramsolutions.in/>).
#
#    For Module Support : info@sitaramsolutions.in  or Skype : contact.hiren1188
#
##############################################################################

from odoo import api, models
from odoo.osv import expression


class srHrEmployee(models.Model):
    _inherit = "hr.employee"

    @api.model
    def _name_search(
        self, name, args=None, operator="ilike", limit=100, name_get_uid=None
    ):
        if self._context.get("search_not_own_doc_user"):
            res_users = self.env["res.users"].search([])
            user_ids = res_users.filtered(
                lambda user: user.has_group("sales_team.group_sale_salesman_all_leads")
                and user.has_group("sales_team.group_sale_manager")
            )
            domain = [("id", "in", user_ids.mapped("employee_id").ids)]
        return self._search(
            expression.OR([domain, args]), limit=limit, access_rights_uid=name_get_uid
        )
