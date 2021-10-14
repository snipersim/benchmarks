DOCKER_IMAGE=centos:6-gcc-7-benchmarks-$(USER)

run: build
	docker run --rm -it -e HOME="${HOME}" -v "${HOME}:${HOME}" --user $(shell id -u):$(shell id -g) -w "${PWD}" $(DOCKER_IMAGE)

build: Dockerfile
	docker build --build-arg UID=$(shell id -u) --build-arg GID=$(shell id -g) --build-arg USER="${USER}" -t $(DOCKER_IMAGE) .

.PHONY: run build
