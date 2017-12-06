from decouple import config

name = 'colab_discourse'
verbose_name = 'Colab Discourse Plugin Plugin'

upstream = 'http://discourse:8080/expressao/'
api_key = config('DISCOURSE_API_KEY')
api_username = config('DISCOURSE_API_USERNAME')
sso_secret = config('DISCOURSE_SSO_SECRET')

urls = {
    'include': 'colab_discourse.urls',
    'prefix': '^expressao/',
    'login': '/expressao/accounts/login/',
}

settings_variables = {
    'COLAB_STATICS': [
        '/usr/lib/python2.7/site-packages/colab_discourse/static'
    ]
}
