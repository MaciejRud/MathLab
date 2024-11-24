FROM python:3.13-alpine3.20

COPY backend/cohort_management /cohort_management
COPY backend/cohort_management/requirements.txt /tmp/requirements.txt
WORKDIR /cohort_management


RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip &&\
    apk add --update --no-cache postgresql-dev && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base python3-dev && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    apk del .tmp-build-deps


    CMD ["sh", "-c", "until pg_isready -h $DB_HOST -p 5432 -U $DB_USER; do echo 'Waiting for DB...'; sleep 1; done; \
    /py/bin/alembic -c /cohort_management/alembic.ini upgrade head"]