#!/usr/bin/env bash
set -m
./opt/mssql/bin/sqlservr & ./init-mssql.sh
fg
