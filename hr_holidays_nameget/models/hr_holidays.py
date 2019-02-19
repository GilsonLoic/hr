# -*- coding: utf-8 -*-
from openerp import models, api, _

import logging

_logger = logging.getLogger(__name__)


class HrHolidays(models.Model):
    _inherit = 'hr.holidays'

    @api.multi
    def name_get(self):
        result = []
        for holiday in self:
            result.append((holiday.id, _("%s (%s -> %s)") % (holiday.name, holiday.date_from, holiday.date_to)))
        return result