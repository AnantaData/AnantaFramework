__author__ = 'lakmal'

import base

from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import chi2
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import SelectPercentile
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import numpy as np
import pandas as pd


class DataReductionProfile:

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

    def __init__(self,columnNames):
        self.columnNames= columnNames

    def execute(self,data):
        print 'started dropping columns step'
        data1 = pd.DataFrame(data)
        data1.drop(self.columnNames,inplace=True,axis=1)  # columnNames is a list of strings
        print 'finished dropping columns step'
        return data1

'''drop a list of columns from column index'''
class DropColumnsByIndexStep:

    def __init__(self,columnIndexes):
        self.columnIndexes = columnIndexes

    def execute(self,data):
        print 'started dropping columns by index step'
        data = data.drop(self.columnIndexes,inplace=True,axis=1)  # columnIndexes is a list of strings
        print 'finished dropping columns by index step'
        return data

'''remove columns which are below a variance threshold'''
class VarianceThresholdStep:

    def __init__(self,varianceThreshold):
        self.varianceThreshold = varianceThreshold

    def execute(self,data):
        print 'started dropping columns based on Variance'
        listOfNames = data.var(axis=0, skipna=True, level=None, numeric_only=True)

        dropList = []
        for i in listOfNames.index:
            variance = listOfNames.ix[i]
            if(variance < self.varianceThreshold):
                dropList.append(i)

        x = DropColumnsByNameStep(dropList)
        data = x.execute(data)
        print 'finished dropping columns step'
        return data


'''select best k features - for classification'''
class SelectKBestStep:

    def __init__(self,kFeatures,x,y):
        self.kFeatures = kFeatures
        self.features = x
        self.target = y

    def execute(self,data):
        print 'started finding the best ',self.kFeatures,' columns'
        transformer =  SelectKBest(score_func=chi2, k=self.kFeatures)
        output = transformer.fit(self.features,self.target).get_support(indices=True)     # data.x are features of the dataset, data.y are the targets

        newData = data.ix[:,(output)]
        print 'finished finding the best ',self.kFeatures,' columns'
        return newData


