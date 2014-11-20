__author__ = 'lakmal'

import base

from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import chi2
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import SelectPercentile
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import numpy as np

''' Data Transformation code region '''
################ Data Transformation Main Profile ################
class DataTransformationProfile(base.Profile):

    steps =[]
    dataset=None

    def set(self, params):
        for param in params:
            self.steps.append(param)

        print "parameters in transformation subprofile set"

    def execute(self, miningprofile):
        for step in steps:
            step.executeStep(dataset)

        print "transfromation subprofile done"

        return self.dataset

    def show(self, params):
        print "showing transformed data"

####################### Data Transformation Steps #######################################################

class EncodingStep(object):

    def executeStep(self,dataset):
        if self.encoding == 'one_hot' :
            dataset=self.BitmapEncode(dataset)
        else if self.encoding == 'label':
            dataset=self.LabelEncode(dataset)

        return dataset



    def BitmapEncode(self, inp_np_arry ):

        bme = OneHotEncoder()
        output_array = bme.fit(inp_np_arry)
        output_array = bme.transform(output_array)

        return output_array

    def LabelEncode(self, inp_np_array ):

        le = LabelEncoder()
        output_array = le.fit_transform(inp_np_array[:,0])

        for i in range(1,inp_np_array[1]):
            output_array=np.column_stack(output_array,le.fit_transform(inp_np_array[:,i]))

        return output_array

class BinningStep(object):

    def __init__(self):
        self.feature_set = np.array([])
        self.bin_algs = np.array([])
        self.num_bins = np.array([])

    def executeStep(self,dataset):

        for i in range(self.feature_set.shape[0]):
            #account for bin_algs
            dataset[self.feature_set[i]]=self.Bin_Uniform_depth(dataset[self.feature_set[i]],num_bins[i])

        return dataset

    def Bin_Uniform_depth(self,inp_np_array, num_of_bins):

        n=num_of_bins

        t=inp_np_array

        t=np.sort(t)

        bins=[]

        for i in range(n):
            bins[i] = t[len(t)/n]

        out_arr= np.digitize(inp_np_array,np.array(bins))

        return out_arr





''' Data Cleaning Code Locale '''


class DataCleaningProfile(base.Profile):

    def set(self, params):
        print "Setting parameters in data cleaning subprofile "

    def execute(self, miningprofile):
        print "Executing data cleaning subprofile "

    def show(self, params):
        print "Showing stats in cleaned data"


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


