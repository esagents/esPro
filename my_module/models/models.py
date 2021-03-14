# -*- coding: utf-8 -*-
from unidecode import unidecode
from odoo import models, fields, api

class my_module(models.Model):
    _name = 'my_module.my_module'
    _description = 'my_module.my_module'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    start_datetime = fields.Datetime('Start time', default=lambda self: fields.Datetime.now())
    
    @api.model
    def create(self, values):
        if 'name' in values:
            values['name'] = unidecode(values['name'])
        return super(my_module, self).create(values)

    def write(self, values):
        if 'name' in values:
            values['name'] = unidecode(values['name'])
        return super(my_module, self).write(values)

    @api.depends('value')
    def _value_pc(self):
         for record in self:
           record.value2 = float(record.value) / 100
