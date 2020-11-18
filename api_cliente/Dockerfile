FROM ubuntu:18.04

WORKDIR /app

ARG ENV=base
ARG TIMEZONE='America/Sao_Paulo'

# Setting Timezone
ENV TIMEZONE=$TIMEZONE

RUN echo $TIMEZONE > /etc/timezone && \
    apt-get update && apt-get install -y tzdata netcat && \
    rm /etc/localtime && \
    ln -snf /usr/share/zoneinfo/$TIMEZONE /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata && \
    apt-get clean

# Setting Locale - pt_BR.utf8
RUN apt-get update && apt-get install --no-install-recommends -y locales && rm -rf /var/lib/apt/lists/*
RUN localedef -c -f UTF-8 -i pt_BR pt_BR.UTF-8

# Install pip
RUN apt-get update \
    && apt-get install -y python3-pip python3-dev \
    && cd /usr/local/bin \
    && ln -s /usr/bin/python3 python \
    && pip3 install --upgrade pip


# Install Requirements
COPY ./requirements/$ENV.txt .

RUN pip3 --no-cache-dir install -r ./$ENV.txt
