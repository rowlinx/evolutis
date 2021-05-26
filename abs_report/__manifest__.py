# -*- coding: utf-8 -*-
{
    'name': "abs_report",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Kouamé Akpindrin",
    'website': "https://www.linkedin.com/in/kouam%C3%A9-akpindrin-agile%C2%AE-itil%C2%AE-devops-%C2%AE-istqb-%C2%AE-571096a5/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'account'],

    # always loaded
    'data': [
        'report/sale.xml',
        'report/invoice.xml',
        'report/invoice_no_header.xml',
        'report/report_menu.xml',
        'views/extends.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
