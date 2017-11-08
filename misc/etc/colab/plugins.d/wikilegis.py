from decouple import config

name = 'colab_wikilegis'
verbose_name = 'Colab Wikilegis Plugin Plugin'

upstream = 'http://wikilegisweb:8000/'

api_key = config('WIKILEGIS_API_KEY')

urls = {
    'include': 'colab_wikilegis.urls',
    'prefix': '^wikilegis/',
    'login': '/wikilegis/accounts/login/',
}

settings_variables = {
    'COLAB_STATICS': [
        '/usr/lib/python2.7/site-packages/colab_wikilegis/static'
    ]
}
