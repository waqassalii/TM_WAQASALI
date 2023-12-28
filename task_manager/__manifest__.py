# -*- coding: utf-8 -*-
{
    'name': "Task Manager",
    'summary': "This module manages the Tasks",
    'description': """ This module manages the Tasks """,
    'author': "WaqasAli",
    'website': "waysSolutions",
    'category': 'Uncategorized',
    'version': '17.0.1.0.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}

