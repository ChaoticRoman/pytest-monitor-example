FROM ubuntu:20.04

RUN apt-get update \
    && apt-get install -y python3-pip time nano \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install pytest-memray

COPY tests /opt/pytest-monitor-example/tests

WORKDIR /opt/pytest-monitor-example/

CMD ["pytest", "--memray", "tests"]
