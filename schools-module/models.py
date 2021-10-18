from odoo import models,fields

class School(models.Model):
    _name = "school_module"

    name = fields.Char()
    adress = fields.Char()
    director = fields.Char()
    students = fields.Integer()
    foundation = fields.Date()
