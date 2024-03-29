# pull base image
FROM python:3.12.2-slim-bullseye

# set enviromental varable
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONDONTWRITECODE=1
ENV PYTHONUNBUFFERED=1

# set working dir 
WORKDIR /code

# installing depentency
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .



