# FMB.py - the main server script
# Author: Burnt-Delta

import gitFunctions

if __name__ == '__main__':
    # starts git functionality
    gf = gitFunctions.GitFunctions() # please don't make fun of my object name

    # pulls or clones every repo on the list
    gf.pullRepos()