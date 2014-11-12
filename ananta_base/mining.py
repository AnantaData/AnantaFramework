from abc import ABCMeta, abstractmethod
import pandas as pd

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


class FileLoadingProfile(Profile):

    def set(self, paramset):
        print "Setting parameters in file loading subprofile "
        self.paramset = paramset

    def execute(self, miningprofile):
        print "Executing file loading subprofile "
        # Get class from globals and create an instance
        m = globals()['FileLoadingProfile']()
        for step in self.paramset.steps:
            func = getattr(m, step.type)
            func(step.params,miningprofile)

    def show(self, params):
        print "Showing stats in loaded files"

    #

    def file_load(self,params,miningprofile):
        print "loading file", params
        dataset = None
        if(params.filetype=="csv"):
            dataset = pd.read_csv(params.filepath)
        elif(params.filetype=="xls"):
            dataset = pd.read_excel(params.filepath)
        if(params.loadto =="trainingset"):
            miningprofile.trainingsets.insert(params.loadindex, dataset)
        elif(params.loadto =="testset"):
            miningprofile.testsets[params.loadindex] = dataset


class ParameterSet:
    def __init__(self):
        pass

class Step:
    def __init__(self):
        self.params = StepParameter()

class StepParameter:
    def __init__(self):
        pass

class DataCleaningProfile(Profile):

    def set(self, params):
        print "Setting parameters in data cleaning subprofile "

    def execute(self, miningprofile):
        print "Executing data cleaning subprofile "

    def show(self, params):
        print "Showing stats in cleaned data"


mp = MiningProfile("a","b")
mp.profiles.append(FileLoadingProfile())
paramset = ParameterSet()
paramset.steps = []
s1 = Step()
s1.type="file_load"
s1.params.filepath = "/home/lakmal/PycharmProjects/AnantaUi/Data/projects.csv"
s1.params.filetype = "csv"
s1.params.loadto = "trainingset"
s1.params.loadindex = 0
s2 = Step()
s2.type="file_load"
s2.params.filepath = "/home/lakmal/PycharmProjects/AnantaUi/Data/projects.csv"
s2.params.filetype = "csv"
s2.params.loadto = "trainingset"
s2.params.loadindex = 0
paramset.steps.append(s1)
paramset.steps.append(s2)
mp.set(0,paramset)
mp.execute(0)
mp.profiles.append(DataCleaningProfile())
mp.set(1,"params from data cleaning ui")
mp.execute(1)