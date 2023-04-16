# FROM python:3.10-bullseye
FROM node:18-bullseye

# Required python environments
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

# The following command installs the required things in the image.
RUN apt dist-upgrade -y && \
    apt update -y && \
    apt install -y --no-install-recommends python3 python3-pip python3-dev\
    build-essential curl unzip wget git && \
    apt clean -y && \
    apt-get purge libpq-dev -y && apt-get autoremove -y && \
    rm /var/lib/apt/lists/* rm -rf /var/cache/apt/*

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip && pip3 install --no-cache-dir -r requirements.txt && pip3 cache purge

COPY . .