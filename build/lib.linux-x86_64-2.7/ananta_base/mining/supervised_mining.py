__author__ = 'gilgamesh'

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVC
from sklearn.preprocessing import OneHotEncoder
import numpy as np

class SupervisedMiningProfile:

    def __init__(self, col_Y):
        print 'creating mining profile...'
        self. col_Y = col_Y
        self.steps = []

    def addStep(self, step):
        self.steps.append(step)
#slight changes from other profiles
    ''' assumptions
    1) dataset.train_X = training manifold / manifest variables
    2) dataset.train_Y = training response
    3) dataset.test_X = testing manifold / required prediction manifest
    4) dataset.test_Y = optionally testing response / will be assigned...
    '''
    def execute(self, dataset):
        clf = None # required transitional classifiers.
        print 'setting response variable as selected...'
        dataset.train_Y = np.array(dataset.data[self.col_Y])
        print 'done!'
        print 'setting training data'
        dataset.train_X = np.array(dataset.data.drop(self.col_Y, axis=1))
        dataset.test_X=dataset.train_X

        print 'done'
        bmi=False
        print 'ready to execute profile...Executing!'
        st=1
        for step in self.steps:
            print 'step :', st
            st+=1
            clf, dataset, bmi = step.execute(classifier=clf, dataset=dataset, ohec=bmi)
        return dataset


# all steps will include a Train____Step() and a PredictStep()
class TrainLogitStep:


    def __init__(self):
        print 'creating logit step...'
        self.clf = LogisticRegression()

    def execute(self, dataset, classifier=None , ohec=False):
        print 'executing logit step...'
        x = dataset.train_X
        y = dataset.train_Y
        ohec=OneHotEncoder()
        x = ohec.fit_transform(x)
        self.clf.fit(x,y)
        #print self.clf.predict(x)
        return self.clf, dataset, True





class TrainRanforStep:


    def __init__(self):
        self.clf = RandomForestRegressor()

    def execute(self,dataset, classifier=None, ohec=False):
        x = dataset.train_X
        y = dataset.train_Y

        self.clf.fit(x,y)


        return self.clf, dataset, False



class TrainSVMStep:

    def __init__(self):
        self.clf = SVC()

    def execute(self, dataset ,classifier=None, ohec = False):
        x = dataset.train_X
        y = dataset.train_Y

        self.clf.fit(x,y)
        return self.clf, dataset, False



class PredictStep:

    def execute(self, dataset, classifier=None, ohec = False):
        print 'executing prediction...'

        if dataset.test_X is None:

            dataset.test_X=dataset.train_X
            #print 'test',dataset.test_X

        if ohec:
            oh = OneHotEncoder()
            dataset.test_X=oh.fit_transform(dataset.test_X)

        dataset.pred_y = classifier.predict(dataset.test_X)
        #print dataset.pred_y
        return None,dataset,False