# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    test_field = fields.Char(string='Campo Test', store=True)
    prova_integer = fields.Integer('Prova Integer')
    description_unina = fields.Text('Desc Unina')
    #value = fields.Integer('')
    #value2 = fields.Float(compute="_value_pc", store=True)
    #description = fields.Text()

    #@api.depends('value')
    #def _value_pc(self):
    #    for record in self:
    #        record.value2 = float(record.value) / 100
