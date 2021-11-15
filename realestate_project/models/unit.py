# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models, SUPERUSER_ID, _
import logging

_logger = logging.getLogger(__name__)

class RealestateUnit(models.Model):

    _name = 'realestate.units'
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']


    name = fields.Char(string="ID")
    sales_person = fields.Many2one('res.partner' ,string="Sales Person")
    type_unit = fields.Many2one('realestate.type' ,string="Type")
    state_unit = fields.Many2one('realestate.state' ,string="state")
    state = fields.Selection([
        ('available', 'Available'),
        ('booked', 'Booked'),
        ('sold', 'Sold'),
    ])
    project_id = fields.Many2one('realestate.project',string="Project")
    product_id = fields.Many2one('product.template', string='Name')

    color = fields.Integer(string='Color Index')
