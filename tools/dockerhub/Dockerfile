FROM snipersim/benchmarks:latest AS dockerhub
# Install your Sniper version
ARG SNIPER_GIT_REPO
ARG PINPLAY_DOWNLOAD=https://snipersim.org/packages_public/pinplay-drdebug-3.7-pin-3.7-97619-g0d0c92f4f-gcc-linux.tar.bz2
RUN git clone $SNIPER_GIT_REPO sniper && \
    mkdir -p sniper/pin_kit && \
    cd sniper && \
    wget --no-check-certificate $PINPLAY_DOWNLOAD && \
    tar -x -f $(basename $PINPLAY_DOWNLOAD) --auto-compress --strip-components=1 -C pin_kit && \
    rm $(basename $PINPLAY_DOWNLOAD) && \
    make
