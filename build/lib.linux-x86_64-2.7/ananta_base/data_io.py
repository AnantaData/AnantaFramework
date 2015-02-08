from ananta_base.base import Profile
import pandas

__author__ = 'lakmal'



class FileLoadingProfile():

    def __init__(self):
        self.steps = []

    def addStep(self, step):
        self.steps.append(step)

    def execute(self, dataset):
        data = dataset.data
        for step in self.steps:
            data = step.execute(data)
        dataset.data = data


class FileLoadStep():

    def __init__(self,filetype, filepath):
        self.filetype = filetype
        self.filepath = filepath

    def execute(self,data):
        if(self.filetype=="csv"):
            print "Started Loading .csv file ",self.filepath
            data = pandas.read_csv(self.filepath)
        elif(self.filetype=="xls"):
            print "Started Loading .xls file ",self.filepath
            data = pandas.read_excel(self.filepath)
        print "Finished Loading File"
        return data