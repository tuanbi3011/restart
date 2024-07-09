from odoo import fields, models, api
from odoo.exceptions import ValidationError

class Score(models.Model):
    _name = 'school.score'
    _description = 'Điểm số môn học của học sinh'

    student_id = fields.Many2one('school.student', string='Học sinh', required=True)
    student_name = fields.Char(string='Tên học sinh', related='student_id.student_name', readonly=True)
    student_birth_date = fields.Date(string='Ngày sinh', related='student_id.date_of_birth', readonly=True)
    ma_mon_hoc = fields.Many2one('school.mon.hoc', string='Môn học', required=True)
    score = fields.Float(string='Điểm số', required=True)

    @api.model
    def create(self, vals):
        record = super(Score, self).create(vals)
        record.student_id._compute_average_score()
        return record

    def write(self, vals):
        res = super(Score, self).write(vals)
        for record in self:
            record.student_id._compute_average_score()
        return res

    def unlink(self):
        for record in self:
            student = record.student_id
            super(Score, record).unlink()
            student._compute_average_score()
        return True

# Check xem giáo viên đó đã đứng lớp nào chưa
    @api.constrains('ma_mon_hoc')
    def _check_unique_subject(self):
        for record in self:
            if record.ma_mon_hoc:
                existing_subject = self.search([('ma_mon_hoc', '=', record.ma_mon_hoc.id), ('id', '!=', record.id)])
                if existing_subject:
                    raise ValidationError("Môn học này đã có trong hồ sơ của học sinh này.")
