import requests

class Repository:
    def __init__(self, owner, repository, token):
        self.owner = owner
        self.repository = repository
        self.token = token

    def run_query(self,query,headers): # A simple function to use requests.post to make the API call. Note the json= section.
        request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
        if request.status_code == 200:
            return request.json()
        else:
            raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

    def createJsonFile(self):
        print("Creating JSON File "+self.repository)
        hearders = {"Authorization": "Bearer "+self.token}
        query = """
                {
                    repository(name: "uptime-chart-OEB", owner: "inab") {
                        id
                        name
                        owner {
                            login
                            url
                        }
                        licenseInfo {
                            name
                        }
                        repositoryTopics(first: 100) {
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
                """
        res = self.run_query(query,hearders);
        
        


    