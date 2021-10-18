include ../tools/scripts/env.makefile
export SPEC_PINBALLS_DIR:=$(BENCHMARKS_ROOT)/cpu2006_pinballs/pinballs

SPEC_PINBALLS_DOWNLOAD="http://snipersim.org/documents/pinballs/cpu2006-pinpoints-w0-d1B-m1.tar"

PINBALLS_DEP=$(SPEC_PINBALLS_DIR)/sphinx3/pinball_short.pp/pinball_t0r1_warmup3000_prolog0_region1000000023_epilog0_001_1-00000.0.result

$(PINBALLS_DEP):
	mkdir -p $(SPEC_PINBALLS_DIR)
	wget --no-check-certificate -O - $(SPEC_PINBALLS_DOWNLOAD) | tar --strip-components=1 -f - -x -C $(SPEC_PINBALLS_DIR)

compile: $(PINBALLS_DEP)

clean:
	rm -rf $(SPEC_PINBALLS_DIR)
