#!/bin/bash

# extracted from the docker-entrypoin.sh script from the official MariaDB container image

set -eo pipefail
shopt -s nullglob

source /usr/local/bin/docker-entrypoint.sh

if [[ -e "$DATADIR"/.my-healthcheck.cnf ]]; then
    exit 0
fi

healthCheckGrant=USAGE
healthCheckConnectPass="$(pwgen --numerals --capitalize --symbols --remove-chars="=#'\\" -1 32)"
healthCheckConnectPassEscaped=$( docker_sql_escape_string_literal "${healthCheckConnectPass}" )
if [ -n "$MARIADB_HEALTHCHECK_GRANTS" ]; then
    healthCheckGrant="$MARIADB_HEALTHCHECK_GRANTS"
fi
read -r -d '' healthCheckUser <<-EOSQL || true
CREATE USER healthcheck@'127.0.0.1' IDENTIFIED BY '$healthCheckConnectPassEscaped';
CREATE USER healthcheck@'::1' IDENTIFIED BY '$healthCheckConnectPassEscaped';
CREATE USER healthcheck@localhost IDENTIFIED BY '$healthCheckConnectPassEscaped';
GRANT $healthCheckGrant ON *.* TO healthcheck@'127.0.0.1';
GRANT $healthCheckGrant ON *.* TO healthcheck@'::1';
GRANT $healthCheckGrant ON *.* TO healthcheck@localhost;
EOSQL
maskPreserve=$(umask -p)
umask 0077
echo -e "[mariadb-client]\\nport=$PORT\\nsocket=$SOCKET\\nuser=healthcheck\\npassword=$healthCheckConnectPass\\nprotocol=tcp\\n" > "$DATADIR"/.my-healthcheck.cnf
$maskPreserve

docker_setup_env
docker_process_sql --dont-use-mysql-root-password --database=mysql --binary-mode <<-EOSQL
-- Securing system users shouldn't be replicated
SET @orig_sql_log_bin= @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN=0;
-- we need the SQL_MODE NO_BACKSLASH_ESCAPES mode to be clear for the password to be set
SET @@SESSION.SQL_MODE=REPLACE(@@SESSION.SQL_MODE, 'NO_BACKSLASH_ESCAPES', '');
${healthCheckUser}
EOSQL
