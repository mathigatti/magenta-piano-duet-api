FROM python:3.7.3-slim-stretch

RUN apt-get -y update && apt-get -y install gcc && apt-get -y install build-essential && apt-get -y install libsndfile1-dev

WORKDIR /
COPY model /model
COPY requirements.txt /

RUN pip3 install --upgrade pip
RUN pip3 --no-cache-dir install -r requirements.txt
COPY *.py /

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENTRYPOINT ["python3", "-X", "utf8", "server.py"]

