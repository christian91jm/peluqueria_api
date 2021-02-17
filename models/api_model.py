from odoo import models, fields, api


class api_model(models.Model):
    _name = 'peluqueria.productos_model'
    _inherit = 'peluqueria.productos_model'
    _description = 'api socios'

    proveedor = fields.Many2one("res.partner","Proveedor")
