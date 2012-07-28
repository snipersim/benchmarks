ifeq ($(BENCHMARKS_ROOT),)
$(error "Error: The BENCHMARKS_ROOT environment variable is not set.")
endif

ifeq ($(GRAPHITE_ROOT),)
$(error "Error: The GRAPHITE_ROOT environment variable is not set.")
endif

.PHONY: all clean dependencies

all: dependencies
	make -C tools/hooks
	make -C splash2
	make -C parsec
	make -C local

clean:
	make -C tools/hooks clean
	make -C splash2 clean
	make -C parsec clean
	make -C local clean

dependencies:
	$(BENCHMARKS_ROOT)/tools/scripts/checkdependencies.py
