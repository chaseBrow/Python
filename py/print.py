# import subprocess
# lpr =  subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
# lpr.stdin.write(b"test")

import os
os.system('lp -o landscape "label.label"')
