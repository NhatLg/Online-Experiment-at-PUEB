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

# Not used since it won't work with dynamic language translation
# def make_emo_field(label):
#     return models.IntegerField(
#         choices=[1, 2, 3, 4, 5],
#         label=_(label),
#         widget=widgets.RadioSelect,
#     )

class Constants(BaseConstants):
    name_in_url = 'presurvey'
    players_per_group = None
    num_rounds = 1
    translated_languages = ('en', 'pl')
    err_msg_percent = _("The numbers must add up to 100")


class Subsession(BaseSubsession):
    def creating_session(self):
        assert self.session.config.get('language', 'en') \
               in Constants.translated_languages, TRNSL_ERR_MSG


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    subjectID = models.StringField(label=False)

    panasUps = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Upset"), widget=widgets.RadioSelect)
    panasHos = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Hostile"), widget=widgets.RadioSelect)
    panasAle = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Alert"), widget=widgets.RadioSelect)
    panasAsh = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Ashamed"), widget=widgets.RadioSelect)
    panasIns = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Inspired"), widget=widgets.RadioSelect)
    panasNer = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Nervous"), widget=widgets.RadioSelect)
    panasDet = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Determined"), widget=widgets.RadioSelect)
    panasAtt = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Attentive"), widget=widgets.RadioSelect)
    panasAfr = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Afraid"), widget=widgets.RadioSelect)
    panasAct = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Active"), widget=widgets.RadioSelect)
    # ppanas_q1 = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Interested"), widget=widgets.RadioSelect)
    # panasDis = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Distressed"), widget=widgets.RadioSelect)
    # panasExc = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Excited"), widget=widgets.RadioSelect)
    # ppanas_q5 = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Strong"), widget=widgets.RadioSelect)
    # ppanas_q6 = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Guilty"), widget=widgets.RadioSelect)
    # panasSca = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Scared"), widget=widgets.RadioSelect)
    # panasEnt = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Enthusiastic"), widget=widgets.RadioSelect)
    # ppanas_q10 = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Proud"), widget=widgets.RadioSelect)
    # ppanas_q11 = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Irritable"), widget=widgets.RadioSelect)    
    # ppanas_q18 = models.IntegerField(choices=[1, 2, 3, 4, 5], label=_("Jittery"), widget=widgets.RadioSelect)

    disI = models.FloatField(label="I")
    disII = models.FloatField(label="II")
    disIII = models.FloatField(label="III")
    disIV = models.FloatField(label="IV")
    
    subjectPhase = models.IntegerField(label=_('What phase of study are you currently in?'),
                                       choices=[
                                            (0, _('Bachelor')), 
                                            (1, _('Master')),
                                            (2, _('PhD')),
                                            (3, _('Others')),
                                        ])
    # subjectProgram = models.StringField(label=_('What is your study program'))
    subjectIsVote = models.BooleanField(label=_("Did you vote in the last election for the student council?"),
                                        choices=[
                                            (True, _("Yes")),
                                            (False, _("No"))
                                        ])
    subjectGender = models.IntegerField(label=_("What is your gender?"),
                                        choices=[
                                            (0, _("Male")),
                                            (1, _("Female")),
                                            (2, _("Diverse")),
                                        ])
    subjectAge = models.IntegerField(label=_("What is your age?"))
    subjectNativeLang = models.StringField(label=_("What is your mother tongue?"))
    subjectIsWorkToStudy = models.BooleanField(label=_("Do you work to fund your study?"),
                                               choices=[
                                                   (True, _("Yes")),
                                                   (False, _("No"))
                                               ])
    
    subjectAttiKant = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], label=False,
                                          widget=widgets.RadioSelectHorizontal)
    subjectAttiTrustOther = models.IntegerField(choices=[1, 2, 3, 4], label=_("Other people"), 
                                                widget=widgets.RadioSelectHorizontal)
    # subjectAttiTrustAdmin = models.IntegerField(choices=[1, 2, 3, 4], label=_("University council"), 
    #                                             widget=widgets.RadioSelectHorizontal)
    subjectAttiTrustCouncil = models.IntegerField(choices=[1, 2, 3, 4], label=_("Student council"), 
                                                  widget=widgets.RadioSelectHorizontal)
    


