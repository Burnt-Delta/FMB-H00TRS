# gitFunctions.py - provides git functionality
# Author: Burnt-Delta
# TODO: add REST API functionality

import os
import jsonParsing as jp

class GitFunctions:
    # adds config info to class
    def __init__(self):
        # authorization
        self.uname, self.pat = jp.getAuth()

        # repos
        self.repoList = jp.getRepos()

        print("Started git functions with following arguments:")
        print("Username: " + self.uname)
        print("PAT: " + self.pat)

        # print all repo names
        output = "Repos: "
        for repo in self.repoList:
            output = output + repo['Repo'] + ', '
        output = output[:-2] # removes last comma
        print(output)
        print("===============================================")
    
    # attempts to pull or clone for each repo in list
    def pullRepos(self):
        repoDir = "cd .. & cd repos"
        status = os.system(repoDir)

        # create repos directory if it doesn't exist
        if status == 1:
            print("Creating directory 'repos'...")
            os.system("cd .. & mkdir repos")
        
        for repo in self.repoList:
            name = repo['Repo']
            base_url = repo['URL']

            print("Repo: " + name)

            status = os.system(repoDir + " & cd " + name)

            # if given repo does not exist locally
            if status == 1:
                print("Given repo \'" + name + "\' not found. Attempting to clone...")

                # insert authentication in to clone url
                url_parts = base_url.split("github.com")
                url = url_parts[0] + self.uname + ":" + self.pat + "@github.com" + url_parts[1]

                os.system(repoDir + " & git clone " + url)
            
            os.system(repoDir + " & cd " + name + " & git pull & git status")
            print()
