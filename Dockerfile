FROM python:3.8-slim

RUN pip install -U pip

RUN pip install -U utrello

ENTRYPOINT [ "utrello" ]
