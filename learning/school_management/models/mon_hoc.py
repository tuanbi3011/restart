from odoo import fields, models, api


class MonHoc(models.Model):
    _name = 'school.mon.hoc'
    _description = 'Môn học'

    name = fields.Char(string="Tên môn học", required=True)
    ma_mon_hoc = fields.Char(string="Mã môn học", required=True)
    description = fields.Text(string="Mô tả")
