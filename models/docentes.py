# -*- coding:utf-8 -*-

from odoo import fields, models, api
 
class Docentes(models.Model):
    _name = "docentes"
    nombres = fields.Char()
    apellidos = fields.Char()
    