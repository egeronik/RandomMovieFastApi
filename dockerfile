FROM python:3.11.7-slim-bullseye

WORKDIR /app
COPY * /app

ARG YA_PORT

ENV YA_PORT=$PORT

RUN ls

RUN pip install -r requirements.txt

EXPOSE $YA_PORT

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", $YA_PORT]

