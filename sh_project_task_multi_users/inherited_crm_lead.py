# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) Sitaram Solutions (<https://sitaramsolutions.in/>).
#
#    For Module Support : info@sitaramsolutions.in  or Skype : contact.hiren1188
#
##############################################################################

from odoo import fields, api, models


class srCrmTeam(models.Model):
    _inherit = "crm.team"

    member_ids = fields.Many2many(
        "res.users",
        string="Channel Members",
        check_company=True,
        domain=[("share", "=", False)],
        help=(
            "Add members to automatically assign their documents to this sales team."
            " You can only be member of one team."
        ),
    )


class srLead(models.Model):
    _inherit = "crm.lead"

    is_current_user = fields.Boolean(
        string="Current User", compute="_compute_current_user"
    )
    invite_user_ids = fields.Many2many("res.users", string="Invite Users")
    branch_id = fields.Many2one(
        "sr.branch", related="partner_id.user_id.branch_id", string="Branch"
    )
    team_id = fields.Many2one(default=False)

    def _compute_current_user(self):
        for crm in self:
            if crm.user_id.id == self.env.user.id:
                crm.is_current_user = False
            else:
                crm.is_current_user = True

    @api.model
    def get_employee(self, employees, emp_list):
        if employees:
            emp_id = self.env["hr.employee"].search(
                [("parent_id", "=", employees[-1].id)]
            )
            if emp_id and len(emp_id.ids) == 1 and emp_id.ids not in emp_list:
                emp_list.append(emp_id.id)
                employees += emp_id
                self.get_employee(employees, emp_list)
            if emp_id and len(emp_id.ids) > 1 and emp_id.ids not in emp_list:
                emp_list.extend(emp_id.ids)
                employees += emp_id
                self.get_employee(employees, emp_list)
            return employees

    @api.model
    def search_read(self, domain=None, fields=None, offset=0, limit=None, order=None):
        employees = self.env["hr.employee"].search(
            [("user_id", "=", self.env.user.id)], limit=1
        )
        leads = self.sudo().search([("user_id", "=", self.env.user.id)])
        leads |= self.sudo().search([("invite_user_ids", "in", self.env.user.ids)])
        emp_list = []
        emp_domain = []
        if employees:
            employees = self.get_employee(employees=employees, emp_list=emp_list)
            employees |= self.env["hr.employee"].browse(emp_list)
            leads |= self.sudo().search(
                [
                    ("user_id", "in", employees.mapped("user_id").ids),
                    # ("type", "!=", "opportunity"),
                    ("team_id", "=", False),
                ]
            )
        leads |= self.sudo().search(
            [
                '|',
                ("team_id.user_id", "=", self.env.user.id),
                ("team_id.member_ids", "in", self.env.user.ids),
            ]
        )
        emp_domain += [('id', 'in', leads.ids)]
        emp_domain += domain
        return super(srLead, self).search_read(
            domain=emp_domain, fields=fields, offset=offset, limit=limit, order=order
        )
