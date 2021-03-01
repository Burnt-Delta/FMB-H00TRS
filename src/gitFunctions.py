# gitFunctions.py - provides git functionality
# Author: Burnt-Delta
# TODO: add REST API functionality

import os
import jsonParsing as jp
from github import Github

class GitFunctions:
    # adds config info to class
    def __init__(self):
        # authorization
        self.uname, self.pat = jp.getAuth()

        # repos
        self.repoList = jp.getRepos()

        # explicit class members
        self.repoDir = "cd .. & cd repos"

        print("Started git functions with following arguments:")
        print("Username: " + self.uname)
        print("PAT: " + self.pat)

        # print all repo names
        output = "Repos: "
        for repo in self.repoList:
            output += repo['Repo'] + ', '
        output = output[:-2] # removes last comma
        print(output)
        print("===============================================")
    
    # attempts to pull or clone for each repo in list
    def pullRepos(self):
        status = os.system(self.repoDir)

        # create repos directory if it doesn't exist
        if status == 1:
            print("Creating directory 'repos'...")
            os.system("cd .. & mkdir repos")
        
        for repo in self.repoList:
            self.pullRepo(repo)

    def gitREST(self, timeStamps):
        g = Github(self.PAT)

        if timeStamps:
            for repo in g.get_user().get_repos():
                if (repo.pushed_at != timeStamps[repo.name]):
                    for listRepo in self.repoList:
                        # If the repo is found in our tracked list
                        if listRepo['Repo'] == repo.name:
                            print("Pulling changes for " + repo.name + "...")
                            self.pullRepo(repo)
                            break

                timeStamps[repo.name] = repo.pushed_at
        else:
            self.pullRepos()
            for repo in g.get_user().get_repos():
                timeStamps[repo.name] = repo.pushed_at
                print("Name: " + repo.name)
                print("Last Pushed: " + str(timeStamps[repo.name]) + "\n")

        return timeStamps

    def pullRepo(self, repo):
        name = repo['Repo']
        base_url = repo['URL']

        print("Repo: " + name)
            
        if name == 'FMB-H00TRS':
            os.system("cd .. & git pull & git status")
        else:
            status = os.system(self.repoDir + " & cd " + name)

            # if given repo does not exist locally
            if status == 1:
                print("Given repo \'" + name + "\' not found. Attempting to clone...")

                # insert authentication in to clone url
                url_parts = base_url.split("github.com")
                url = url_parts[0] + self.uname + ":" + self.pat + "@github.com" + url_parts[1]

                os.system(self.repoDir + " & git clone " + url)

            os.system(self.repoDir + " & cd " + name + " & git pull & git status")
            print()

