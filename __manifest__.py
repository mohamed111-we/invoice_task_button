# -*- coding: utf-8 -*-
{
    'name': 'Account Invoice Task State',
    'version': '1.0',
    'summary': 'إضافة حالة وزرار وحقل اسم التاسك في الفاتورة',
    'sequence': 10,
    'description': """
        هذا الموديول يقوم بتعديل شاشة الفواتير لإضافة:
        - حالة جديدة (State)
        - زرار لتغيير الحالة
        - حقل لعرض اسم التاسك
    """,
    'category': 'Accounting',
    'author': 'Your Name',
    'website': 'https://www.yourwebsite.com',
    'depends': ['accountant'],
    'data': [
        'security/security.xml',
        'views/account_move.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}