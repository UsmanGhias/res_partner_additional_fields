{
    'name': "Accounting Ext",
    'summary': """Accounting Extended""",
    'description': """Extended module for accounting""",
    'author': "Usman Ghias",
    'license': 'LGPL-3',
    'company': 'Telenoc',
    'website': "https://telenoc.org",
    # 'category': 'sale',
    'depends': ['base', 'sale'],
    # 'data':[
    #     'data/ir_sequence.xml',
    #     'views/sale_order_views_extended.xml',
    # ],
    'data':[
        'views/tele_res_partner.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
