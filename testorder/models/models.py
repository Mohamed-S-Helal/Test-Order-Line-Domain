# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TestOrder(models.Model):
    _name = 'test.order'

    name = fields.Char()
    line_ids = fields.One2many('test.order.line', 'order_id')


class TestOrderLine(models.Model):
    _name = 'test.order.line'

    @api.onchange('product_id')
    def _get_domain(self):
        print(self)
        return {'domain': {'product_id': [('id', 'not in', self.order_id.line_ids.mapped('product_id.id'))]}}

    order_id = fields.Many2one('test.order')
    product_id = fields.Many2one('product.product')

