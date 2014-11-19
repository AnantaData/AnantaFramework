__author__ = 'lakmal'

import base


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


class ConvertToNpStep:

    def __init__(self):
        self.type = "convert_to_np"



