from ananta_base.base import Profile
import pandas

__author__ = 'lakmal'



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
            dataset = pandas.read_csv(params.filepath)
        elif(params.filetype=="xls"):
            dataset = pandas.read_excel(params.filepath)
        if(params.loadto =="trainingset"):
            miningprofile.trainingsets.insert(params.loadindex, dataset)
        elif(params.loadto =="testset"):
            miningprofile.testsets[params.loadindex] = dataset