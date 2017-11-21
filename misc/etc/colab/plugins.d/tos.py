# -*- coding: utf-8 -*-

name = 'colab_mkdocs_tos'
verbose_name = 'Colab Mkdocs Plugin Plugin'

upstream = ''

docs_title = "Sobre"

pages = [
    ('Página Inicial', 'index.md'),
    ('Wikilegis', 'wikilegis.md'),
    ('Audiências Interativas', 'audiencias.md'),
    ('Expressão', 'expressao.md'),
    ('Termos de Serviço', 'tos.md'),
]


urls = {
    'include': 'colab_mkdocs_tos.urls',
    'prefix': '^sobre/',
}