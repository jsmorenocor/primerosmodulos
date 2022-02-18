# -*- coding: utf-8 -*-
# from odoo import http


# class CajaTaller(http.Controller):
#     @http.route('/caja_taller/caja_taller', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/caja_taller/caja_taller/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('caja_taller.listing', {
#             'root': '/caja_taller/caja_taller',
#             'objects': http.request.env['caja_taller.caja_taller'].search([]),
#         })

#     @http.route('/caja_taller/caja_taller/objects/<model("caja_taller.caja_taller"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('caja_taller.object', {
#             'object': obj
#         })
