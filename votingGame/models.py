from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
from django.utils.translation import ugettext_lazy as _
import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'votinggame'
    players_per_group = None
    num_rounds = 1
    translated_languages = ('en', 'pl')
    voteOptions = [  (0, _("Additional funds for the annual competition for the best master's or bachelor's thesis")),
                     (1, _('Scholarships (800-1000 Zloty per student) for study or internships abroad')),
                     (2, _('Online Access to important standard textbooks via university WiFi')),
                     (3, _('Financial support for selected Study Circles ')),
                     (99, _('White vote')),
                    ]

class Subsession(BaseSubsession):
    def do_my_shuffle(self):
        all_players = self.get_players()
        random.shuffle(all_players)
        group_matrix = [all_players[i::3] for i in range(3)]

        self.set_group_matrix(group_matrix)
        for p in all_players:
            p.isVoteTreatment = 1 if p in self.get_group_matrix()[0] else 0
            p.isDictatorTreatment = 1 if p in self.get_group_matrix()[1] else 0
            p.isPresidentTreatment = 1 if p in self.get_group_matrix()[2] else 0


class Group(BaseGroup):
    isTie = models.BooleanField()
    voteResult1 = models.IntegerField() # not off by 1
    voteResult2 = models.IntegerField() # not off by 1
    proposalResult = models.IntegerField() #to record the randomly selected dictator result (not off by 1)

    def first_tie_check(self):
        players_vote_treatment = self.subsession.get_group_matrix()[0]
        vote_result = dict()
        for p in players_vote_treatment:
            vote_result[p.treatment_vote] = vote_result.get(p.treatment_vote, 0) + 1
        vote_result.pop(99, None) #delete counts of white vote (which is coded as 99)
        if not vote_result: raise Exception("Everyone vote blanc")
        max_value = max(vote_result.values())
        most_voted = [key for key, value in vote_result.items() if value == max_value]
        # record if there is a tie
        if len(most_voted) != 1:
            self.isTie = True
            self.voteResult1 = 0
        else:
            self.voteResult1 = most_voted[0] + 1

    def second_tie_check(self):
        players_vote_treatment = self.subsession.get_group_matrix()[0]
        vote_result = dict()
        for p in players_vote_treatment:
            vote_result[p.treatment_vote2] = vote_result.get(p.treatment_vote2, 0) + 1
        vote_result.pop(99, None)  # delete counts of white vote (which is coded as 99)
        if not vote_result: raise Exception("Everyone vote blanc")
        max_value = max(vote_result.values())
        most_voted = [key for key, value in vote_result.items() if value == max_value]
        # if tie, break the tie with random choice
        if len(most_voted) != 1:
            self.voteResult2 = random.sample(most_voted, 1) + 1
        else:
            self.voteResult2 = most_voted[0] + 1

    def select_dictator_result(self):
        players_dictator_treatment = self.subsession.get_group_matrix()[1]
        dictator_candidates = []
        for player in players_dictator_treatment:
            proposalResult = player.tDictatorProposal + 1
            if proposalResult != 100:
                dictator_candidates.append(player)

        if dictator_candidates:
            dictator = random.choice(dictator_candidates)
            self.proposalResult = dictator.tDictatorProposal + 1
            for player in players_dictator_treatment:
                player.treatment_dictator_id = dictator.id_in_group
        else:
            raise Exception("All players vote blanc")


class Player(BasePlayer):
    treatment_vote = models.IntegerField(label=False,
                                         choices=Constants.voteOptions, initial=99, widget=widgets.RadioSelect)
    treatment_vote2 = models.IntegerField(label=False,
                                         choices=Constants.voteOptions, initial=99, widget=widgets.RadioSelect)
    tDictatorProposal = models.IntegerField(label=False,
                                         choices=Constants.voteOptions, initial=99, widget=widgets.RadioSelect)

    treatment_dictator_id = models.IntegerField() #to record who is the dictator
    isVoteTreatment = models.BooleanField()
    isDictatorTreatment = models.BooleanField()
    isPresidentTreatment = models.BooleanField()
    isLetTimeOut1 = models.BooleanField(initial=False)
    isLetTimeOut2 = models.BooleanField(initial=False)
    isLetTimeOutDic = models.BooleanField(initial=False)