# -*- coding: utf-8 -*-
{
    'name': "caja_taller",

    'summary': """
        Caja menor para administracion de un punto taller""",

    'description': """
        Este modulo cuenta con orden de servicio, la cual especifica los servicios que ser prestan
    """,

    'author': "Sebastian moreno",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'license':'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/orden_servicio_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
