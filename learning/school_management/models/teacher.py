from odoo import fields, models, api, _


class Teacher(models.Model):
    _name = 'school.teacher'
    _description = 'Giáo viên'

    name = fields.Char(string="Tên Giáo Viên", required=1)
    teacher_id = fields.Char(string="Mã Giáo Viên", readonly=True, copy=False, default=lambda self: self.env['ir.sequence'].next_by_code('school.teacher'))
    chu_nhiem = fields.Boolean(string="Chủ nhiệm")
    classroom_id = fields.Many2one('school.classroom', string="Dạy lớp :", default='_onchange_classroom')
    description = fields.Char(string="Mô tả giáo viên")
    date_of_birth = fields.Date(string="Ngày sinh", default=lambda self: fields.Date.context_today(self))

    @api.onchange('classroom_id')
    def _onchange_classroom(self):
        if self.classroom_id:
            self.classroom_id.teacher_id = self

    @api.model
    def create(self, vals):
        if 'teacher_id' not in vals or not vals['teacher_id']:
            vals['teacher_id'] = self.env['ir.sequence'].next_by_code('school.teacher')
        return super(Teacher, self).create(vals)