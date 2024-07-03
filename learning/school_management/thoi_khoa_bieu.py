from odoo import fields, models, api


class ThoiKhoaBieu(models.Model):
    _name = 'school.thoi.khoa.bieu'
    _description = 'Thời khóa biểu'

    name = fields.Char(string='Title', required=True)
    classroom_id = fields.Many2one('school.classroom', string='Lớp học', required=True)
    teacher_id = fields.Many2one('school.teacher', string='Giáo viên', required=True)
    student_ids = fields.Many2many('school.student', string='Học sinh')
    start_time = fields.Datetime(string='Start Time', required=True)
    end_time = fields.Datetime(string='End Time', required=True)
