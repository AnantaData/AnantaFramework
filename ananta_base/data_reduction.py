__author__ = 'lakmal'

import base

from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import chi2
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import SelectPercentile
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import numpy as np



class DataReductionProfile(base.Profile):

    def __init__(self):
        self.steps = []

    def addStep(self, step):
        self.steps.append(step)

    def execute(self, dataset):
        data = dataset.data
        for step in self.steps:
            data = step.execute(data)
        dataset.data = data

'''drop a list of columns from column names'''
class DropColumnsByNameStep:

    def execute(self,data):
        return data.drop(self.columnNames,inplace=True,axis=1)  # columnNames is a list of strings


'''drop a list of columns from column index'''
class DropColumnsByIndexStep:

    def execute(self,data):
        return data.drop(self.columnIndexes,inplace=True,axis=1)  # columnIndexes is a list of strings


'''remove columns which are below a variance threshold'''
class VarianceThresholdStep:

    def execute(self,data):

        listOfNames = data.var(axis=0, skipna=True, level=None, numeric_only=True)

        dropList = []
        for i in listOfNames.index:
            variance = listOfNames.ix[i]
            if(variance < self.varianceThreshold):
                dropList.append(i)

        x = DropColumnsByNameStep()

        self.columnNames = dropList
        return x.execute(data)


'''select best k features - for classification'''
class SelectKBestStep:

    def execute(self,data):

        transformer =  SelectKBest(score_func=chi2,self.k)
        output = transformer.fit(data.x,data.y).get_support(indices=True)     # data.x are features of the dataset, data.y are the targets

        newData = data.ix[:,(output)]

        return newData


