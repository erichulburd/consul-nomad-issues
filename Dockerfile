FROM python:3.9-alpine

WORKDIR /app

ADD src .

CMD ["python", "-m", "http.server", "8080"]
