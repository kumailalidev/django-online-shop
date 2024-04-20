# pull official base image
FROM python:3.11.4-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
    # Additional dependencies
    && apt-get install -y netcat \
    # dependencies for building weasyprint python package
    && apt-get install -y libpango-1.0-0 \
    && apt-get install -y libpangoft2-1.0-0 \
    && apt-get install -y libpangocairo-1.0-0 \
    && apt-get install -y libharfbuzz0b \
    && apt-get install -y libcairo2 \
    # cleaning up unused files
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements ./requirements
RUN pip install -r requirements/development.txt

# copy scripts/dev/web/entrypoint.sh
COPY ./scripts/dev/web/entrypoint.sh /usr/src/app/scripts/dev/web/entrypoint.sh
RUN sed -i 's/\r$//g' /usr/src/app/scripts/dev/web/entrypoint.sh
RUN chmod +x /usr/src/app/scripts/dev/web/entrypoint.sh

# copy scripts/dev/web/start.sh
COPY ./scripts/dev/web/start.sh /usr/src/app/scripts/dev/web/start.sh
RUN sed -i 's/\r$//g' /usr/src/app/scripts/dev/web/start.sh
RUN chmod +x /usr/src/app/scripts/dev/web/start.sh

# copy scripts/dev/web/celery/worker/start.sh
COPY ./scripts/dev/web/celery/worker/start.sh /usr/src/app/scripts/dev/web/celery/worker/start.sh
RUN sed -i 's/\r$//g' /usr/src/app/scripts/dev/web/celery/worker/start.sh
RUN chmod +x /usr/src/app/scripts/dev/web/celery/worker/start.sh

# copy scripts/dev/web/celery/flower/start.sh
COPY ./scripts/dev/web/celery/flower/start.sh /usr/src/app/scripts/dev/web/celery/flower/start.sh
RUN sed -i 's/\r$//g' /usr/src/app/scripts/dev/web/celery/flower/start.sh
RUN chmod +x /usr/src/app/scripts/dev/web/celery/flower/start.sh

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/scripts/dev/web/entrypoint.sh"]
