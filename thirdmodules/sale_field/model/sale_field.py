# -*- coding: utf-8 -*-
from odoo import api, fields, models

class Sale_field(models.Model):

    _inherit='sale.order'

    x_ordendecompra = fields.Char(string='Orden de Compra')
