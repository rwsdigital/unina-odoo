# -*- coding: utf-8 -*-
from odoo import http

# class RwsdigitalSale(http.Controller):
#     @http.route('/rwsdigital_sale/rwsdigital_sale/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rwsdigital_sale/rwsdigital_sale/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rwsdigital_sale.listing', {
#             'root': '/rwsdigital_sale/rwsdigital_sale',
#             'objects': http.request.env['rwsdigital_sale.rwsdigital_sale'].search([]),
#         })

#     @http.route('/rwsdigital_sale/rwsdigital_sale/objects/<model("rwsdigital_sale.rwsdigital_sale"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rwsdigital_sale.object', {
#             'object': obj
#         })