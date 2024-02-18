# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models
from odoo.addons.account.models.chart_template import template


class AccountChartTemplate(models.AbstractModel):
    _inherit = 'account.chart.template'

    @template('ni')
    def _get_ni_template_data(self):
        return {
            'code_digits': '9',
            'property_account_receivable_id': 'cta11010101',
            'property_account_payable_id': 'cta21010101',
            'property_account_income_categ_id': 'cta44010102',
            'property_account_expense_categ_id': 'cta51020100',
    }

    @template('ni', 'res.company')
    def _get_ni_res_company(self):
        return {
            self.env.company.id: {
                'account_fiscal_country_id': 'base.ni',
                'bank_account_code_prefix': '10010',
                'cash_account_code_prefix': '10020',
                'transfer_account_code_prefix': '100301',
                'account_default_pos_receivable_account_id': 'cta11020108',
                'income_currency_exchange_account_id': 'cta45010102',
                'expense_currency_exchange_account_id': 'cta710101',
                # 'account_sale_tax_id': 'impuestos_plantilla_iva_por_pagar',
                # 'account_purchase_tax_id': 'impuestos_plantilla_iva_por_cobrar',
            },
        }

