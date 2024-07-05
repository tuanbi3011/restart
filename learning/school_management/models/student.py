from odoo import fields, models, api, _


class Student(models.Model):
    _name = 'school.student'
    _description = 'Học sinh'

    name = fields.Char(string="Tên Học Sinh", required=1)
    student_id = fields.Char(string="Mã Học Sinh", readonly=True, copy=False, default=lambda self: _('New'))
    description = fields.Char(string="Mô tả học sinh")
    date_of_birth = fields.Date(string="Ngày sinh", default=lambda self: fields.Date.context_today(self))
    nam_nhap_hoc = fields.Char(string="Năm Nhập Học", required=True)

    @api.model
    def create(self, vals):
        if vals.get('student_id', _('New')) == _('New'):
            if 'year_of_admission' in vals:
                year = vals['year_of_admission']
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

