# FMB.py - the main server script
# Author: Burnt-Delta

import gitFunctions
import time

if __name__ == '__main__2':
    # starts git functionality
    gf = gitFunctions.GitFunctions() # please don't make fun of my object name

    while True:
        # pulls or clones every repo on the list every 12 hours
        gf.pullRepos()
        time.sleep(43200) # TODO: once API's hooked up, have this increment depending on if pull had a change

if __name__ == '__main__':
    gf = gitFunctions.GitFunctions()
    timeStamps = {}
    times = 2

    while times > 0:
        gf.gitREST(timeStamps)
        times -= 1
