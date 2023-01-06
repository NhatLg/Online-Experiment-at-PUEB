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
    name_in_url = 'postsurvey'
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

    ppanasUps = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Upset"), widget=widgets.RadioSelect)
    ppanasHos = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Hostile"), widget=widgets.RadioSelect)
    ppanasAle = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Alert"), widget=widgets.RadioSelect)
    ppanasAsh = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Ashamed"), widget=widgets.RadioSelect)
    ppanasIns = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Inspired"), widget=widgets.RadioSelect)
    ppanasNer = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Nervous"), widget=widgets.RadioSelect)
    ppanasDet = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Determined"), widget=widgets.RadioSelect)
    ppanasAtt = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Attentive"), widget=widgets.RadioSelect)
    ppanasAfr = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Afraid"), widget=widgets.RadioSelect)
    ppanasAct = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Active"), widget=widgets.RadioSelect)

    subjectAcceptance = models.IntegerField(label=False,choices=[1,2,3,4,5,6,7,8,9,10], widget=widgets.RadioSelect)


