from odoo import fields, models, api


class Student(models.Model):
    _name = 'school.student'
    _description = 'Học sinh'

    name = fields.Char(string="Tên Học Sinh", required=1)
    student_id = fields.Char(string="Mã Học Sinh")
    description = fields.Char(string="Mô tả học sinh")
    date_of_birth = fields.Date(string="Ngày sinh", default=lambda self: fields.Date.context_today(self))


