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
        "panasUps",
        "panasHos",
        "panasAle",
        "panasAsh",
        "panasIns",
        "panasNer",
        "panasDet",
        "panasAtt",
        "panasAfr",
        "panasAct",
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
