from odoo import fields, models, api


class ThoiKhoaBieu(models.Model):
    _name = 'school.thoi.khoa.bieu'
    _description = 'Thời khóa biểu'

    name = fields.Char(string='Thời khóa biểu tháng', required=True)
    classroom_id = fields.Many2one('school.classroom', string='Lớp học', required=True)
    teacher_id = fields.Many2one('school.teacher', string='Giáo viên', required=True)
    student_id = fields.Many2many('school.student', string='Học sinh')
    ma_mon_hoc = fields.Many2one('school.mon.hoc', string='Môn học')
    start_time = fields.Datetime(string='Thời gian bắt đầu', required=True)
    stop_time = fields.Datetime(string='Thời gian kết thúc', required=True)

    @api.onchange('classroom_id')
    def _onchange_classroom(self):
        if self.classroom_id:
            self.student_ids = self.classroom_id.student_ids
            self.teacher_id = self.classroom_id.teacher_id
