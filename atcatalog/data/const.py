'''
Module holding constant definitions
'''
from os.path import expanduser

ATC_HOME = expanduser('~') + u'/workspace/'
# Database
DATA_PATH = ATC_HOME + u'atcatalog/data/'
DB_PREFIX = u'sqlite:///'
DB_PATH = DATA_PATH
DB_FILE = u'atcdb.db'
DB_URI = DB_PREFIX + DB_PATH + DB_FILE

# Users
IMAGE = u'file:///static/images/male.png'
MALE_IMAGE = u'file:///static/images/male.png'
FEMALE_IMAGE = u'file:///static/images/female.png'

# Languages
DEFAULT_LANGUAGE = u'en_US'
LANG_DICT = { u'bg_BG' : u'Bulgarian',
              u'cs_CZ' : u'Czech',
              u'de_DE' : u'German',
              u'dk_DK' : u'Danish',
              u'el_GR' : u'Greek',
              u'en_AU' : u'English (Australia)',
              u'en_CA' : u'English (Canada)',
              u'en_GB' : u'English (Great Britain)',
              u'en_US' : u'English (United States)',
              u'es_ES' : u'Spanish (Spain)',
              u'es_MX' : u'Spanish (Mexico)',
              u'fa_IR' : u'Persian (Iran)',
              u'fi_FI' : u'Finnish',
              u'fr_FR' : u'French',
              u'hi_IN' : u'Hindi',
              u'it_IT' : u'Italian',
              u'ja_JP' : u'Japanese',
              u'ko_KR' : u'Korean',
              u'lt_LT' : u'Lithuanian',
              u'lv_LV' : u'Latvian',
              u'ne_NP' : u'Nepali',
              u'nl_NL' : u'Dutch (Netherlands)',
              u'no_NO' : u'Norwegian',
              u'pl_PL' : u'Polish',
              u'pt_BR' : u'Portuguese (Brazil)',
              u'pt_PT' : u'Portuguese (Portugal)',
              u'ru_RU' : u'Russian',
              u'sl_SI' : u'Slovene',
              u'sv_SE' : u'Swedish',
              u'tr_TR' : u'Turkish',
              u'zh_CN' : u'Chinese (China)',
              u'zh_TW' : u'Chinese (Taiwan)' }

# Sentences
AUDIO_DUMMY = u'file:///static/audio/dummy.mp3'

# Storage
LANGUAGE_FILE = u'languages.csv'
USER_FILE = u'users.csv'
SENTENCE_FILE = u'sentences.csv'

# Generated data
LANG_NUM = 10
USER_NUM = 10
SENTENCE_NUM = 100
DEFAULT_PROBABILITY = 0.