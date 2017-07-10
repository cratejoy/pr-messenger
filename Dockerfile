FROM python:3.6.1-alpine

WORKDIR /usr/src/app
# COPY requirements.txt ./
COPY setup.py .
# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install .
COPY . .
ENTRYPOINT ["pr-messenger"]
