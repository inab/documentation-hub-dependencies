import requests
from DependencyFile import DependencyFile
from ErrorFile import ErrorFile

# github api
URL = 'https://api.github.com/graphql'


class GitHubDataFetcher:
    def __init__(self, owner, repository, token):
        self.owner = owner
        self.repository = repository
        self.token = token

    # http post requests
    def run_query(self, query, headers):
        request = requests.post(
            URL, json={'query': query}, headers=headers)
        if request.status_code == 200:
            return request.json()
        else:
            raise Exception("Query failed to run by returning code of {}. {}".format(
                request.status_code, query))

    # get info
    def getInfo(self):
        print("Creating JSON File "+self.repository)

        # github token
        hearders = {"Authorization": "Bearer "+self.token}

        # create query. For the sake of sanaty reasons the topic limit is set to first 100 topics
        query = """
                {
                    repository(name: \"%s\" , owner: \"%s\" ) {
                        id
                        name
                        owner {
                            login
                            url
                        }
                        licenseInfo {
                            name
                        }
                        repositoryTopics(first: %d) {
                            edges {
                                node {
                                    topic {
                                        name
                                    }
                                }
                            }
                        }
                    }
                }
                """ % (self.repository, self.owner, 100)

        res = self.run_query(query, hearders)

        if('errors' in res):
            print("Error in creating file, please read the output file")
            msg = res['errors']
            e = ErrorFile(msg)
            return e
        elif('data' in res):
            repoid = res['data']['repository']['id']
            name = res['data']['repository']['name']
            owner = res['data']['repository']['owner']
            licenseInfo = res['data']['repository']['licenseInfo']
            topics = res['data']['repository']['repositoryTopics']['edges']
            repositoryTopics = []
            for node in topics:
                for key in node:
                    repositoryTopics.append(node[key]['topic']['name'])
            # create dependecy object
            d = DependencyFile(repoid, name, owner,
                               licenseInfo, repositoryTopics)
            return d
        else:
            msg = "Something went wrong"
            e = ErrorFile(msg)
            return e
