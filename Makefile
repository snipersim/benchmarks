ifeq ($(BENCHMARKS_ROOT),)
$(error "Error: The BENCHMARKS_ROOT environment variable is not set.")
endif

# Set both SNIPER_ROOT and GRAPHITE_ROOT
# SNIPER_ROOT has priority over GRAPHITE_ROOT
ifeq ($(SNIPER_ROOT),)
ifeq ($(GRAPHITE_ROOT),)
$(error "Error: Either the SNIPER_ROOT or GRAPHITE_ROOT environment variable must be set.")
else
SNIPER_ROOT=$(GRAPHITE_ROOT)
export SNIPER_ROOT
endif
else
GRAPHITE_ROOT=$(SNIPER_ROOT)
export GRAPHITE_ROOT
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
