# syntax=docker/dockerfile:1

FROM python:3.9-slim-buster
WORKDIR /app
COPY ./src/server/requirements.txt app/server/requirements.txt
RUN pip install -r app/server/requirements.txt
COPY . .
EXPOSE 8002
ENV SERVER=server.py
CMD ["flask", "--app", "src/server/server:init_app(1)","run", "--host=0.0.0.0", "--port=8002" ]

