DOCKERLOCAL_IMAGE=benchmarks-$(USER):latest
DOCKERHUB_IMAGE=snipersim/benchmarks:latest

DOCKERHUB_DIR:=$(dir $(realpath $(lastword $(MAKEFILE_LIST))))
SNIPER_ROOT=$(DOCKERHUB_DIR)/sniper
export SNIPER_ROOT

ifeq ($(SNIPER_GIT_REPO),)
$(error Please set your SNIPER_GIT_REPO directory)
endif

run: build
	docker run --rm -it $(DOCKERLOCAL_IMAGE)

build: Dockerfile
	docker build -f ./Dockerfile --build-arg SNIPER_GIT_REPO=$(SNIPER_GIT_REPO) -t $(DOCKERLOCAL_IMAGE) .

runhub: buildhub
	docker run --rm -it benchmarks-local-$(USER):latest

push: buildhub
	docker push snipersim/benchmarks-builder:latest
	docker push snipersim/benchmarks:latest

buildhub: Dockerfile.dockerhub
	docker build -f ./Dockerfile.dockerhub --target builder -t snipersim/benchmarks-builder:latest .
	docker build -f ./Dockerfile.dockerhub --target runner -t snipersim/benchmarks:latest .
	docker build -f ./Dockerfile.dockerhub --target localrunner --build-arg SNIPER_GIT_REPO=$(SNIPER_GIT_REPO) -t benchmarks-local-$(USER):latest .

.PHONY: run build runhub push buildhub
