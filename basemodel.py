import os
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base

# BUG with MSSQL Connection String for NVARCHAR data
# https://stackoverflow.com/questions/8890427/pyodbc-freetds-unixodbc-on-debian-linux-issues-with-tds-version
os.environ["TDSVER"] = "8.0"  # DO NOT REMOVE

MSSQL_CONN_STRING = (
    "mssql+pyodbc://{0}:{1}@{2}:{3}/{4}?driver=FreeTDS&odbc_options='TDS_Version=8.0'"
)
db_url = MSSQL_CONN_STRING.format(
    'sa', 'Your_password123', 'localhost', '1433', 'ASRMAdmin'
)
connect_args = {"check_same_thread": False}
engine = create_engine(
    db_url, connect_args=connect_args, pool_size=20, max_overflow=0
)

Base = automap_base()

# reflect the tables
AdminBase = Base.prepare(autoload_with=engine)
