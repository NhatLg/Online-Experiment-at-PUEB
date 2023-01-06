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
    voteOptions = [  (0, _('A presentation by Marek Zmysłowski, Polish-born entrepreneur and co-founder of Rocket Internet, RTB House, OLX and GLOVO and author of the bestseller "Chasing Black Unicorns.')),
                     (1, _('Access to a collection of important standard textbooks as ebooks accessible to all students when logged in to the university WiFi.')),
                     (2, _('A number of scholarships (600-800 Zloty per student) for study abroad or internship abroad outside of funded programs (so-called free mover).')),
                     (3, _('Financial support of selected Study Circles to support their activities, among others publications and conferences.')),
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
            p.isCouncilTreatment = 1 if p in self.get_group_matrix()[1] else 0
            p.isPresidentTreatment = 1 if p in self.get_group_matrix()[2] else 0


class Group(BaseGroup):
    isTie = models.BooleanField()
    voteResult1 = models.IntegerField()
    voteResult2 = models.IntegerField()

    def first_tie_check(self):
        players_vote_treatment = self.subsession.get_group_matrix()[0]
        vote_result = dict()
        for p in players_vote_treatment:
            vote_result[p.treatment_vote] = vote_result.get(p.treatment_vote, 0) + 1
        vote_result.pop(99, None) #delete counts of white vote (which is coded as 99)
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
        max_value = max(vote_result.values())
        most_voted = [key for key, value in vote_result.items() if value == max_value]
        # if tie, break the tie with random choice
        if len(most_voted) != 1:
            self.voteResult2 = random.sample(most_voted, 1) + 1
        else:
            self.voteResult2 = most_voted[0] + 1

class Player(BasePlayer):
    treatment_vote = models.IntegerField(label=False,
                                         choices=Constants.voteOptions, initial=99)

    treatment_vote2 = models.IntegerField(label=False,
                                         choices=Constants.voteOptions, initial=99)
    isVoteTreatment = models.BooleanField()
    isCouncilTreatment = models.BooleanField()
    isPresidentTreatment = models.BooleanField()