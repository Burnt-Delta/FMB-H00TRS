# FMB.py - the main server script
# Author: Burnt-Delta

import gitFunctions
import time

if __name__ == '__main__':
    # starts git functionality
    gf = gitFunctions.GitFunctions() # please don't make fun of my object name

    while True:
        # pulls or clones every repo on the list every 12 hours
        gf.pullRepos()
        time.sleep(43200)