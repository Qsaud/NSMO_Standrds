{
    "name": "QSteps Project Customization",
    "version": "18.0.1.0.0",
    "category": "Project",
    "summary": "Customizations for Odoo 18 Project module",
    "depends": ["project"],
    "data": [
        "security/ir.model.access.csv",
        "views/project_task_views.xml",
        "views/project_project_views.xml",
        "views/project_bucket_views.xml",
    ],
    "installable": True,
    "application": False,
    "license": "LGPL-3",
}
