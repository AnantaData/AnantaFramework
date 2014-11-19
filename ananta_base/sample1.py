from ananta_base.base import *
from ananta_base.data_io import FileLoadingProfile, FileLoadStep
#from ananta_base.preprocess import DataCleaningProfile
from ananta_base.data_preparing import DataPreparingProfile, DataSortStep, DataSelectStep
from ananta_base.data_set import TrainingSet

__author__ = 'lakmal'

projects = TrainingSet()

flp1 = FileLoadingProfile()
s1 = FileLoadStep()
s1.filepath = "/home/lakmal/PycharmProjects/AnantaUi/Data/projects.csv"
s1.filetype = "csv"
flp1.addStep(s1)

flp1.execute(projects)

dpp1 = DataPreparingProfile()
s2 = DataSortStep()
s2.fieldname = "projectid"
s3 = DataSelectStep()
s3.selectlogic = "data.loc[data['date_posted'] < '2014-01-01']"
dpp1.addStep(s2)
dpp1.addStep(s3)

dpp1.execute(projects)


print projects.data