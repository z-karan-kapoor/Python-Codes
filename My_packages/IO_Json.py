import json

class jsonIO:
    def __init__(self, path, data=None):  # constructor
        self.data = data
        self.path = path

    def readJson(self):  # function to read JSON file
        with open(self.path, 'r+') as file:
            print(json.load(file))


def testIO(path):          # function for testing
    obj = jsonIO(path)
    obj.readJson()

testIO("Desktop/PyPackages/data/sample.json")
