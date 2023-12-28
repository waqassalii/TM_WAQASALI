# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TaskManagerTask(models.Model):
    _name = 'task.manager.task'
    _description = 'Task Management'

    title = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    deadline = fields.Date(string='Deadline')
    completed = fields.Boolean(string='Completed', default=False)
    state = fields.Selection([
        ('pending', 'Pending'),
        ('complete', 'Completed'),
        ('delay', 'Delayed'),
        ('cancel', 'Cancelled'),
    ], string="status", default='pending',copy=False,)

    deadline_days = fields.Integer(string='Days Left', compute='_compute_deadline_days')

    @api.depends('deadline')
    def _compute_deadline_days(self):
        for rec in self:
            today = fields.Date.today()
            if rec.deadline:
                rec.deadline_days = int((rec.deadline - today).days)
            else:
                rec.deadline_days = 0

    def action_pending(self):
        self.state = 'pending'
        self.completed = False

    def action_complete(self):
        self.state = 'complete'
        self.completed = True

    def action_cancel(self):
        self.state = 'cancel'
        self.completed = False
