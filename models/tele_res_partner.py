from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description='Additional Fields'

    tele_code = fields.Char(string='Code')
    # cr_number = fields.Char(string="CR No.")
    # nature_of_services_goods = fields.Char(string='Nature of Goods')
    # classification = fields.Selection([
    #     ('employee', "Employee"), ('vendor', "Vendor"), ('landlord', "LandLord"),
    # ],string="Classification")
    # cost_center = fields.Many2one('account.analytic.account', string='cost Center')
    # vendor_posting_group = fields.Selection([
    #     ('landlord', "LandLord"),('e00001', "E00001"), ('gre00001',"gre00001"),('ic00001',"IC00001"),('tp00001',"TP00001")
    # ],string='Vendor Posting Group')
    # shipment_method_code = fields.Selection([
    #     ('airway', "Airway"),('shipping',"Shipping"),('road',"Road"),('service',"Service")
    # ], string='shipment Method Code')
    #
    # shipping_agent_code = fields.Char(string="Shipping Agent Code")
    # status= fields.Selection([
    #     ('active', 'Active'),
    #     ('blocked', 'Blocked'),
    # ],string='Status')
    #
    # payment_method = fields.Selection([
    #     ('bank', 'Bank'),
    #     ('check', 'Check'),
    # ], string='Payment Method')
    #
    # auto_manual = fields.Selection([
    #     ('auto', 'Auto'),
    #     ('manual', 'Manual'),
    # ], string="Auto/Manual")
    #
    # foreign_local = fields.Selection([
    #     ('foreign', 'Foreign'),
    #     ('local', 'Local'),
    # ], string='Foreign/Local')
    #
    # vat_applicable = fields.Selection([
    #     ('yes', 'Yes'),
    #     ('no', 'No'),
    # ], string='Vat Applicable')
    #
    # vat_posting_group = fields.Selection([
    #     ('v15', 'Vat 15%'),
    #     ('v5', 'Vat 5%'),
    #     ('w5', 'WHT 5%'),
    #     ('w15', 'WHT 15%')
    #
    # ], string='Vat Posting Group')
    #
    # block_payment_toll = fields.Char(string="Block Payment Tolerance")
    # advance = fields.Float(string="Advanced Percentage")
    #
    # partner_type = fields.Selection([
    #     ('company', 'Active'),
    #     ('individual', 'Blocked'),
    #     ('government', 'Government'),
    #     ('semigovernment','Semi Government'),
    #     ('ngo', 'NGO'),
    #     ('foreigncompany','Foreign Company')
    # ], string='Partner Type')

