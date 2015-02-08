__author__ = 'lakmal'

import base
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import numpy as np

class DataTransformationProfile():

    def __init__(self):
        self.steps = []

    def addStep(self, step):
        self.steps.append(step)

    def execute(self, dataset):
        data = dataset.data
        for step in self.steps:
            data = step.execute(data)
        dataset.data = data

'''
class EncodingStep(object):

    def __init__(self,encoding,fields):
        self.encoding = encoding
        self.fields = fields

    def execute(self,data):
        if self.encoding == 'one_hot' :
            dataset=self.BitmapEncode(data,self.fields)
        elif self.encoding == 'label':
            dataset=self.LabelEncode(data,self.fields)
        return dataset

    def BitmapEncode(self,data,fields):
        bme = OneHotEncoder()
        for field in fields:
            print data[field]
            output_array = bme.fit(np.array(data[field]))
            print output_array
            data[field] = bme.transform(output_array)
        return data

    def LabelEncode(self, inp_np_array ):

        le = LabelEncoder()
        output_array = le.fit_transform(inp_np_array[:,0])

        for i in range(1,inp_np_array[1]):
            output_array=np.column_stack(output_array,le.fit_transform(inp_np_array[:,i]))

        return output_array

class BitmapEncodingStep(object):

    def __init__(self,column_list):
        self.column_list=column_list

    def execute(self,data):
        bme = OneHotEncoder()
        for field in self.column_list:
            print data[field]
            output_array = bme.fit(np.array(data[field]))
            print output_array
            data[field] = bme.transform(output_array)
        return data
'''

class LabelEncodingStep():

    def __init__(self,column_list):
        self.column_list=column_list

    def execute(self,data):
        print 'started label encoding step'
        le = LabelEncoder()
        output_array = le.fit_transform(data[self.column_list[0]])
        for i in range(1,len(self.column_list)):
            output_array=np.column_stack([output_array,le.fit_transform(data[self.column_list[i]])])
        print 'finished label encoding step'
        return output_array

class BinningStep(object):

    def __init__(self):
        self.feature_set = np.array([])
        self.bin_algs = np.array([])
        self.num_bins = np.array([])

    def execute(self,dataset):
        print 'started binning step'
        for i in range(self.feature_set.shape[0]):
            #account for bin_algs
            dataset[self.feature_set[i]]=self.Bin_Uniform_depth(dataset[self.feature_set[i]],self.num_bins[i])
        print 'finished binning step'
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


class ConvertToNpStep:

    def __init__(self):
        self.type = "convert_to_np"



