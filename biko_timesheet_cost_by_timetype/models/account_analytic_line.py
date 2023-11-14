# -*- coding: utf-8 -*-
from odoo import models, fields, api


class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    def _timesheet_postprocess_values(self, values):
        result = {id_: {} for id_ in self.ids}
        sudo_self = self.sudo()
        if any(
            field_name in values
            for field_name in ["unit_amount", "employee_id", "account_id"]
        ):
            for timesheet in sudo_self:
                cost = (
                    timesheet.employee_id.get_timesheet_cost(
                        timesheet.employee_id,
                        timesheet.project_id,
                        timesheet.time_type_id,
                    )
                    or 0.0
                )
                amount = -timesheet.unit_amount * cost
                amount_converted = timesheet.employee_id.currency_id._convert(
                    amount,
                    timesheet.account_id.currency_id or timesheet.currency_id,
                    self.env.company,
                    timesheet.date,
                )
                result[timesheet.id].update(
                    {
                        "amount": amount_converted,
                    }
                )
        return result
