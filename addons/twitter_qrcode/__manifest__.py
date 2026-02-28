{
    'name': 'Twitter QR Code',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Generate QR codes for Twitter/X accounts',
    'author': 'Curt Coetzee',
    'depends': ['base', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'views/twitter_account_views.xml',
        'views/website_templates.xml',
    ],
    'installable': True,
    'application': True,
}