import sys, os, time, getopt, subprocess, tempfile


abspath = lambda d: os.path.abspath(os.path.join(d))

HOME = abspath(os.path.dirname(__file__))

__allbenchmarks = None

def allbenchmarks():
  global __allbenchmarks
  if not __allbenchmarks:
    benchmarks = subprocess.Popen([ '%(HOME)s/parsec-2.1/bin/parsecmgmt' % globals(), '-a', 'info' ], stdout = subprocess.PIPE).communicate()
    benchmarks = [ line[15:].split(' ')[0] for line in benchmarks[0].split('\n') if line.startswith('[PARSEC]     - ') and (line.endswith(' (apps)') or line.endswith(' (kernels)')) ]
    __allbenchmarks = sorted(benchmarks)
  return __allbenchmarks


def allinputs():
  return [ f[:-8] for f in os.listdir('%(HOME)s/parsec-2.1/config' % globals()) if f.endswith('.runconf') ]



def log2(n):
  log2n = -1
  while n:
    n >>= 1
    log2n += 1
  return log2n



class Program:

  def __init__(self, program, nthreads, inputsize, benchmark_options = []):
    if program not in allbenchmarks():
      raise ValueError("Invalid benchmark %s" % program)
    if inputsize not in allinputs():
      if inputsize in ('small', 'large'):
        inputsize = 'sim' + inputsize
      else:
        raise ValueError("Invalid input size %s" % inputsize)
    self.program = program
    self.nthreads = nthreads
    self.inputsize = inputsize
    if program in ('freqmine',):
      self.openmp = True
    else:
      self.openmp = False
    # do the tests in self.ncores, and fail early if we're called with an unsupported (program, nthreads, inputsize) combination
    self.ncores()


  def ncores(self):
    if self.program == 'blackscholes':
      ncores = self.nthreads - 1
    elif self.program == 'bodytrack':
      ncores = self.nthreads - 2
    elif self.program == 'facesim':
      if self.nthreads not in (1, 2, 3, 4, 6, 8, 16, 32, 64, 128):
        raise ValueError("Benchmark %s does not support this number of cores" % self.program)
      ncores = self.nthreads
    elif self.program == 'ferret':
      ncores = (self.nthreads - 2) / 4
    elif self.program == 'fluidanimate':
      # ncores must be power of two, one master thread will be added
      ncores = 1 << log2(self.nthreads - 1)
    elif self.program == 'swaptions':
      ncores = self.nthreads - 1
    elif self.program == 'canneal':
      ncores = self.nthreads - 1
    elif self.program == 'raytrace':
      ncores = self.nthreads - 1
    elif self.program == 'dedup':
      ncores = self.nthreads / 4
    elif self.program == 'streamcluster':
      ncores = self.nthreads - 1
    elif self.program == 'vips':
      ncores = self.nthreads - 2
    else:
      ncores = self.nthreads

    if ncores < 1:
      raise ValueError("Benchmark %s needs more cores" % self.program)

    return ncores


  def run(self, graphitecmd):
    flags = []
    rundir = tempfile.mkdtemp()
    if self.openmp:
      os.putenv('OMP_NUM_THREADS', str(self.ncores()))
    proc = subprocess.Popen([ '%s/parsec-2.1/bin/parsecmgmt' % HOME,
                         '-a', 'run', '-p', self.program, '-c', 'gcc-sniper', '-i', self.inputsize, '-n', str(self.ncores()),
                         '-s', graphitecmd, '-d', rundir
                     ] + flags)
    proc.communicate()

    os.system('rm -r %(rundir)s' % locals())
    return proc.returncode

  def rungraphiteoptions(self):
    return ''
