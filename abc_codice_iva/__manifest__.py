# -*- coding: utf-8 -*-
{
    'name': "ABC - abc_codiceIva",

    'summary': """
        Modulo che permette di aggiungere il campo Codice Iva nelle Imposte di Contabilità.""",

    'description': """
        Modulo che permette di aggiungere il campo Codice Iva nelle Imposte di Contabilità.
    """,

    'author': "A.B.C srl",
    'website': "https://www.abcstrategie.it/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Account',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    "installable": True,
}
