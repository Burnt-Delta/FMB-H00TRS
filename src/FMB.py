# FMB.py - the main server script
# Author: Burnt-Delta

import gitFunctions
import time

if __name__ == '__main__':
    gf = gitFunctions.GitFunctions() # please don't make fun of my object name
    timeStamps = {} # used to check if we should pull a repo         
    times = 2 # debug

    while times > 0:
        gf.updateRepos(timeStamps)
        times -= 1
