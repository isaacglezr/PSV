# -*- coding: utf-8 -*-
from odoo import api, fields, models

class Sale_field(models.Model):

    _inherit='account.invoice'

    aref = fields.Reference([('sale_order', 'String')])
    x_OrdenCompra = fields.Char(string='Orden de Compra', compute="_orden_agregar")

    @api.multi
    @api.depends('origin')
    def _orden_agregar(self):
        for record in self:
#            cr = self.env.cr
#            sql = cr.execute("SELECT x_ordendecompra FROM sale_order where name='%s';" % self.origin)
#            record['x_OrdenCompra'] = sql
#            record['x_OrdenCompra'] = cr.fetchone()
             record['x_OrdenCompra'] = self.env['sale.order'].search([('name', '=', self.origin)]).x_ordendecompra
