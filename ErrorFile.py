import json


class ErrorFile:
    def __init__(self, message):
        self.message = message

    def toJson(self, filename):
        with open(filename, 'w') as outfile:
            return json.dump(self.__dict__, outfile)
