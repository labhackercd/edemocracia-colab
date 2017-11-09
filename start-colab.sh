#!/bin/bash

PLUGINS_SETTINGS="/etc/colab/plugins.d/"
if [ "$(ls -A $PLUGINS_SETTINGS)" ]; then
    find $PLUGINS_SETTINGS ! -name 'edemocracia.py' -type f -exec rm -f {} +
fi

PLUGINS_WIDGETS="/etc/colab/widgets.d/"
if [ "$(ls -A $PLUGINS_WIDGETS)" ]; then
    rm /etc/colab/widgets.d/*
fi

activate_plugin() {
    PLUGIN_NAME=$1
    cp ./misc/etc/colab/plugins.d/${PLUGIN_NAME}.py /etc/colab/plugins.d/
    cp ./misc/etc/colab/widgets.d/${PLUGIN_NAME}_widgets.py /etc/colab/widgets.d/
    cp ./misc/etc/cron.d/colab-${PLUGIN_NAME} /etc/cron.d/
    crontab /etc/cron.d/colab-${PLUGIN_NAME}
}

[[ -z "${ENABLE_AUDIENCIAS}" ]] && ENABLE_AUDIENCIAS=2 || ENABLE_AUDIENCIAS="${ENABLE_AUDIENCIAS}"
[[ -z "${ENABLE_WIKILEGIS}" ]] && ENABLE_WIKILEGIS=2 || ENABLE_WIKILEGIS="${ENABLE_WIKILEGIS}"

if [[ "$ENABLE_WIKILEGIS" = true ]]; then
    activate_plugin wikilegis
fi

if [[ "$ENABLE_AUDIENCIAS" = true ]]; then
    activate_plugin audiencias
fi

crond
colab-admin migrate
colab-admin initdb
colab-admin compress --force
colab-admin collectstatic --noinput
gunicorn colab.wsgi:application --config=/etc/colab/gunicorn.py