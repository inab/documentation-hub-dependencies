from Methods import Methods

default = [{
    "repoUrl": "",
    "description": ""
}]


class DependencyFile(Methods):
    def __init__(self, repoid, name, owner, licenseInfo, repositoryTopics, dependencies=default):
        self.repoid = repoid
        self.name = name
        self.owner = owner
        self.licenseInfo = licenseInfo
        self.repositoryTopics = repositoryTopics
        self.dependencies = dependencies
