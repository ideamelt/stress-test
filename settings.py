import urllib

# IdeaMelt API settings
API_URL = 'https://api.ideamelt.com/v1/'
API_KEY_QP = '?api_key='
API_KEY = 'testing' # IM api key

# ECHO API settings
ECHO_API_URL = "http://api.echoenabled.com/v1/search?q=childrenof:"
ECHO_CLIENT_URL = urllib.quote_plus('http://www.stocial.com/')
ECHO_DATATYPE_URL = urllib.quote_plus('im-notifications/')
ECHO_APP_KEY_QP = '&appkey=prod.fuseconcepts' # Echo api key

# Common settings
BASE_USER_URL = 'http://www.test.com/'
USER_MAX = 1000 # Max number of testable users (DO NOT CHANGE THIS VALUE)
USER_LIST = range(1, USER_MAX + 1)

# Submit stress test
NOTIFICATIONS_MAX_USERS = 10 # each user will receive at least this many notifications
NOTIFICATIONS_MIN_USERS = 200 # each user will receive at most this many notifications
NOTIFICATIONS_TIMEOUT = 0 # how long to wait before sending the next batch

# Stress test settings
SEARCH_TOTAL_TIME = 20 # seconds
SEARCH_INTERVAL_TIME = 5 # seconds
USERS_TO_TEST = 5 # you can stress test a random sample users set in USER_MAX (must be less than USER_MAX)