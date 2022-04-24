from __future__ import print_function
import os
print( os.getcwd() )
print( os.environ['PATH'] )

import sys
print( sys.version )

import subprocess
proc= subprocess.Popen(["sphinx-build","-b","html","source","build"])
proc.wait()