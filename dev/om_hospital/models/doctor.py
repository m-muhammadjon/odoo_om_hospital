from odoo import models, fields


class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _inherit = "mail.thread"
    _description = "Doctor Records"

    name = fields.Char(string="Name", required=True, tracking=True)
    gender = fields.Selection([("male", "Male"), ("female", "Female")], string="Gender", tracking=True)
    ref = fields.Char(string="Reference", required=True)

