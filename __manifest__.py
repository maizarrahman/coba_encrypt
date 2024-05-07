# -*- coding: utf-8 -*-
{
    'name': "Coba - Encrypt",

    'summary': """
        Uji coba module field_encryption""",

    'description': """
        Uji coba module field_encryption
    """,

    'author': "Maizar",
    'website': "http://www.metalindo.com",
    'images': [],
    "application": True,
    "installable": True,
    'category': 'Metalindo',
    'version': '1.0',
    'sequence': 5,

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'field_encryption',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/coba_encrypt.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}
