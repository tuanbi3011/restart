from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Classroom(models.Model):
    _name = 'school.classroom'
    _description = 'Các lớp học'

    name = fields.Char(string="Tên lớp học", required=1)
    classroom_id = fields.Char(string="Mã lớp học")
    student_id = fields.Many2one('school.student', string="Học sinh trong lớp")
    teacher_id = fields.Many2one('school.teacher', string="Giáo viên chủ nhiệm", default=lambda self: self.env['school.teacher'].search([], limit=1))

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