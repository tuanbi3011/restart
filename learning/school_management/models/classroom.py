from odoo import fields, models, api


class Classroom(models.Model):
    _name = 'school.classroom'
    _description = 'Các lớp học'

    name = fields.Char(string="Tên lớp học", required=1)
    classroom_id = fields.Char(string="Mã lớp học", required=1)
