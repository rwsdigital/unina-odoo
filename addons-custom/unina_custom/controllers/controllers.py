# -*- coding: utf-8 -*-
# Part of RWSdigital. See LICENSE file for full copyright and licensing details.
from odoo import http

# class UninaCustom(http.Controller):
#     @http.route('/unina_custom/unina_custom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/unina_custom/unina_custom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('unina_custom.listing', {
#             'root': '/unina_custom/unina_custom',
#             'objects': http.request.env['unina_custom.unina_custom'].search([]),
#         })

#     @http.route('/unina_custom/unina_custom/objects/<model("unina_custom.unina_custom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('unina_custom.object', {
#             'object': obj
#         })