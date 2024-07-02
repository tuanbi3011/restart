from odoo import fields, models, api


class Teacher(models.Model):
    _name = 'school.teacher'
    _description = 'Giáo viên'

    name = fields.Char(string="Tên Giáo Viên", required=1)
    teacher_id = fields.Char(string="Mã Giáo Viên")
    description = fields.Char(string="Mô tả giáo viên")
    date_of_birth = fields.Date(string="Ngày sinh", default=lambda self: fields.Date.context_today(self))

