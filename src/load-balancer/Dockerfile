# syntax=docker/dockerfile:1

FROM python:3.9-slim-buster
WORKDIR /app
COPY ./src/load-balancer/requirements.txt load-balancer/requirements.txt
RUN pip install -r load-balancer/requirements.txt
COPY . .
EXPOSE 8002
ENV FLASK_APP=main.py
CMD ["flask", "--app", "src/load-balancer/main", "run", "--host=0.0.0.0", "--port=8002" ]

