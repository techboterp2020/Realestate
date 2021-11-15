# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models, SUPERUSER_ID, _
import logging

_logger = logging.getLogger(__name__)

class Realestatetype(models.Model):

    _name = 'realestate.type'

    name = fields.Char(string="Type Name")
