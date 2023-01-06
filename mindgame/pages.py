from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from django.utils import translation

class TransMixin:
    def get_context_data(self, **context):
        user_language = self.session.config.get('language', 'en')
        translation.activate(user_language)
        return super().get_context_data(**context)

class a0TestCoin(TransMixin, Page):
    form_model = 'player'
    form_fields = ["subjectIsWorkingCoin"]
   
class aInstructions(TransMixin, Page):
   def vars_for_template(self):
       return dict(
           last_vote_result = self.participant.vars["vote_str_result"],
       )
   
class bDecision(TransMixin, Page):
    form_model = 'player'
    form_fields = [
        "subjectReport",
        "subjectClickSeq"
    ]

    def vars_for_template(self):
        return dict(
            last_vote_result=self.participant.vars["vote_str_result"],
        )

    def is_displayed(self):
        return self.player.subjectIsWorkingCoin

class bDecisionText(TransMixin, Page):
    form_model = 'player'
    form_fields = [
        "subjectReport",
        "subjectClickSeq"
    ]

    def vars_for_template(self):
        return dict(
            last_vote_result=self.participant.vars["vote_str_result"],
        )

    def is_displayed(self):
        return not self.player.subjectIsWorkingCoin

class cClosing(TransMixin, Page):
    pass

class WaitPage(TransMixin, WaitPage):
    pass



page_sequence = [a0TestCoin, aInstructions, bDecision, bDecisionText, cClosing]
