__author__ = 'lakmal'

import base

from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import chi2
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import SelectPercentile
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import numpy as np



class DataReductionProfile(base.Profile):

    def set(self, paramset):
        print "Setting parameters in data reduction subprofile "
        self.paramset = paramset

    def execute(self, miningprofile):
        m = globals()['DataReductionProfile']()
        for step in self.paramset.steps:
            func = getattr(m, step.type)
            func(step,miningprofile)

    def show(self, params):
        print "Showing stats in reduced data"


    #removes features which has a probability less than 'input_threshold'
    def varianceThreshold(self,input_threshold=0.6):

        sel = VarianceThreshold(threshold=(input_threshold * (1 - input_threshold)))
        reduced_array = sel.fit_transform(self.array)
        return reduced_array

    #for Classification, selects the two best features
    def chi_square_test(self,params,miningprofile):

        X_new = SelectKBest(score_func=chi2, k=2)
        X_r = X_new.transform(self.array)
        print X_r

    #select the k best features
    def selectKbest(self,k=2):

        transformer =  SelectKBest( k)
        output = transformer.transform(self.array)
        print output

    def selectPercentile(self,percentage=60):

        transformer = SelectPercentile(percentile=percentage)
        output = transformer.transform(self.array)
        print np.array(output).shape

