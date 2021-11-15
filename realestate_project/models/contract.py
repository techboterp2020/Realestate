# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models, SUPERUSER_ID, _
import logging

_logger = logging.getLogger(__name__)

class RealestateContract(models.Model):

    _name = 'realestate.contract'

    name = fields.Char(string="ID")
    sale_order_id = fields.Many2one('res.partner' ,string="Sale order")
    client = fields.Many2one('res.partner' ,string="Customer")
    type_unit = fields.Many2one('type.unit' ,string="Type")
    state_unit = fields.Many2one('state.unit' ,string="state")
    project_id = fields.Many2one('realestate.project',string="Project")
    contract_date =fields.date(string="Contract date")
    