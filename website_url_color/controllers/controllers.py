# -*- coding: utf-8 -*-
from odoo import http

# class WebsiteUrlColor(http.Controller):
#     @http.route('/website_url_color/website_url_color/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_url_color/website_url_color/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_url_color.listing', {
#             'root': '/website_url_color/website_url_color',
#             'objects': http.request.env['website_url_color.website_url_color'].search([]),
#         })

#     @http.route('/website_url_color/website_url_color/objects/<model("website_url_color.website_url_color"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_url_color.object', {
#             'object': obj
#         })