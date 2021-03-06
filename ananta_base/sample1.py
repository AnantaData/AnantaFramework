from ananta_base.base import *
from ananta_base.data_cleaning_pan import DataCleaningProfile, UseGlobalConstantStep, IgnoreTupleStep
from ananta_base.data_io import FileLoadingProfile, FileLoadStep
from ananta_base.data_preparing import DataPreparingProfile, DataSortStep, DataSelectStep
from ananta_base.data_set import TrainingSet
from ananta_base.data_transformation import DataTransformationProfile, EncodingStep


projects = TrainingSet()

flp1 = FileLoadingProfile()
s1 = FileLoadStep("csv", "/home/lakmal/PycharmProjects/AnantaUi/Data/projects.csv")
flp1.addStep(s1)
flp1.execute(projects)
print projects.data

dpp1 = DataPreparingProfile()
s2 = DataSortStep("projectid")
s3 = DataSelectStep("data.loc[data['date_posted'] < '2014-01-01']")
dpp1.addStep(s2)
dpp1.addStep(s3)
dpp1.execute(projects)

dcp1 = DataCleaningProfile()
s4 = UseGlobalConstantStep([5],['total_price_including_optional_support'])
dcp1.addStep(s4)
dcp1.execute(projects)

'''dtp1 = DataTransformationProfile()
s5= EncodingStep('one_hot',['school_charter'])
dtp1.addStep(s5)
dtp1.execute(projects)

print projects.data.school_charter'''
