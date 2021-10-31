# -*- coding: utf-8 -*-
from odoo import http

# class EbsOcma(http.Controller):
#     @http.route('/ebs_ocma/ebs_ocma/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ebs_ocma/ebs_ocma/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ebs_ocma.listing', {
#             'root': '/ebs_ocma/ebs_ocma',
#             'objects': http.request.env['ebs_ocma.ebs_ocma'].search([]),
#         })

#     @http.route('/ebs_ocma/ebs_ocma/objects/<model("ebs_ocma.ebs_ocma"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ebs_ocma.object', {
#             'object': obj
#         })