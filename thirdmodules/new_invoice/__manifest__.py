# -*- coding: utf-8 -*-
{
    'name': 'New Invoice GBA',
    
    'summary': """
        Nuevo formato de Factura 3.3 """,
    
    'description': """
        Se realiza modificaciones en factura para cumplir con la reforma de facturacion CFDI 3.3 """,
    
    'author': "GBA Tecnologías",
    'website': "http://www.gba.com.mx",
    
    'category': 'Invoice',
    'version': '0.1',
    
    'depends': ['account', 'l10n_mx_edi'],
    
    'data': [
        'view/CodeUse_view.xml',
        'view/new_invoice_view.xml',
    ],
    'installable': True,
    'auto_install': False,    
}
