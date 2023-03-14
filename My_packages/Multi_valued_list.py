class Detector:
    def __init__(self, name="", list=[], dict={}):  # initialize
        self.name = name
        self.list = list
        self.dict = dict

    def search():  # search
        pass

    def save():  # save
        pass

    def delete():  # delete
        pass

    def __len__(self):  # len function
        Llen = len(self.list)
        Dlen = len(self.dict)
        print(f'list1 : {Llen}')
        print(f'dict1 : {Dlen}')
        return Llen+Dlen

    def __sum__(self):  # add function
        Lsum = sum(self.list)
        Dsum = sum(self.dict.values())
        print(f'list1 : {Lsum}')
        print(f'dict1 : {Dsum}')
        return Lsum+Dsum

    def __iter__(self):     #overrides __iter__() for compatibility
        self.nex = 0
        return self

    def __next__(self):     #overrides __next__() for compatibility
        if self.nex < len(self.list):
            result = self.list[self.nex]
            self.nex += 1
            return result
        else:
            raise StopIteration
