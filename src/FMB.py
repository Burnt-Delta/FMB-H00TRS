# FMB.py - the main server script
# Author: Burnt-Delta

import gitFunctions
import time

# Time intervals for cloning
INTERVAL_INITIAL = 1    # (Hours) Initial interval to wait before retrying git
INTERVAL_MAX = 24       # (Hours) Maximum interval to wait before retrying git

# Saves local clones of remote repo
def startLocalClones(gf, times):
    interval = INTERVAL_INITIAL # number of hours to wait before retrying git
    hasNew = False

    while times > 0:
        hasNew = gf.updateRepos(timeStamps)

        # Reset the sleep interval if local was updated; otherwise, increment
        if hasNew:
            interval = INTERVAL_INITIAL
        else:
            if interval < INTERVAL_MAX:
                interval += 1

        # Sleep, decrement the test variable :)
        time.sleep(3600 * interval)
        times -= 1

# FMB-H00TRS INIT
if __name__ == '__main__':
    #### GIT ####
    gf = gitFunctions.GitFunctions() # please don't make fun of my object name
    timeStamps = {} # used to check if we should pull a repo         
    times = 2 # debug

    # Get local clones
    startLocalClones(gf, times)


