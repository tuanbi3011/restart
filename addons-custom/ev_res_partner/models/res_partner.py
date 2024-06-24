# -*- coding: utf-8 -*-

from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    type_partner = fields.Selection([
        ('private', 'Private'),
        ('public', 'Public'),
    ], default='public', string='Type Partner', check='True')
#    have_write_right = fields.Boolean(string='Have write right', compute="_compute_have_write_right")

#    @api.onchange('translate_display_name')
    # phân quyền
#    def _compute_have_write_right(self):
#        if self.env.user.has_group('res_group.group_user'):
#            self.have_write_right = False  # nếu False thì goup_user có quyền
#        if self.env.user.has_group('res_group.group_sale'):
#            self.have_write_right = True  # nếu True thì goup_admin có quyền

#    @api.model
#    def create(self, vals):
#        vals['name'] = self.env['ir.sequence'].next_by_code('res.partner')
#        if not self.go:
#            vals['go'] = True
#        return super(ResPartner, self).create(vals)


