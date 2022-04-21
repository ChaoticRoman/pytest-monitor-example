IMAGE = pytest-monitor-example

build:
	docker build -t $(IMAGE) .

DOCKER_RUN_BASE_CMD = docker run -it --rm $(IMAGE)

test: build
	$(DOCKER_RUN_BASE_CMD) ./testit

interactive: build
	$(DOCKER_RUN_BASE_CMD) bash
