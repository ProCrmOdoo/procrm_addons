# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import models, fields, api


class ProjectTask(models.Model):
    _inherit = 'project.task'

    @api.model
    def default_multi_user(self):
        return self.env.user.ids
        

    sh_user_ids = fields.Many2many('res.users', 'rel_user_task','task_id',string='Assigned to multi users',default=default_multi_user)
    sh_multi_user = fields.Boolean('Display multi users in task ?', related='company_id.sh_multi_user')
    
    @api.onchange('sh_user_ids')
    def onchange_your_field(self):
        self.partner_id.message_subscribe(self.env.user.ids)
            