FROM python:3.13-alpine3.20

ENV PYTHONUNBUFFERED=1
ENV PATH="/py/bin:$PATH"

COPY ./cohort_management/requirements.txt /tmp/requirements.txt
COPY ./cohort_management /cohort_management
WORKDIR /cohort_management
EXPOSE 8000

ARG DEV=false
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip &&\
    apk add --update --no-cache postgresql-dev && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base python3-dev && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser -D --no-create-home docker-user && \
    chown -R docker-user:docker-user /cohort_management

USER docker-user

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
