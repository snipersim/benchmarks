FROM snipersim/benchmarks:latest AS dockerhub
# Install a Sniper version from GitHub
ARG SNIPER_GIT_REPO=https://github.com/snipersim/snipersim
ARG SNIPER_GIT_TREEISH=d49d0b3e36899572b69dc1812bdfb6bc6cc00d47
ARG PINPLAY_DOWNLOAD=https://snipersim.org/packages/pinplay-dcfg-3.11-pin-3.11-97998-g7ecce2dac-gcc-linux.tar.bz2
# Tell Sniper to use Pin/Pinplay (instead of SDE) and allow the use of our own version
ARG USE_PINPLAY=1
# Let's Encrypt certificates aren't supported in Centos 6.x
ARG WGET_OPTIONS=--no-check-certificate
RUN git clone $SNIPER_GIT_REPO sniper && \
    cd sniper && \
    git checkout $SNIPER_GIT_TREEISH && \
    mkdir -p pin_kit && \
    wget --quiet $WGET_OPTIONS $PINPLAY_DOWNLOAD && \
    tar -x -f $(basename $PINPLAY_DOWNLOAD) --auto-compress --strip-components=1 -C pin_kit && \
    rm $(basename $PINPLAY_DOWNLOAD) && \
    make
