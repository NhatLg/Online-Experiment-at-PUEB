from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from django.utils import translation

class TransMixin:
    def get_context_data(self, **context):
        user_language = self.session.config.get('language', 'en')
        translation.activate(user_language)
        return super().get_context_data(**context)

class aPanas(TransMixin, Page):
    form_model = 'player'
    form_fields = [
        'pPanasDis',
        'pPanasExc',
        'pPanasUps',
        'pPanasSca',
        'pPanasEnt',
        'pPanasAle',
        'pPanasIns',
        'pPanasNer',
        'pPanasDet',
        'pPanasAfr',
        # 'ppanas_q11',
        # 'ppanas_q12',
        # 'ppanas_q13',
        # 'ppanas_q14',
        # 'ppanas_q15',
        # 'ppanas_q16',
        # 'ppanas_q17',
        # 'ppanas_q18',
        # 'ppanas_q19',
        # 'ppanas_q20',
    ]

class bAcceptance(TransMixin, Page):
    form_model = 'player'
    form_fields = ["subjectAcceptance"]


class WaitPage(TransMixin, WaitPage):
    pass



page_sequence = [aPanas, bAcceptance]
