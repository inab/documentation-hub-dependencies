import json

default = [{
    "repoUrl": "",
    "description": ""
}]


class DependencyFile:
    def __init__(self, repoid, name, owner, licenseInfo, repositoryTopics, dependencies=default):
        self.repoid = repoid
        self.name = name
        self.owner = owner
        self.licenseInfo = licenseInfo
        self.repositoryTopics = repositoryTopics
        self.dependencies = dependencies

    def toJson(self, filename):

        with open(filename, 'w') as outfile:
            return json.dump(self.__dict__, outfile)
