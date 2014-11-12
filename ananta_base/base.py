from abc import ABCMeta, abstractmethod

class MiningProfile():

    def __init__(self,name,timestamp):
        self.name = name
        self.timestamp = timestamp
        self.trainingsets = []
        self.testsets = []
        self.profiles = []
        self.lastcheckpoint = 0


    def set(self,index, params):
        self.profiles[index].set(params)

    def execute(self, index):
        if(self.lastcheckpoint<=index):
            for i in range(self.lastcheckpoint,index+1):
                self.profiles[i].execute(self)
        else:
            for i in range(0,index+1):
                self.profiles[i].execute(self)
        self.lastcheckpoint += 1

    def show(self, index, params):
        self.profiles[index].show(params)


class Profile():
    __metaclass__ = ABCMeta

    @abstractmethod
    def set(self, params):
        print "Setting parameters in subprofile "

    @abstractmethod
    def execute(self, miningprofile):
        print "Executing subprofile "

    @abstractmethod
    def show(self, params):
        print "Showing stats in modified data"


class ParameterSet():
    def __init__(self):
        pass

class Step():
    def __init__(self):
        self.params = StepParameter()

class StepParameter():
    def __init__(self):
        pass



