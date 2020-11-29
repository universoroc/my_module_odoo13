# -*- coding: utf-8 -*-
# from odoo import http


# class MyModuleOdoo13(http.Controller):
#     @http.route('/my_module_odoo13/my_module_odoo13/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_module_odoo13/my_module_odoo13/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_module_odoo13.listing', {
#             'root': '/my_module_odoo13/my_module_odoo13',
#             'objects': http.request.env['my_module_odoo13.my_module_odoo13'].search([]),
#         })

#     @http.route('/my_module_odoo13/my_module_odoo13/objects/<model("my_module_odoo13.my_module_odoo13"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_module_odoo13.object', {
#             'object': obj
#         })
