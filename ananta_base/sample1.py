from ananta_base.base import *
from ananta_base.data_io import FileLoadingProfile, FileLoadStep
#from ananta_base.preprocess import DataCleaningProfile

__author__ = 'lakmal'

projects = None

flp1 = FileLoadingProfile()
s1 = FileLoadStep()
s1.filepath = "/home/lakmal/PycharmProjects/AnantaUi/Data/projects.csv"
s1.filetype = "csv"
flp1.addStep(s1)

projects = flp1.execute()




