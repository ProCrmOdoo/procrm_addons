# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name": "Assign Task To Multiple Users",
    "author": "Softhealer Technologies",
    "website": "http://www.softhealer.com",
    "support": "support@softhealer.com",
    "license": "OPL-1",
    "category": "Project",
    "summary": "task to multi user,task to multiple user,single task to multiple user,single task to mult user,assign single task to users,Multiple User for Project Task,Assign one task to multiple user,Task Assigned Multi Users,Multiple users in one task Odoo",
    "description": """This module is very useful in the case where you have multiple users who going to manage different actions based on tasks. This module allows to assign a single task to multiple users. That task visible for all assigned users.""",
    "version": "14.0.1",
    "depends": [
        "project",
    ],
    "application": True,
    "data": [
        "views/res_config_settings.xml",
        "views/project_task.xml",
    ],
    "images": ["static/description/background.png", ],
    "auto_install": False,
    "installable": True,
    "price": "15",
    "currency": "EUR"
}
