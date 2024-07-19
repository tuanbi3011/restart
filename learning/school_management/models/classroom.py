from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Classroom(models.Model):
    _name = 'school.classroom'
    _description = 'Các lớp học'
    _rec_name = 'classroom_id'

    name = fields.Char(string="Tên lớp học", required=1)
    classroom_id = fields.Char(string="Mã lớp học")
    teacher_id = fields.Many2one('school.teacher', string="Giáo viên chủ nhiệm", default=lambda self: self.env['school.teacher'].search([], limit=1))

    student_ids = fields.One2many('school.student', 'classroom_id', string='Học sinh trong lớp')
#Để quản lý chuyện đứng lớp giáo viên, tự động cập nhật bên class teacher
    @api.model
    def create(self, vals):
        res = super(Classroom, self).create(vals)
        if res.teacher_id:
            res.teacher_id.write({'classroom_id': res.id})
        return res

    def write(self, vals):
        res = super(Classroom, self).write(vals)
        if 'teacher_id' in vals:
            teacher = self.env['school.teacher'].browse(vals['teacher_id'])
            teacher.write({'classroom_id': self.id})
        return res

# Check xem giáo viên đó đã đứng lớp nào chưa
    @api.constrains('teacher_id')
    def _check_unique_teacher(self):
        for record in self:
            if record.teacher_id:
                existing_classroom = self.search([('teacher_id', '=', record.teacher_id.id), ('id', '!=', record.id)])
                if existing_classroom:
                    raise ValidationError("Giáo viên này đã được chỉ định cho một lớp học khác.")

    @api.onchange('student_ids')
    def _onchange_student_ids(self):
        for student in self.student_ids:
            student_name = student.student_name
            date_of_birth = student.date_of_birth

    @api.depends('student_ids')
    def _compute_average_scores(self):
        for classroom in self:
            self.env.cr.execute("""
                SELECT s.id, AVG(ss.score)
                FROM school_student s
                JOIN school_student_subject ss ON s.id = ss.student_id
                WHERE s.classroom_id = %s
                GROUP BY s.id
            """, (classroom.id,))
            scores = dict(self.env.cr.fetchall())
            for student in classroom.student_ids:
                student.average_score = scores.get(student.id, 0.0)