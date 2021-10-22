# Benchmarks for the [Sniper Multi-Core Simulator](https://snipersim.org)

[Sniper](https://snipersim.org) is a Multi-Core Simulator that can be used to simulate a variety of processor designs.
We designed this benchmarks repository to allow researchers to run applications in Sniper more easily by providing a unified
interface to run them.

Available Benchmarks:
* Splash-2
* Parsec 2.1
* NPB 3.3.1
* SPEC CPU2006 ([pinball support](http://snipersim.org/w/Pinballs) with [Pinplay 3.5 or older](https://www.intel.com/content/www/us/en/developer/articles/tool/program-recordreplay-toolkit.html), and local compilation support).

## Quick Start

The command below downloads the benchmarks repository, and builds and installs Sniper in a local [docker](https://www.docker.com) image.
[This image](https://hub.docker.com/u/snipersim) is downloaded from Docker Hub with the commands below.
The source for generating these images [is available as well](https://github.com/snipersim/benchmarks/tree/main/tools/docker).

```
# Register to download Sniper at https://snipersim.org/w/Download
export SNIPER_GIT_REPO=https://path-to-snipers-git-repo-from-the-email
git clone https://github.com/snipersim/benchmarks
cd benchmarks/tools/docker
make # Downloads the docker image with pre-compiled benchmarks, compiles Sniper and starts the docker image
cd benchmarks
./run-sniper -p splash2-fft # "-i test -n 1" are default options
```

## benchmarks/run-sniper options

* `-p suitename-benchmarkname` (required): suite (splash2, parsec) and name (fft, blackscholes, ...) of the benchmark
* `-n numcores` (optional): number of threads to run. Note that this is the total number of threads that will run (equal to the number of available cores in the simulated machine). For Parsec, this means that the -n passed to the benchmark is usually lower since many Parsec programs start additional helper threads or use multiple threads per requested core.
* `-i inputsize` (optional): input set name. Usually test, small and large are available, as defined in our [IISWC 2011](http://snipersim.org/w/Paper:Iiswc2011Heirman) paper.
* `--benchmarks=suitename-benchmarkname-inputsize-numcores[,sn-bn-is-nc]+`: Run one or more benchmarks simultaneously
* `-c`, `-g`, `-s`: passes the configuration file, option or script name to sniper/run-sniper unmodified

## Other Benchmark Compilation Options

This suite has been tested with CentOS 6, and all docker images are compiled using that image as a base.
If you'd like, there are also options to compile the benchmarks manually (using `cd benchmarks; make`), 
using a passthrough Docker container (with `cd benchmarks/tools/docker; make runpassthrough`) which stores the compiled binaries in your current directory,
and the source to build the Docker Hub image (`cd benchmarks/tools/docker; make runhub`).
