from ananta_base.base import Profile
import pandas

__author__ = 'lakmal'



class FileLoadingProfile(Profile):

    def __init__(self):
        self.steps = []

    def addStep(self, step):
        self.steps.append(step)

    def set(self, paramset):
        print "Setting parameters in file loading subprofile "
        self.paramset = paramset

    def execute(self):
        print "Executing file loading subprofile "
        # Get class from globals and create an instance
        m = globals()['FileLoadingProfile']()
        for step in self.steps:
            func = getattr(m, step.type)
            data = func(step)
        return data

    def show(self, params):
        print "Showing stats in loaded files"


    def file_load(self,params):
        print "loading file", params
        dataset = None
        if(params.filetype=="csv"):
            dataset = pandas.read_csv(params.filepath)
        elif(params.filetype=="xls"):
            dataset = pandas.read_excel(params.filepath)
        return dataset


class FileLoadStep():

    def __init__(self):
        self.type = "file_load"
