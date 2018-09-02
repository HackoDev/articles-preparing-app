CURRENT_PATH=$(shell pwd)

build:
	docker build -t articles --build-arg UUID=$$(id -u $$USER) .

run:
	docker run --name articles -itd -v $(CURRENT_PATH)/src:/app articles