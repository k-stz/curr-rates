FROM python:3.10.5-alpine AS builder

COPY ./requirements.txt /app/requirements.txt

RUN python3 -m venv /app/venv && . /app/venv/bin/activate && python3 -m pip --no-cache-dir install -r /app/requirements.txt
COPY flask /app/

FROM python:3.10.5-alpine
COPY --from=builder /app /app

ENV PATH="/app/venv/bin:$PATH"

CMD [ "python3", "/app/app.py" ]