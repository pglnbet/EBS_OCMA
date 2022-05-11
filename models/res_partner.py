# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class Partner(models.Model):
    _inherit = 'res.partner'

    is_disco = fields.Boolean(string='Disco')
    is_genco = fields.Boolean(string='Genco')
    
    vesting_contract = fields.Boolean(string='Vesting Contract')

    contract_capacity_share = fields.Float('Contract Capacity Share')
    