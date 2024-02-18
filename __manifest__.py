{
    'name': 'Nicaragua - Accounting',
    'countries':['ni'],  # Add country code to ensure the module is loaded for the specific country
    'version': '17.0.1.0',  # Update version to reflect Odoo version and module iteration
    'summary': 'Chart of Accounts for Nicaragua',  # Add a short summary of the module's purpose
    'sequence': 125,  # Optional: Define the sequence for module loading priority
    'url': 'https://github.com/Carlos9905',
    'author': 'Diego A. Munoz Del rio',
    'website': 'https://dmunoz2019.github.io/diegoweb/',
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
    'depends': ['base','account'],  # Verify dependencies are still valid for Odoo 17
    'data': [
       
    ],
    'application': False,  # Specify if this module is an Odoo application
    'installable': True,  # Ensure the module can be installed
    'auto_install': False,  # Auto installation option based on dependencies
    'external_dependencies': {'python': [], 'bin': []},  # Define external dependencies if any
}
