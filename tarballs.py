#!/usr/bin/python3

import os
import re

DIR = 'content/releases'

versions = []
for n in os.listdir(DIR):
    g = re.match('^dulwich-(.*).tar.gz$', n)
    if not g:
        continue
    versions.append(g.group(1))

def version_key(s):
    return list(map(int, s.split('.')))

for version in sorted(versions, key=version_key, reverse=True):
    filename = "dulwich-" + version + ".tar.gz"
    v = {"version": version, "filename": filename}
    sig_filename = os.path.join(DIR, filename + ".asc")
    if os.path.exists(sig_filename):
        v["signature_filename"] = sig_filename
    print("* `%(version)s <releases/%(filename)s>`_" % v, end='')
    if "signature_filename" in v:
        print(" (`%(version)s GPG signature <releases/%(signature_filename)s>`_)" % v,
              end='')
    print("")
