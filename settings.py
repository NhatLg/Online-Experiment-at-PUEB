from os import environ

SESSION_CONFIGS = [
    {
        'name': 'presurvey_en',
        'display_name': "PUEB-English",
        'num_demo_participants': 4,
        'app_sequence': ['presurvey', 'votingGame', 'postsurvey', 'mindgame'],
        'language':'en'
    },
    {
        'name': 'presurvey_pl',
        'display_name': "PUEB-Polish",
        'num_demo_participants': 4,
        'app_sequence': ['presurvey', 'votingGame', 'postsurvey', 'mindgame'],
        'language': 'pl'
    },
]

ROOMS = [
    dict(
        name='pilot',
        display_name='PUEB Econ Waiting Room 0',
        participant_label_file='_rooms/pilot.txt',
        use_secure_urls=False
    ),
    dict(
        name='session1',
        display_name='PUEB Econ Waiting Room 1',
        participant_label_file='_rooms/session1.txt',
        use_secure_urls=False
    ),
    dict(
        name='session2',
        display_name='PUEB Econ Waiting Room 2',
        participant_label_file='_rooms/session2.txt',
        use_secure_urls=False
    ),
    dict(
        name='session3',
        display_name='PUEB Econ Waiting Room 3',
        participant_label_file='_rooms/session3.txt',
        use_secure_urls=False
    ),
    dict(
        name='session4',
        display_name='PUEB Econ Waiting Room 4',
        participant_label_file='_rooms/session4.txt',
        use_secure_urls=False
    ),
    dict(
        name='session5',
        display_name='PUEB Econ Waiting Room 5',
        participant_label_file='_rooms/session5.txt',
        use_secure_urls=False
    ),
    dict(
        name='session6',
        display_name='PUEB Econ Waiting Room 6',
        participant_label_file='_rooms/session6.txt',
        use_secure_urls=False
    ),
    dict(
        name='session7',
        display_name='PUEB Econ Waiting Room 7',
        participant_label_file='_rooms/session7.txt',
        use_secure_urls=False
    ),
    dict(
        name='session8',
        display_name='PUEB Econ Waiting Room 8',
        participant_label_file='_rooms/session8.txt',
        use_secure_urls=False
    ),
    dict(
        name='session9',
        display_name='PUEB Econ Waiting Room 9',
        participant_label_file='_rooms/session9.txt',
        use_secure_urls=False
    ),
    dict(
        name='session10',
        display_name='PUEB Econ Waiting Room 10',
        participant_label_file='_rooms/session10.txt',
        use_secure_urls=False
    ),
    dict(
        name='session11',
        display_name='PUEB Econ Waiting Room 11',
        participant_label_file='_rooms/session11.txt',
        use_secure_urls=False
    )
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

LANGUAGE_SESSION_KEY = '_language'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '9wkeawebi!n92by+l^k=ljhjqlylr)j0bxq*t(qextnubod%h7'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
