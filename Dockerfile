FROM python:3.6.1-alpine

WORKDIR /usr/src/app
ENV PYTHONPATH=/usr/src/app

COPY setup.py .
RUN pip install .
COPY . .

ENTRYPOINT ["pr-messenger"]
