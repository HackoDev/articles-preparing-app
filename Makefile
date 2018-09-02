CURRENT_PATH=$(shell pwd)

build:
	docker build -t articles .

run:
	docker run --name articles -itd -v $(CURRENT_PATH)/src:/app articles