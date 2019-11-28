# -*- coding: utf-8 -*-
# Part of RWSdigital. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api

class ResPartner(models.Model):
    _name = 'unina_custom.unina_custom'

    class ResPartner(models.Model):
        _inherit = "res.partner"

        birthdate_date = fields.Date("Birthdate")
