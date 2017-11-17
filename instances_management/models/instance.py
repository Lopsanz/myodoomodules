# -*- coding: utf-8 -*-
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

import odoo
from odoo import _, api, fields, models



class Instance(models.Model):
    _name="instance"
    _description = "Instances of Odoo working"

    name = fields.Char(
        string='Machine',
        required=True,
    )
    active = fields.Boolean(
        default=True,
    )
    ip_address = fields.Char(
        string = "IP Address"
    )
    version = fields.Selection([
        ('8.0', '8.0'),
        ('10.0', '10.0'),
        ('11.0', '11.0'),
        ]
    )
    res_partner_id = fields.Many2one(
        'res.partner'
    )
    domain = fields.Html(
        "Domain access"
    )
    #machine_id = fields.Many2one(
    #    "machine"
    #)
    alive = fields.Boolean( string="Is online",  )
    description = fields.Text(
        "About this Instance"
    )
    ssh_login=fields.Char("SSH User")
    ssh_pwd=fields.Char("SSH password")
    backend_login    = fields.Char("Odoo Login")
    backend_pwd      = fields.Char("Odoo password")
    postgresql_login = fields.Char("PSQL Login")
    postgresql_pwd = fields.Char("PSQL password")
