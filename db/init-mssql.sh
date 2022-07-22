#!/usr/bin/env bash

# load baks
load_db_from_bak() {
  local db=${1}
  local bak=${2}

  echo "sa password: $SA_PASSWORD"

  # create the database
  /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P $SA_PASSWORD -q "
      CREATE DATABASE [${db}];
      GO"

  # load the database
  /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P $SA_PASSWORD -q "
      ALTER DATABASE [${db}]
      SET SINGLE_USER WITH ROLLBACK IMMEDIATE
      RESTORE DATABASE [${db}]
      FROM  DISK = N'/${bak}'
      WITH  FILE = 1,
      MOVE N'${db}' TO N'/var/opt/mssql/${db}.mdf',
      MOVE N'${db}_log' TO N'/var/opt/mssql/${db}.ldf',
      NOUNLOAD,
      REPLACE,
      STATS = 5
      ALTER DATABASE [${db}] SET MULTI_USER
      GO"
}

sleep 20

if [[ $LOAD_DB_BAK == "true" ]]; then

    echo ""
    echo "Creating DB ASRMAdmin..."
    echo ""
    load_db_from_bak ASRMAdmin asrmadmin.bak
fi

echo ""
echo "Database is ready."
echo ""

