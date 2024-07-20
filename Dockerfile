FROM alpine:latest

RUN apk add --no-cache python3 py3-psutil

COPY serve.py /serve.py

EXPOSE 80

ENTRYPOINT ["/serve.py"]
