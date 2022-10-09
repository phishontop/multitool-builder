import requests
import pathlib


class Github:
    
    def __init__(self, repos, name):
        self.name = name
        self.skids = self.getSkids()
        self.repos = self.parseRepos(repos)
    
    def getSkids(self):
        response = requests.get("https://raw.githubusercontent.com/phishontop/multitool-builder/main/skid-list.txt")
        return response.text.split("\n")
    
    def getCode(self, repo):
        raw = repo.replace("https://github.com", "https://raw.githubusercontent.com")
        response = requests.get(f"{raw}/main/main.py")
        return response.text
    
    def parseRepos(self, repos):
        newRepos = []
        for repo in repos:
            if repo.split("/")[3] not in self.skids:
                newRepos.append(repo)

        return newRepos
    
    def saveCode(self):
        for repo in self.repos:
            code = self.getCode(repo)
            repoName = f'{repo.split("/")[3]}-{repo.split("/")[4]}'
            pathlib.Path(rf"./results/{self.name}/tools/").mkdir(parents=True, exist_ok=True)
            with open(rf"./results/{self.name}/tools/{repoName}.py", "w+") as file:
                file.write(code)