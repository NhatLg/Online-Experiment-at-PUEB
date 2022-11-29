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

    ppanas_q1 = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Interested"), widget=widgets.RadioSelect)
    ppanas_q2 = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Distressed"), widget=widgets.RadioSelect)
    ppanas_q3 = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Excited"), widget=widgets.RadioSelect)
    ppanas_q4 = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Upset"), widget=widgets.RadioSelect)
    ppanas_q5 = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Strong"), widget=widgets.RadioSelect)
    ppanas_q6 = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Guilty"), widget=widgets.RadioSelect)
    ppanas_q7 = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Scared"), widget=widgets.RadioSelect)
    ppanas_q8 = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Hostile"), widget=widgets.RadioSelect)
    ppanas_q9 = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Enthusiastic"), widget=widgets.RadioSelect)
    ppanas_q10 = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Proud"), widget=widgets.RadioSelect)
    ppanas_q11 = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Irritable"), widget=widgets.RadioSelect)
    ppanas_q12 = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Alert"), widget=widgets.RadioSelect)
    ppanas_q13 = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Ashamed"), widget=widgets.RadioSelect)
    ppanas_q14 = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Inspired"), widget=widgets.RadioSelect)
    ppanas_q15 = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Nervous"), widget=widgets.RadioSelect)
    ppanas_q16 = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Determined"), widget=widgets.RadioSelect)
    ppanas_q17 = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Attentive"), widget=widgets.RadioSelect)
    ppanas_q18 = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Jittery"), widget=widgets.RadioSelect)
    ppanas_q19 = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Active"), widget=widgets.RadioSelect)
    ppanas_q20 = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Afraid"), widget=widgets.RadioSelect)

    subjectAcceptance = models.IntegerField(label=False,choices=[1,2,3,4,5,6,7,8,9,10], widget=widgets.RadioSelect)


