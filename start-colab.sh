#!/bin/bash

cp ./misc/etc/colab/plugins.d/audiencias.py /etc/colab/plugins.d/
cp ./misc/etc/colab/widgets.d/audiencias_widgets.py /etc/colab/widgets.d/

cp  ./misc/etc/colab/plugins.d/wikilegis.py /etc/colab/plugins.d/
cp ./misc/etc/colab/widgets.d/wikilegis_widgets.py /etc/colab/widgets.d/

colab-admin migrate
colab-admin initdb
colab-admin compress --force
colab-admin collectstatic --noinput
gunicorn colab.wsgi:application --config=/etc/colab/gunicorn.py