# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TaskManagerTask(models.Model):
    _name = 'task.manager.task'
    _description = 'Task Management'

    title = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    deadline = fields.Date(string='Deadline')
    completed = fields.Boolean(string='Completed', default=False)