from ananta_base.base import *
from ananta_base.data_cleaning_pan import DataCleaningProfile, UseGlobalConstantStep
from ananta_base.data_io import FileLoadingProfile, FileLoadStep
#from ananta_base.preprocess import DataCleaningProfile
from ananta_base.data_preparing import DataPreparingProfile, DataSortStep, DataSelectStep
from ananta_base.data_set import TrainingSet
from ananta_base.data_transformation import DataTransformationProfile, EncodingStep

__author__ = 'lakmal'

projects = TrainingSet()

flp1 = FileLoadingProfile()
s1 = FileLoadStep("csv", "/home/lakmal/PycharmProjects/AnantaUi/Data/projects.csv")
flp1.addStep(s1)
flp1.execute(projects)
'''
dpp1 = DataPreparingProfile()
s2 = DataSortStep("projectid")
s3 = DataSelectStep("data.loc[data['date_posted'] < '2014-01-01']")
dpp1.addStep(s2)
dpp1.addStep(s3)
dpp1.execute(projects)

dcp1 = DataCleaningProfile()
<<<<<<< HEAD
mp.profiles.append(dcp1)


dtp1 = DataTransformationProfile()
dtp1.dataset=data#from somewhere
mp.profiles.append(dtp1)
dtp1paramset= ParameterSet()
dtp1.set(dtp1paramset)

s3=BinningStep()
s3.feature_set=np.array(['age','income','monthly_charge'])
s3.typeset=np.array(['uni_depth','mini_max','mini_max'])

s4= EncodingStep()
s4.encoding='one_hot'


dtp1paramset.addStep(s3)




mp.set(1,"params from data cleaning ui")
mp.execute(1)
=======
s4 = UseGlobalConstantStep([5],['total_price_including_optional_support'])
dcp1.addStep(s4)
dcp1.execute(projects)
'''
dtp1 = DataTransformationProfile()
s5= EncodingStep('one_hot',['school_charter'])
dtp1.addStep(s5)
dtp1.execute(projects)

print projects.data.school_charter
>>>>>>> 033a93038fc951090251c1fe562a8548d08a36b3
