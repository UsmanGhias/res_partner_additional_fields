# -*- coding: utf-8 -*-
{
    'name': 'Partner Commercial Extra Fields & Master Data',
    'version': '17.0.1.0.0',
    'category': 'Sales',
    'summary': 'Enrich partner master data with Commercial Registration (CR), organization type, compliance status, and logistics preferences.',
    'description': """
Partner Commercial Extra Fields & Master Data
=============================================
Enrich Odoo customer and vendor profiles with essential commercial, regulatory, and logistics master data fields.

Key Features:
-------------
* Commercial Registration (CR) and Trade License tracking
* Partner Code identifier for internal reference and ERP migration
* Organization Type classification (Corporate, Government, Semi-Govt, NGO, Foreign Company)
* Business Classification (Customer, Vendor, Contractor, Strategic Partner)
* Compliance & Onboarding Status (Active, Under Review, Suspended, Blocked)
* Preferred Logistics & Shipping Method (Air, Sea, Road, Express Courier, Pickup)
* Payment method preferences and Tax / VAT applicability flags
* Dedicated Commercial & Compliance tab on contact forms with responsive group layouts
    """,
    'author': 'CODCrafters, Usman Ghias',
    'website': 'https://usmanghias.co.uk',
    'support': 'support@codcrafters.org',
    'license': 'OPL-1',
    'price': 19.00,
    'currency': 'EUR',
    'depends': ['base'],
    'data': [
        'views/res_partner_views.xml',
    ],
    'images': [
        'static/description/banner.png',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
