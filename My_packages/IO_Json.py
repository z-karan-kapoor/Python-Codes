class IO:
    def __init__(self,path,data=None):
        self.data=data
        self.path=path

    def readJson(self):
        with open(self.path,'r+') as file:
            print(file.read())

    
def TestIO(path):
    obj=IO(path)
    obj.readJson()

# TestIO("Desktop/PyPackages/data/sample.json")