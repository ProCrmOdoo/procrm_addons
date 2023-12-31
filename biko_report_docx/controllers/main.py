# Copyright (C) 2017 Creu Blanca
# License AGPL-3.0 or later (https://www.gnuorg/licenses/agpl.html).

import json

from odoo.http import content_disposition, request, route, serialize_exception
from odoo.tools import html_escape
from odoo.tools.safe_eval import safe_eval

from odoo.addons.web.controllers import main as report


class ReportController(report.ReportController):
    @route()
    def report_routes(self, reportname, docids=None, converter=None, **data):
        if converter == "docx":
            return self._report_routes_docx(reportname, docids, converter, **data)
        return super().report_routes(reportname, docids, converter, **data)

    def _report_routes_docx(self, reportname, docids=None, converter=None, **data):
        try:
            report = request.env["ir.actions.report"]._get_report_from_name(reportname)
            context = dict(request.env.context)
            if docids:
                docids = [int(i) for i in docids.split(",")]
            if data.get("options"):
                data.update(json.loads(data.pop("options")))
            if data.get("context"):
                # Ignore 'lang' here, because the context in data is the one
                # from the webclient *but* if the user explicitely wants to
                # change the lang, this mechanism overwrites it.
                data["context"] = json.loads(data["context"])
                if data["context"].get("lang"):
                    del data["context"]["lang"]
                context.update(data["context"])
            docx = report.with_context(**context)._render_docx(docids, data=data)[0]
            report_name = report.name
            if report.print_report_name and not len(docids) > 1:
                obj = request.env[report.model].browse(docids[0])
                report_name = safe_eval(report.print_report_name, {"object": obj})
            docxhttpheaders = [
                (
                    "Content-Type",
                    "application/vnd.openxmlformats-"
                    "officedocument.spreadsheetml.sheet",
                ),
                ("Content-Length", len(docx)),
                ("Content-Disposition", content_disposition(report_name + ".docx")),
            ]
            return request.make_response(docx, headers=docxhttpheaders)
        except Exception as e:
            se = serialize_exception(e)
            error = {"code": 200, "message": "Odoo Server Error", "data": se}
            return request.make_response(html_escape(json.dumps(error)))
