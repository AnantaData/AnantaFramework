from ananta_base.base import *
from ananta_base.ananta_io import FileLoadingProfile
from ananta_base.preprocess import DataCleaningProfile

__author__ = 'lakmal'

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