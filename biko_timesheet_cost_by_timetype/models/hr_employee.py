from odoo import _, api, fields, models


class HrEmployeePrivate(models.Model):
    _inherit = "hr.employee"

    timesheet_table_ids = fields.One2many(
        "hr.timesheet.type.cost",
        "employee_id",
        groups="hr.group_hr_user",
        string="Timesheet Table",
    )

    def get_timesheet_cost(self, employee, project, timesheet_type):

        if not employee:
            return 0.0

        sql = f"""
            select timesheet_cost from hr_timesheet_type_cost
            where employee_id={employee.id}
            and (project_id{"=" + str(project.id) if project else " is NULL"} or project_id is NULL)
            AND (timesheet_type_id{"=" + str(timesheet_type.id) if timesheet_type else " is NULL"} or timesheet_type_id IS NULL)
            ORDER BY project_id DESC NULLS LAST, timesheet_type_id DESC NULLS LAST
            LIMIT 1
        """

        result = self.env.cr.execute(sql)
        cost_rec = self.env.cr.dictfetchall()

        return (
            cost_rec[0]["timesheet_cost"]
            if cost_rec
            else (employee.timesheet_cost or 0.0)
        )
