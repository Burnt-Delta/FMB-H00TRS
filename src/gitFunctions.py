# gitFunctions.py - provides git functionality
# Author: Burnt-Delta

import os
import jsonParsing as jp
from github import Github

class GitFunctions:
    # adds config info to class
    def __init__(self):
        # authorization
        self.uname, self.pat = jp.getAuth()

        # other config
        self.debugMode = True
        self.repoDir = "cd .. & cd repos"
        self.repoNames = self.getRepoNames()

        # print init
        print("Started git functions with following arguments:")
        self.printConfig()
        self.debug("DEBUG MODE")
        print("===============================================")

        # make sure repo dir exists
        status = os.system(self.repoDir)
        if status == 1:
            print("Creating directory 'repos'...")
            os.system("cd .. & mkdir repos")

    # prints the running config & stats
    def printConfig(self):
        print("Username: " + self.uname)
        print("PAT: " + self.pat)

        repoString = ""
        for repo_name in self.repoNames:
            repoString += (repo_name + ", ")
        repoString = repoString[:-2]

        print("Repos: " + repoString)

    # used just for internal logs, probably already deprecated tbh
    def getRepoNames(self):
        names = []
        g = Github(self.pat)

        for repo in g.get_user().get_repos():
            names.append(repo.name)

        return names

    # used by top-level script; refreshes local copies of repos
    def updateRepos(self, timeStamps):
        g = Github(self.pat)
        hasNew = False

        # if we already have timestamps, use them
        if timeStamps:
            self.debug("Found 'timeStamps'")
            for repo in g.get_user().get_repos():
                # If the repo either isn't yet tracked locally or isn't up to date, pull it
                if (not timeStamps[repo.name] or repo.pushed_at != timeStamps[repo.name]):
                    hasNew = True
                    timeStamps[repo.name] = repo.pushed_at
                    self.pullRepo(repo)
                # Otherwise, we're good
                else:
                    print("'" + repo.name + "' is up to date.")
        # Otherwise, attempt to pull every repo
        else:
            hasNew = True
            self.debug("'timeStamps' is empty!")
            for repo in g.get_user().get_repos():
                timeStamps[repo.name] = repo.pushed_at
                self.pullRepo(repo)

        return hasNew


    # pulls a repo given its API object
    def pullRepo(self, repo):
        name = repo.name
        base_url = repo.clone_url

        print("Pulling repo: " + name)
        print("-------" + len(name)*"-")
        
        status = os.system(self.repoDir + " & cd " + name)

        # if given repo does not exist locally
        if status == 1:
            print("Given repo \'" + name + "\' not found. Attempting to clone...")
            self.cloneRepo(base_url)

        os.system(self.repoDir + " & cd " + name + " & git pull & git status")
        print()

    # clones a repo given the clone URL
    def cloneRepo(self, url):
         # insert authentication in to clone url
         url_parts = base_url.split("github.com")
         url = url_parts[0] + self.uname + ":" + self.pat + "@github.com" + url_parts[1]
         
         os.system(self.repoDir + " & git clone " + url)

    # prints debug messages
    def debug(self, string):
        if self.debugMode:
            print("DEBUG: " + string)
