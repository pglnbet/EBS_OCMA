# -*- coding: utf-8 -*-

from odoo import models, fields, api

class BillingCircle(models.Model):
    _name = 'billing.circle'
    _description = 'BillingCircle'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    title = fields.Char(string='Title')

    name = fields.Char(string='Billing Circle', compute="billing_circle")
    month = fields.Selection(selection=[('JAN', 'January'), ('FEB', 'February'), ('MAR', 'March'), ('APR', 'April'),
                                        ('MAY', 'May'), ('JUN', 'June'), ('JUL', 'July'), ('AUG', 'August'),
                                        ('AUG', 'September'), ('OCT', 'October'), ('NOV', 'November'),
                                        ('DEC', 'December'), ],
                             string='Billing Month', )
    year = fields.Selection(selection='_get_years', string='Billing Year', store=True)
    date = fields.Date(
        string='Date', 
        required=False)
    ref_no = fields.Char(
        string='Reference Number', 
        required=False)
    
    ref_sequence = fields.Char(string='Sequence No.', readonly=True, index=True, copy=False, default='New')
    
    genco_inv_verify = fields.One2many(
        comodel_name='genco.verify',
        inverse_name='billing_circle_id',
        string='Genco_inv_verify',
        required=False)
    genco_inv_verify_dollars = fields.One2many(
        comodel_name='genco.verify_dollars',
        inverse_name='billing_circle_id',
        string='Genco_inv_verify dollars',
        required=False)
    # genco_payments = fields.One2many(
    #     comodel_name='genco.payments',
    #     inverse_name='billing_circle_id',
    #     string='Genco_payments',
    #     required=False)
    disco_summary = fields.One2many(
        comodel_name='disco.summary',
        inverse_name='billing_circle_id',
        string='Disco_summary',
        required=False)
    # disco_payments = fields.One2many(
    #     comodel_name='disco.payments',
    #     inverse_name='billing_circle_id',
    #     string='Disco_payments',
    #     required=False)
    cbn_average = fields.Float(
        string='Cbn_average', 
        required=False, track_visibility=True, trace_visibility='onchange')
    nbet_dist_rate = fields.Float(
        string='Nbet_dist_rate', 
        required=False, track_visibility=True, trace_visibility='onchange')
    nbet_dist_azura = fields.Float(
        string='Nbet_dist_azura', 
        required=False, track_visibility=True, trace_visibility='onchange')
    additional_notes = fields.Text(
        string="Additional_notes",
        required=False, track_visibility=True, trace_visibility='onchange')

    hours_in_months = fields.Float(string='Hours in Month')
    transmission_loss_factor = fields.Float(string="Transmission Loss Factor")
    agip_quaterly_index = fields.Float(string="Agip Quaterly Index")
    azura_fx_date = fields.Float(string="Azura FX Date")
    azura_fx_value = fields.Float(string="Azura FX Value")
    user_id = fields.Many2one(comodel_name='res.users', string='Responsible User', default=lambda self: self.env.uid)

    @api.model
    def create(self, vals):
        if vals.get('ref_sequence', 'New') == 'New':
            vals['ref_sequence'] = self.env['ir.sequence'].next_by_code('billing.circle') or '/'
        return super(BillingCircle, self).create(vals)

    @api.multi
    @api.depends('')
    def _get_years(self):
        year_list = []
        for i in range(2010, 2046):
            year_list.append((i, str(i)))
        return year_list

    @api.one
    @api.depends('month', 'year')
    def billing_circle(self):
        for record in self:
            m = record.month
            y = record.year
            record['name'] = ("%s%s" % (m, y))
            
            
class GencoVerify(models.Model):
    _name = 'genco.verify'
    _description = 'GencoVerify'

    name = fields.Char()
    genco_id = fields.Many2one(
        comodel_name='res.partner',
        string='Genco',
        required=False)
    capacity_payment = fields.Float(
        string='Capacity Payments',
        required=False)
    energy_payment = fields.Float(
        string='Energy payments',
        required=False)
    startup_payment = fields.Float(
        string='Startup Payments',
        required=False)
    interest_payment = fields.Float(
        string='Interest Payments',
        required=False)
    total_payment = fields.Float(
        string='Total Payments',
        required=False)
    nbet_computed = fields.Float(
        string='Nbet computed figures',
        required=False)
    date_received = fields.Date(
        string='Date received',
        required=False)
    due_date = fields.Date(
        string='Due date',
        required=False)
    cus_invoice_ref = fields.Char(
        string='Customer invoice ref',
        required=False)
    billing_circle_id = fields.Many2one(
        comodel_name='billing.circle',
        string='Billing Circle',
        required=False)


class GencoVerifyDollars(models.Model):
    _name = 'genco.verify_dollars'
    _description = 'GencoVerify'

    name = fields.Char()
    genco_id = fields.Many2one(
        comodel_name='res.partner',
        string='Genco_id',
        required=False)
    capacity_payment = fields.Float(
        string='Capacity_payment', 
        required=False)
    energy_payment = fields.Float(
        string='Energy_payment', 
        required=False)
    startup_payment = fields.Float(
        string='Startup_payment', 
        required=False)
    interest_payment = fields.Float(
        string='Interest_payment', 
        required=False)
    total_payment = fields.Float(
        string='Total_payment', 
        required=False)
    nbet_computed = fields.Float(
        string='Nbet_computed', 
        required=False)
    date_received = fields.Date(
        string='Date_received', 
        required=False)
    due_date = fields.Date(
        string='Due_date', 
        required=False)
    cus_invoice_ref = fields.Char(
        string='Cus_invoice_ref', 
        required=False)
    billing_circle_id = fields.Many2one(
        comodel_name='billing.circle',
        string='Billing Circle',
        required=False)

class DiscoSummary(models.Model):
    _name = 'disco.summary'
    _description = 'DiscoSummary'

    name = fields.Char()
    disco_id = fields.Many2one(
        comodel_name='res.partner',
        string='Disco_id',
        required=False)
    capacity_delivered = fields.Float(
        string='Capacity_delivered',
        required=False)
    energy_delivered = fields.Float(
        string='Energy_delivered',
        required=False)
    percentage_total = fields.Float(
        string='Percentage of total',
        required=False)
    portion_capacity = fields.Float(
        string='Portion_capacity',
        required=False)
    portion_energy = fields.Float(
        string='Portion_energy',
        required=False)
    invoice_value = fields.Float(
        string='Invoice_value',
        required=False)
    billing_circle_id = fields.Many2one(
        comodel_name='billing.circle',
        string='Billing Circle',
        required=False)





# class ebs_ocma(models.Model):
#     _name = 'ebs_ocma.ebs_ocma'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100