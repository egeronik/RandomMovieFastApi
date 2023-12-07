FROM python:3.11.7-slim-bullseye

WORKDIR /app
COPY * /app

EXPOSE 80

RUN ls

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

