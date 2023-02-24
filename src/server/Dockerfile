# syntax=docker/dockerfile:1

FROM python:3.9-slim-buster
WORKDIR /app
COPY ./src/server/requirements.txt server/requirements.txt
RUN pip install -r server/requirements.txt
COPY . .
EXPOSE 8002
ENV FLASK_APP=server.py
CMD ["flask", "--app", "src/server/server:init_app(0)", "run", "--host=0.0.0.0", "--port=8002" ]

