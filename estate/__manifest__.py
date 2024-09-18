{
    'name': "Estate",
    'version': '1.0',
    'depends': ['base'],
    'author': "Ezra",
    'category': 'Sales/CRM',
    'data': [
        'security/ir.model.access.csv',
        
        'views/estate_property_views.xml',        
        'views/estate_menus.xml',
    ],
    'installable': True,
    'application': True,    
}