from ananta_base.base import *
from ananta_base.ananta_io import FileLoadingProfile, FileLoadStep
from ananta_base.preprocess import DataCleaningProfile

__author__ = 'lakmal'

mp = MiningProfile("","")

flp1 = FileLoadingProfile()
mp.profiles.append(flp1)

flp1paramset = ParameterSet()
flp1.set(flp1paramset)

s1 = FileLoadStep()
s1.filepath = "/home/lakmal/PycharmProjects/AnantaUi/Data/projects.csv"
s1.filetype = "csv"
s1.loadto = "trainingset"
s1.loadindex = 0

s2 = FileLoadStep()
s2.type="file_load"
s2.filepath = "/home/lakmal/PycharmProjects/AnantaUi/Data/projects.csv"
s2.filetype = "csv"
s2.loadto = "trainingset"
s2.loadindex = 1

flp1paramset.addStep(s1)
flp1paramset.addStep(s2)

mp.execute(0)

dcp1 = DataCleaningProfile()
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