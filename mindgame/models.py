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

author = 'Your name here'

doc = """
Your app description
"""

TRNSL_ERR_MSG = 'Translation for this language does not exist'



class Constants(BaseConstants):
    name_in_url = 'mindgame'
    players_per_group = None
    num_rounds = 1
    translated_languages = ('en', 'pl')


class Subsession(BaseSubsession):
    def creating_session(self):
        assert self.session.config.get('language', 'en') \
               in Constants.translated_languages, TRNSL_ERR_MSG


class Group(BaseGroup):
    pass

# Not used since it doesn't work with dynamic language translation
# def make_emo_field(label):
#     return models.IntegerField(
#         choices=[1, 2, 3, 4, 5],
#         label=_(label),
#         widget=widgets.RadioSelect,
#     )

class Player(BasePlayer):
    subjectIsWorkingCoin = models.BooleanField(label=False, choices = [
        (True, _("Yes")),
        (False, _("No"))
    ])

    subjectReport = models.IntegerField(label=False,
                                        choices=[
                                            (0,_("0 correct predictions - your contribution is 15 Zloty, you earn extra 0 Zloty")),
                                            (1,_("1 correct predictions - your contribution is 14 Zloty , you earn extra 1 Zloty")),
                                            (2,_("2 correct predictions - your contribution is 13 Zloty , you earn extra 2 Zloty")),
                                            (3,_("3 correct predictions - your contribution is 12 Zloty , you earn extra 3 Zloty")),
                                            (4,_("4 correct predictions - your contribution is 11 Zloty , you earn extra 4 Zloty")),
                                            (5,_("5 correct predictions - your contribution is 10 Zloty , you earn extra 5 Zloty")),
                                        ],
                                        widget=widgets.RadioSelect)

    subjectClickSeq = models.StringField()


