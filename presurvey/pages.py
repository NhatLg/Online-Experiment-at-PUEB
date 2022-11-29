from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from django.utils import translation

class TransMixin:
    def get_context_data(self, **context):
        user_language = self.session.config.get('language', 'en')
        translation.activate(user_language)
        return super().get_context_data(**context)

class aWelcome(TransMixin, Page):
    pass

class bIdRequest(TransMixin, Page):
    form_model = 'player'
    form_fields = ['subjectID']

class cPanas(TransMixin, Page):
    form_model = 'player'
    form_fields = [
        'panas_q1',
        'panas_q2',
        'panas_q3',
        'panas_q4',
        'panas_q5',
        'panas_q6',
        'panas_q7',
        'panas_q8',
        'panas_q9',
        'panas_q10',
        'panas_q11',
        'panas_q12',
        'panas_q13',
        'panas_q14',
        'panas_q15',
        'panas_q16',
        'panas_q17',
        'panas_q18',
        'panas_q19',
        'panas_q20',
    ]
    
class dHypoEx1(TransMixin, Page):
    form_model = 'player'
    form_fields = ['disI', 'disII', 'disIII', 'disIV']

    def error_message(self, values):
        if values['disI'] + values['disII'] + values['disIII'] + values['disIV'] != 100:
            return Constants.err_msg_percent

class ePersonalData(TransMixin, Page):
    form_model = 'player'
    form_fields = ["subjectPhase", "subjectProgram", "subjectIsVote",
                   "subjectGender", "subjectAge", "subjectNativeLang",
                   "subjectIsWorkToStudy"]

class fAttitudes(TransMixin, Page):
    form_model = 'player'
    form_fields = ["subjectAttiKant", "subjectAttiTrustOther", "subjectAttiTrustAdmin", "subjectAttiTrustCouncil"]


class WaitPage(TransMixin, WaitPage):
    pass



page_sequence = [aWelcome, bIdRequest, cPanas, dHypoEx1, ePersonalData, fAttitudes]
