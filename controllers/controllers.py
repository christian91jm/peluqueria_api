# -*- coding: utf-8 -*-
# from odoo import http


# class PeluqueriaApi(http.Controller):
#     @http.route('/peluqueria_api/peluqueria_api/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/peluqueria_api/peluqueria_api/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('peluqueria_api.listing', {
#             'root': '/peluqueria_api/peluqueria_api',
#             'objects': http.request.env['peluqueria_api.peluqueria_api'].search([]),
#         })

#     @http.route('/peluqueria_api/peluqueria_api/objects/<model("peluqueria_api.peluqueria_api"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('peluqueria_api.object', {
#             'object': obj
#         })
