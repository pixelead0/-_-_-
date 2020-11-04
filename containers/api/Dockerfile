FROM python:3.8
RUN mkdir /api
WORKDIR /api

RUN apt-get update
RUN apt-get -y install gettext libgettextpo-dev
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y locales
RUN sed -i -e 's/# es_MX.UTF-8 UTF-8/es_MX.UTF-8 UTF-8/' /etc/locale.gen
RUN dpkg-reconfigure --frontend=noninteractive locales
RUN update-locale LANG=es_MX.UTF-8

ENV LANG es_MX.UTF-8
ENV LANGUAGE es_MX.UTF-8
ENV LC_ALL es_MX.UTF-8

COPY ./containers/api/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY ./containers/api/wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh
CMD ["sh entrypoint.sh"]
