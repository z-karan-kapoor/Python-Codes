from multiprocessing import Process


class mProcess(object):  # Class for MultiProcessing
    def __init__(self, func, args, procs):  # Constructor
        self.func = func
        self.args = args
        self.procs = procs

    def run(self):  # Run Processes
        procs = []

        # Divide Tasks over number of Processes
        tmp = int(len(self.args)/self.procs)
        tmplist = [self.args[i:i+tmp] for i in range(0, len(self.args), tmp)]

        for i in tmplist:
            proc = Process(target=self.func, args=(i,))  # Allocate Process
            procs.append(proc)
            proc.start()  # Starts Process

        for proc in procs:
            proc.join()  # Joins Process


def fun(nums=[]):  # Function to square List elements
    ls = []
    [ls.append(i ** 2) for i in nums]
    print (ls)


if __name__ == '__main__':  # Main function
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    procs = 3
    obj = mProcess(fun, nums, procs)
    obj.run()
