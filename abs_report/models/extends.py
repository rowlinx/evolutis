# -*- coding: utf-8 -*-
from num2words import num2words
from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    def get_amount_letters(self):
        for val in self:
            val.amount_text = num2words(val.amount_total, lang='fr')

    amount_text = fields.Char(string="Montant en lettre", compute=get_amount_letters)


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def get_amount_letters(self):
        for val in self:
            val.amount_text = num2words(val.amount_total, lang='fr')

    amount_text = fields.Char(string="Montant en lettre", compute=get_amount_letters)


class ResCompany(models.Model):
    _inherit = 'res.company'

    bank_name = fields.Char(string="Nom de la banque")
    bank_code = fields.Char(string="Code banque")
    code_guichet = fields.Char(string="Code guichet")
    account_number = fields.Char(string="Numéro de compte")
    rib = fields.Char(string="RIB")
    code_swift = fields.Char(string="Code SWIFT")
