FROM python:3.9.6
ENV PYTHONNUNBUFFERED 1
RUN mkdir /config
ADD /config/requirements.pip /config
RUN pip install -r /config/requirements.pip
RUN mkdir /src;
WORKDIR /src
