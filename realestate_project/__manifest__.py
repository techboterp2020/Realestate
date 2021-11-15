# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Realestate Project',
    'sequence': 1,
    'summary': 'Realestate ',
    'description': """
    Realestate
    """,
    'depends': ['product','base','mail','portal'],
    'data': [
            # 'security/group.xml',
            # 'security/ir.model.access.csv',
            'views/state_unit_views.xml',
            # 'views/product_unit.xml',
            'views/projects_views.xml',
            'views/type_unit_views.xml',
            'views/units_views.xml',
            'views/menus.xml',
            # 'data/data.xml',
              ],
     'images': [
        'static/src/img/house.png',
    ],

    'installable': True,
    'application': True,
    # 'auto_install': False
}
