import sys, os, time, getopt, subprocess, tempfile, glob


abspath = lambda d: os.path.abspath(os.path.join(d))

HOME = abspath(os.path.dirname(__file__))
PINBALLS_DIR = os.path.join(HOME,'pinballs')

inputmap = {
  # test is not valid
  # train is not valid
  'ref': 'ref',
  # small is not valid
  # large is not valid
  'huge': 'ref',
}

def allbenchmarks():
  return map(os.path.basename, glob.glob(PINBALLS_DIR+"/*"))

def allinputs():
  return inputmap.keys()

# From https://stackoverflow.com/a/1724723
def find_all(name, path):
  result = []
  for root, dirs, files in os.walk(path):
    if name in files:
      result.append(os.path.join(root, name))
  return result

# From https://stackoverflow.com/a/2186673
import os, fnmatch
def find_files(directory, pattern):
  print 'finding dir=', directory, 'pat=', pattern
  for root, dirs, files in os.walk(directory):
    for basename in files:
      if fnmatch.fnmatch(basename, pattern):
        filename = os.path.join(root, basename)
        yield filename

class Program:

  def __init__(self, program, nthreads, inputsize, benchmark_options = []):
    if program not in allbenchmarks():
      raise ValueError("Invalid benchmark %s" % program)
    if inputsize not in allinputs():
      raise ValueError("Invalid input size %s" % inputsize)
    self.program = program
    self.nthreads = nthreads
    self.inputsize = inputmap[inputsize]
    pinball = list(find_files(os.path.join(PINBALLS_DIR, program), '*.address'))
    if len(pinball) == 0:
      print 'Error, unable to find pinballs. Run make in the cpu2006_pinballs directory to download them.'
      pinball = None
    elif len(pinball) > 1:
      print 'Warning, found multiple pinballs for', program, 'using first. :', pinball
      pinball = pinball[0]
    else:
      pinball = pinball[0]
    self.pinball = pinball


  def ncores(self):
    return self.nthreads


  def run(self, graphitecmd, postcmd = ''):
    rc = 1 # Indicate failure if there are any problems
    rc = run_bm(self.program, '', graphitecmd, env = '', postcmd = postcmd)
    return rc


  def rungraphiteoptions(self):
    return ('--pinballs=%s'%(self.pinball or '',))


def run(cmd):
  sys.stdout.flush()
  sys.stderr.flush()
  rc = os.system(cmd)
  rc >>= 8
  return rc

def run_bm(bm, cmd, submit, env, postcmd = ''):
  print '[CPU2006_PINBALLS]', '[========== Running benchmark', bm, '==========]'
  cmd = env + ' ' + submit + ' ' + cmd + ' ' + postcmd
  print '[CPU2006_PINBALLS]', 'Running \'' + cmd + '\':'
  print '[CPU2006_PINBALLS]', '[---------- Beginning of output ----------]'
  rc = run(cmd)
  print '[CPU2006_PINBALLS]', '[----------    End of output    ----------]'
  print '[CPU2006_PINBALLS]', 'Done.'
  return rc
