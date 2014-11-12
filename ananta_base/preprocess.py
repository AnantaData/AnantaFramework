__author__ = 'lakmal'

import base
from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import chi2
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import SelectPercentile
import numpy as np

class DataCleaningProfile(base.Profile):

    def set(self, params):
        print "Setting parameters in data cleaning subprofile "

    def execute(self, miningprofile):
        print "Executing data cleaning subprofile "

    def show(self, params):
        print "Showing stats in cleaned data"


class Reduction:

    def __init__(self,numpyArray):
        self.array = np.array(numpyArray)

    #removes features which has a probability less than 'input_threshold'
    def varianceThreshold(self,input_threshold=0.6):

        sel = VarianceThreshold(threshold=(input_threshold * (1 - input_threshold)))
        reduced_array = sel.fit_transform(self.array)
        return reduced_array

    #for Classification, selects the two best features
    def chiSquareTest(self):

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