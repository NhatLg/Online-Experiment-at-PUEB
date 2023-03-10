from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from django.utils import translation
from django.utils.translation import ugettext_lazy as _

class TransMixin:
    def get_context_data(self, **context):
        user_language = self.session.config.get('language', 'en')
        translation.activate(user_language)
        return super().get_context_data(**context)

class aIntro(TransMixin, Page):
    pass

class bWaitPageShuffle(TransMixin, WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = 'do_my_shuffle'
    title_text = _("Waiting for other players")
    body_text = _("waiting for other players to get ready before splitting into groups...")
    
class cTreatmentVote(TransMixin, Page):
    form_model='player'
    form_fields=['treatment_vote']
    timeout_seconds = 90

    def is_displayed(self):
        return self.player.isVoteTreatment

    def before_next_page(self):
        if self.timeout_happened:
            self.player.treatment_vote = 99
            self.player.isLetTimeOut1 = True


class cWaitPageTieCheck(TransMixin, WaitPage):
    after_all_players_arrive = 'first_tie_check'
    title_text = _("Waiting for other players")
    body_text = _("waiting for other players and calculate voting result...")

    def is_displayed(self):
        return self.player.isVoteTreatment

class cVoteResult(TransMixin, Page):
    def vars_for_template(self):
        return dict(
            vote_final_result=self.group.voteResult1,
            vote_final_result_label = Constants.voteOptions[self.group.voteResult1 - 1][1]
        )
    def is_displayed(self):
        return self.player.isVoteTreatment

    def before_next_page(self):
        self.participant.vars["vote_str_result"] =  Constants.voteOptions[self.group.voteResult1 - 1][1]

class cTreatmentVote2(TransMixin, Page):
    form_model='player'
    form_fields=['treatment_vote2']
    timeout_seconds = 90
    
    def is_displayed(self):
        return (self.player.isVoteTreatment) and (self.group.isTie)

    def before_next_page(self):
        if self.timeout_happened:
            self.player.treatment_vote2 = 99
            self.player.isLetTimeOut2 = True

class cWaitPageTieCheck2(TransMixin, WaitPage):
    after_all_players_arrive = 'second_tie_check'
    title_text = _("Waiting for other players")
    body_text = _("waiting for other players and calculate voting result...")
    
    def is_displayed(self):
        return (self.player.isVoteTreatment) and (self.group.isTie)

class cVoteResult2(TransMixin, Page):
    
    def vars_for_template(self):
        return dict(
            vote_final_result=self.group.voteResult2,
            vote_final_result_label = Constants.voteOptions[self.group.voteResult2 - 1][1]
        )
    
    def is_displayed(self):
        return (self.player.isVoteTreatment) and (self.group.isTie)

    def before_next_page(self):
        self.participant.vars["vote_str_result"] =  Constants.voteOptions[self.group.voteResult2 - 1][1]

class dTreatmentPresident(TransMixin, Page):

    def is_displayed(self):
        return self.player.isPresidentTreatment

    def before_next_page(self):
        self.participant.vars["vote_str_result"] =  Constants.voteOptions[3 - 1][1] #voting result starts from 1 not 0

class eTreatmentDictator(TransMixin, Page):
    form_model='player'
    form_fields=['tDictatorProposal']
    timeout_seconds = 90
    
    def is_displayed(self):
        return self.player.isDictatorTreatment
    
    def before_next_page(self):
        if self.timeout_happened:
            self.player.treatment_dictator = 99
            self.player.isLetTimeOutDic = True

class eWaitPageDictator(TransMixin, WaitPage):
    after_all_players_arrive = 'select_dictator_result'
    title_text = _("Waiting for other players")
    body_text = _("waiting for other players before randomly selecting a proposal...")

    def is_displayed(self):
        return self.player.isDictatorTreatment
    
class eTreatmentDictatorResult(TransMixin, Page):

    def vars_for_template(self):
        return dict(
            vote_final_result=self.group.proposalResult,
            vote_final_result_label = Constants.voteOptions[self.group.proposalResult - 1][1]
        )

    def before_next_page(self):
        self.participant.vars["vote_str_result"] =  Constants.voteOptions[self.group.proposalResult - 1][1]
        
    def is_displayed(self):
        return self.player.isDictatorTreatment

page_sequence = [aIntro, bWaitPageShuffle, 
                 cTreatmentVote, cWaitPageTieCheck, cVoteResult,
                 cTreatmentVote2, cWaitPageTieCheck2, cVoteResult2,
                 dTreatmentPresident,
                 eTreatmentDictator, eWaitPageDictator, eTreatmentDictatorResult,
                ]
