# Local build based on Docker Hub
DOCKERLOCAL_IMAGE=benchmarks-$(USER):latest
# Docker Hub recipes
DOCKERHUB_BUILDER_IMAGE=snipersim/benchmarks-builder:latest
DOCKERHUB_IMAGE=snipersim/benchmarks:latest
# Passthrough recipes
DOCKERBASE_IMAGE=benchmarks-basebuilder-$(USER):latest
DOCKERPASSTHROUGH_IMAGE=benchmarks-passthrough-$(USER):latest

DOCKERHUB_DIR:=$(dir $(realpath $(lastword $(MAKEFILE_LIST))))
SNIPER_ROOT=$(DOCKERHUB_DIR)/sniper
export SNIPER_ROOT

# QUICKSTART: Run 'make' to use the precompiled Docker Hub version of these benchmarks
#
# There are three seperate sets of builds in one Dockerfile
# First, there is the run/build targets, which use the compiled benchmarks pushed to Docker Hub.
#   This is the easiest way to get start.
# Next, there is the runhub/buildhub/push versions, which allow for running, building and pushing
#   the Docker Hub version. This is for maintenance of the version in Docker Hub.
# Finally, we have the runpassthrough/buildpassthrough versions, which allow for the automation of
#   building the benchmarks, but using the user's original directory as a base.

# Local build of Sniper based on the Docker Hub base image
run: build
	docker run --rm -it $(DOCKERLOCAL_IMAGE)

build: Dockerfile
ifndef SNIPER_GIT_REPO
	$(error Please set the SNIPER_GIT_REPO variable)
endif
	docker build -f ./Dockerfile --target dockerhub --build-arg SNIPER_GIT_REPO=$(SNIPER_GIT_REPO) -t $(DOCKERLOCAL_IMAGE) .

# Build recipe to generate the Docker Hub images
runhub: buildhub
	docker run --rm -it $(DOCKERHUB_IMAGE)

push: buildhub
	docker push $(DOCKERHUB_BUILDER_IMAGE)
	docker push $(DOCKERHUB_IMAGE)

buildhub: Dockerfile.dockerhub
	docker build -f ./Dockerfile.dockerhub --target builder -t $(DOCKERHUB_BUILDER_IMAGE) .
	docker build -f ./Dockerfile.dockerhub --target runner -t $(DOCKERHUB_IMAGE) .

# Build recipes for passthrough images (using local directories to store the benchmark and Sniper data)
runpassthrough: buildpassthrough
	docker run --rm -it -e HOME="${HOME}" -v "${HOME}:${HOME}" --user $(shell id -u):$(shell id -g) -w "${PWD}" $(DOCKERPASSTHROUGH_IMAGE)

buildpassthrough: Dockerfile.passthrough
	docker build -f ./Dockerfile.dockerhub --target basebuilder -t $(DOCKERBASE_IMAGE) .
	docker build -f ./Dockerfile.passthrough --target builderpassthrough --build-arg FROMLOCATION=$(DOCKERBASE_IMAGE) --build-arg UID=$(shell id -u) --build-arg GID=$(shell id -g) --build-arg USER="${USER}" --build-arg GROUP=$(shell id --group --name) -t $(DOCKERPASSTHROUGH_IMAGE) .

.PHONY: run build runhub push buildhub runpassthrough buildpassthrough
