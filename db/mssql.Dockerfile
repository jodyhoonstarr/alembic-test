FROM mcr.microsoft.com/mssql/server

USER root

ENV SA_PASSWORD Your_password123
ENV ACCEPT_EULA Y

RUN apt-get update -y \
    && apt-get install -y dos2unix \
    && apt-get install curl -y

# copy files into the container
COPY entrypoint-mssql.sh /entrypoint-mssql.sh
COPY init-mssql.sh asrmadmin.bak* /

# clean windows line endings
RUN dos2unix ./init-mssql.sh
RUN dos2unix ./entrypoint-mssql.sh

# start db and initialize
CMD ./entrypoint-mssql.sh
