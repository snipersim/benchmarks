FROM centos:6
# Fix main repos, from https://stackoverflow.com/a/29559374
RUN sed -i '/^mirrorlist/s/^/#/;/^#baseurl/{s/#//;s/mirror.centos.org\/centos\/$releasever/vault.centos.org\/6.10/}' /etc/yum.repos.d/*B*
# Install wget and install a new repository for the devtoolset-2 (gcc-4.8)
# Install repos for devtoolset-2
RUN yum update -y && \
    yum install -y \
      centos-release-scl \
      wget \ 
    && \
    wget --no-check-certificate http://people.centos.org/tru/devtools-2/devtools-2.repo -O /etc/yum.repos.d/devtools-2.repo && \
    yum clean all && \
    rm -rf /tmp/* /var/tmp/*
# Fix SCL repos, from https://stackoverflow.com/a/29559374
RUN sed -i '/^mirrorlist/s/^/#/;/^#baseurl/{s/#//;s/mirror.centos.org\/centos\/6/vault.centos.org\/6.10/}' /etc/yum.repos.d/*SCL*
RUN sed -i '/^mirrorlist/s/^/#/;/^# baseurl/{s/# //;s/mirror.centos.org\/centos\/6/vault.centos.org\/6.10/}' /etc/yum.repos.d/*SCL* 
# Install dependencies for LLVM, Sniper and Benchmarks, matplotlib, gcc-4.8 / devtoolset-2, gcc-7 / devtoolset-7
RUN yum update -y && \
    yum install -y \
      autoconf \
      automake \
      bison-devel \
      bison \
      boost-devel \
      bzip2-devel \
      cmake \
      curl-devel \
      devtoolset-2-gcc \
      devtoolset-2-gcc-gfortran \
      devtoolset-2-binutils \
      devtoolset-2-gcc-c++ \
      devtoolset-7-toolchain \
      devtoolset-7-gcc-gfortran \
      flex-devel \
      flex \
      freetype-devel \
      gcc-c++ \
      gettext \
      git \
      glibc-static \
      glibc.i686 \
      libpng-devel \
      libtool \
      libxslt \
      libX11-devel \
      libXext-devel \
      libXi-devel \
      libXmu-devel \
      libXt-devel \
      m4 \
      openssh-clients \
      openssl-devel \
      patch \
      perl-ExtUtils-MakeMaker \
      python-devel \
      redhat-lsb \
      scons \
      sqlite-devel \
      tar \
      which \
      zlib-devel \
      && \
    yum clean all && \
    rm -rf /tmp/* /var/tmp/*
# Install Python 2.7
RUN cd /tmp && \
    wget -O - https://www.python.org/ftp/python/2.7.10/Python-2.7.10.tgz | tar -x -f - -z && \
    cd Python-2.7.10 && \
    ./configure --prefix=/usr/local && \
    make install && \
    cd / && \
    rm -rf /tmp/* /var/tmp/*
# Install Git 2.5.0
RUN cd /tmp && \
    wget --no-check-certificate -O - https://www.kernel.org/pub/software/scm/git/git-2.5.0.tar.gz | tar -x -f - -z && \
    cd git-2.5.0 && \
    ./configure --prefix=/usr/local && \
    make all install && \
    cd / && \
    rm -rf /tmp/* /var/tmp/*
# Add Python and Git to the path
ENV PATH /usr/local/bin/:$PATH
# Setup the user in your environment
ARG USER
ARG GROUP
ARG UID
ARG GID
# Add a new group just in case it is needed
RUN groupadd --gid $GID --non-unique "${GROUP}-docker"
RUN useradd --create-home -s /bin/bash --uid $UID --gid "${GROUP}-docker" $USER
# Enable gcc-4.8 as the default
ENV PATH /opt/rh/devtoolset-2/root/usr/bin/:$PATH
# Enable gcc-7 as the default
#ENV PATH /opt/rh/devtoolset-7/root/usr/bin/:$PATH
