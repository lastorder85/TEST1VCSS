import sys
import os
cwd = os.getcwd()
sys.path.append(cwd)

from generate_list import printIT
for num in range(0,1000):
    printIT()
