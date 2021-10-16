FROM snipersim/benchmarks:latest
# Install your Sniper version
ARG SNIPER_GIT_REPO
RUN git clone $SNIPER_GIT_REPO sniper && make -C sniper
