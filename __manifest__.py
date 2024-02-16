{
    'name': 'Nicaragua - Accounting',
    'version': '17.0.1.0',  # Update version to reflect Odoo version and module iteration
    'summary': 'Chart of Accounts for Nicaragua',  # Add a short summary of the module's purpose
    'sequence': 125,  # Optional: Define the sequence for module loading priority
    'url': 'https://github.com/Carlos9905',
    'author': 'Carlos Aguilar',
    'maintainer': 'Diego A. Munoz Del rio',
    'website': 'http://braintch.net',
    'category': 'Accounting/Localizations/Account Charts',
    'license': 'LGPL-3',
    'description': """
Chart of accounts for Nicaragua.
=================================

Includes:
---------
    * account.account.template
    * account.tax.template
    * account.chart.template
    """,
    'depends': ['account'],  # Verify dependencies are still valid for Odoo 17
    'data': [
        'data/l10n_ni_res_partner_title.xml',
        'data/l10n_ni_chart_data.xml',
        'data/account.account.template.csv',
        'data/account_tax_group_data.xml',
        'data/account_chart_template_data.xml',
        'data/account_tax_template_data.xml',
        'data/account_chart_template_configure_data.xml',
    ],
    'demo': ['demo/demo_company.xml'],
    'application': False,  # Specify if this module is an Odoo application
    'installable': True,  # Ensure the module can be installed
    'auto_install': False,  # Auto installation option based on dependencies
    'external_dependencies': {'python': [], 'bin': []},  # Define external dependencies if any
}
