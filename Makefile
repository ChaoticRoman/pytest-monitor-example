build:
	docker build -t pytest-monitor-example .

test: build
	docker run -it pytest-monitor-example pytest-3 .
