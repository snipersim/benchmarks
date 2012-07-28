#!/usr/bin/env python

import sys, os

# list of (packagename, filename)

DEPENDENCIES = [
  ('g++ / gcc-g++', '/usr/bin/g++'),
  ('m4', '/usr/bin/m4'),
]

ALTERNATIVES = [
  ('/usr/lib', '/usr/lib/x86_64-linux-gnu'),
  ('/usr/lib', '/usr/lib64'),
]

missing = False

def find_file(filename):
  if os.path.exists(filename):
    return True
  for pattern, replacement in ALTERNATIVES:
    if os.path.exists(filename.replace(pattern, replacement)):
      return True
  return False

for package, filename in DEPENDENCIES:
  if not find_file(filename):
    print '*** Please install package %s' % package
    missing = True


if missing:
  sys.exit(1)
else:
  sys.exit(0)
