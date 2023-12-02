{
    'name': 'Nicaragua - Accounting',
    'url': 'https://github.com/Carlos9905',
    'author': 'Carlos Aguilar',
    'website': 'http://braintch.net',
    'category': 'Accounting/Localizations/Account Charts',
    'description': """
Chart of accounts for Nicaragua.
=================================

Includes:
---------
    * account.account.template
    * account.tax.template
    * account.chart.template
    """,
    'depends': ['account'],
    'data': [
        'data/l10n_ni_res_partner_title.xml',
        'data/l10n_ni_chart_data.xml',
        'data/account.account.template.csv',
        'data/account_tax_group_data.xml',
        'data/account_chart_template_data.xml',
        'data/account_tax_template_data.xml',
        'data/account_chart_template_configure_data.xml',
    ],
    'demo': [
        'demo/demo_company.xml',
    ],
    'license': 'LGPL-3',
}