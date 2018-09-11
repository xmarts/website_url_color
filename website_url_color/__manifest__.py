# -*- coding: utf-8 -*-
{
    'name': "website_url_color",

    'summary': """
        Links Color of WEBSITE""",

    'description': """
        Change link color of website.
    """,

    'author': "Pablo Osorio Gama, XMARTS",
    'website': "https://www.xmarts.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website'],

    # always loaded
    'data': [
        'views/templates.xml',
    ],
}