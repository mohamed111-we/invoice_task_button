from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class AccountMove(models.Model):
    _inherit = 'account.move'

    state = fields.Selection(selection_add=[
        ('draft', 'Draft'),
        ('first_confirm', 'First Confirm'),
        ('posted', 'Posted'),
        ('cancel', 'Cancelled')
    ], ondelete={'first_confirm': 'cascade'})

    def action_first_confirm(self):
        for move in self:
            if not move.line_ids.filtered(lambda line: line.display_type not in ('line_section', 'line_note')):
                raise ValidationError(_('You need to add a line before posting.'))
            move.state = 'first_confirm'