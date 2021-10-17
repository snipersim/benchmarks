FROM snipersim/benchmarks:latest
# Install your Sniper version
ARG SNIPER_GIT_REPO
ARG PINPLAY_DOWNLOAD=https://snipersim.org/packages_public/pinplay-dcfg-3.11-pin-3.11-97998-g7ecce2dac-gcc-linux.tar.bz2
RUN git clone $SNIPER_GIT_REPO sniper && \
    mkdir -p sniper/pin_kit && \
    cd sniper && \
    wget --no-check-certificate $PINPLAY_DOWNLOAD && \
    tar -x -f $(basename $PINPLAY_DOWNLOAD) --auto-compress --strip-components=1 -C pin_kit && \
    rm $(basename $PINPLAY_DOWNLOAD) && \
    make
