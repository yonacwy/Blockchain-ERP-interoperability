{
    'name': 'SCM',
    "version": "17.0.1.0.0",
    'category': 'Sales/CRM',
    'summary': 'SCM module',
    'description': "",
    'depends': ['base'],
    'data': [
             'security/ir.model.access.csv',
             'views/transaction.xml',
             'views/enrollment.xml',
             'views/register.xml',
             'views/query.xml',
             'views/template.xml',
             'views/menus_view.xml',
             ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OPL-1',

}
