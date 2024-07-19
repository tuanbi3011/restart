from odoo import fields, models, api


class ThemHocSinh(models.Model):
    _name = 'them.hoc.sinh'
    _description = 'Thêm học sinh vào lớp học'

    student_ids = fields.Many2many('school.student', string='Học sinh')


    @api.model
    def default_get(self, fields):
        res = super(ThemHocSinh, self).default_get(fields)
        active_id = self.env.context.get('active_id')
        if active_id:
            classroom = self.env['school.classroom'].browse(active_id)
            res['student_ids'] = classroom.student_ids.ids
        return res

    def add_students(self):
        active_id = self.env.context.get('active_id')
        if active_id:
            classroom = self.env['school.classroom'].browse(active_id)
            classroom.student_ids = [(6, 0, self.student_ids.ids)]
        return {'type': 'ir.actions.act_window_close'}
