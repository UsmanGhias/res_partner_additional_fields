# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    partner_code = fields.Char(
        string='Partner Code',
        copy=False,
        index=True,
        help='Unique internal identification or account code for this partner.'
    )
    cr_number = fields.Char(
        string='Commercial Reg. (CR) No.',
        index=True,
        help='Official Commercial Registration or Trade License registration number.'
    )
    nature_of_business = fields.Char(
        string='Nature of Business / Goods',
        help='Primary commercial activities, business sector, or goods supplied.'
    )
    partner_category_type = fields.Selection([
        ('corporate', 'Corporate / Private Enterprise'),
        ('government', 'Government Entity'),
        ('semi_government', 'Semi-Government'),
        ('ngo', 'NGO / Non-Profit'),
        ('individual', 'Individual / Sole Proprietor'),
        ('foreign_company', 'Foreign / Multinational')
    ], string='Organization Type', default='corporate', tracking=True)

    business_classification = fields.Selection([
        ('customer', 'Customer'),
        ('vendor', 'Vendor / Supplier'),
        ('contractor', 'Contractor / Subcontractor'),
        ('partner', 'Strategic Partner')
    ], string='Business Classification', default='customer', tracking=True)

    partner_status = fields.Selection([
        ('active', 'Active & Approved'),
        ('under_review', 'Under Review / Onboarding'),
        ('suspended', 'Suspended / On Hold'),
        ('blocked', 'Blocked')
    ], string='Compliance Status', default='active', tracking=True)

    preferred_shipping_method = fields.Selection([
        ('air', 'Air Freight'),
        ('sea', 'Sea Freight'),
        ('road', 'Road Transportation'),
        ('courier', 'Express Courier'),
        ('pickup', 'Customer Pickup')
    ], string='Preferred Shipping Method')

    shipping_agent_code = fields.Char(
        string='Shipping Agent Code',
        help='Reference code for designated forwarder or shipping agent.'
    )
    payment_method_preference = fields.Selection([
        ('bank_transfer', 'Bank Wire / EFT'),
        ('check', 'Corporate Check'),
        ('credit_card', 'Credit / Debit Card'),
        ('cash', 'Cash on Delivery')
    ], string='Payment Preference', default='bank_transfer')

    vat_applicable = fields.Boolean(
        string='VAT / Tax Applicable',
        default=True,
        help='Indicates whether sales or purchases for this partner are subject to VAT.'
    )
