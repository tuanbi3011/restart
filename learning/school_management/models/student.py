from odoo import fields, models, api, _


class Student(models.Model):
    _name = 'school.student'
    _description = 'Học sinh'
    _rec_name = 'student_id'

    student_id = fields.Char(string="Mã Học Sinh", readonly=True, copy=False, default=lambda self: _('New'))
    student_name = fields.Char(string="Tên Học Sinh", required=1)
    description = fields.Char(string="Mô tả học sinh")
    date_of_birth = fields.Date(string="Ngày sinh", default=lambda self: fields.Date.context_today(self))
    nam_nhap_hoc = fields.Char(string="Năm Nhập Học", required=True)
    average_score = fields.Float(string='Điểm trung bình', compute='_compute_average_score', store=True)
    classroom_id = fields.Many2one('school.classroom', string='Lớp học')
    hoc_luc = fields.Char(string="Học Lực", compute="_compute_hoc_luc")

    ma_mon_hoc = fields.One2many('school.score', 'student_id', string='Môn học')

# Sinh mã id theo năm học
    @api.model
    def create(self, vals):
        if vals.get('student_id', _('New')) == _('New'):
            if 'nam_nhap_hoc' in vals:
                year = vals['nam_nhap_hoc']
                sequence_code = 'school.student.%s' % year
                sequence = self.env['ir.sequence'].search([('code', '=', sequence_code)], limit=1)
                if not sequence:
                    sequence = self.env['ir.sequence'].create({
                        'name': 'Quản Lý Học Sinh %s' % year,
                        'code': sequence_code,
                        'prefix': 'HS%s' % year,
                        'padding': 5,
                        'company_id': False,
                    })
                vals['student_id'] = sequence.next_by_id()
        return super(Student, self).create(vals)

    @api.depends('ma_mon_hoc.score')
    def _compute_average_score(self):
        for student in self:
            total_score = sum(subject.score for subject in student.ma_mon_hoc)
            subject_count = len(student.ma_mon_hoc)
            student.average_score = total_score / subject_count if subject_count > 0 else 0

    @api.depends('average_score')
    def _compute_hoc_luc(self):
        for student in self:
            if student.average_score >= 8.0:
                student.hoc_luc = 'Giỏi'
            elif student.average_score >= 6.5:
                student.hoc_luc = 'Khá'
            elif student.average_score >= 5.0:
                student.hoc_luc = 'Trung bình'
            else:
                student.hoc_luc = 'Yếu'
