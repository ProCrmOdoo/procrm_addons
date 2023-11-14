from odoo import models, fields


class HrTimesheetTypeCost(models.Model):
    _name = "hr.timesheet.type.cost"
    _description = "Timesheet Type Cost"

    employee_id = fields.Many2one("hr.employee", string="Employee")
    company_id = fields.Many2one("res.company", related="employee_id.company_id")
    project_id = fields.Many2one("project.project", string="Project")
    timesheet_type_id = fields.Many2one("project.time.type", string="Timesheet Type")

    timesheet_cost = fields.Monetary(
        "Timesheet Cost",
        currency_field="currency_id",
        default=0.0,
    )
    currency_id = fields.Many2one(
        "res.currency", related="company_id.currency_id", readonly=True
    )
