FROM python:3.8-alpine

RUN pip install -U utrello

ENTRYPOINT [ "utrello" ]