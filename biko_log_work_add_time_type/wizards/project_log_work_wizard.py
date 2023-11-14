from odoo import api, fields, models


class ProjectTaskLogWork(models.TransientModel):
    _inherit = "project.task.log.work"

    project_time_type = fields.Many2one("project.time.type", string="Time Type")

    def action_log_work_apply(self):
        tasks = self.env["project.task"].browse(self.env.context.get("active_ids"))
        for task in tasks:
            if self.description:
                task.message_post(body=self.description)
            vals_list = {
                "name": self.comment if self.comment else " / ",
                "date": self.date,
                "unit_amount": self.log_time,
                "task_id": task.id,
                "project_id": task.project_id.id,
                "user_id": self.user_id.id,
                "employee_id": self.employee_id.id,
                "time_type_id": self.project_time_type.id,
            }
            self.env["account.analytic.line"].create(vals_list)
