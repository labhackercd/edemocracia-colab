#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE DATABASE colab OWNER root;
    CREATE DATABASE audiencias OWNER root;
    CREATE DATABASE wikilegis OWNER root;
EOSQL
