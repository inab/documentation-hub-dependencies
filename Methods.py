import json


class Methods:

    def toJson(self, filename):
        with open(filename, 'w') as outfile:
            return json.dump(self.__dict__, outfile)
