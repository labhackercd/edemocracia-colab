from decouple import config

name = 'colab_audiencias'
verbose_name = 'Colab Audiencias Plugin Plugin'

upstream = 'http://audienciasweb:8000/audiencias/'
api_key = config('AUDIENCIAS_API_KEY')

urls = {
    'include': 'colab_audiencias.urls',
    'prefix': '^audiencias/',
    'login': '/audiencas/accounts/login/',
}
