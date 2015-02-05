__author__ = 'gilgamesh'

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVC

class SupervisedMiningProfile:

    def __init__(self):
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
        for step in self.steps:
            clf, dataset = step.execute(classifier=clf, dataset=dataset)
        return dataset


# all steps will include a Train____Step() and a PredictStep()
class TrainLogitStep:


    def __init__(self):
        self.clf = LogisticRegression()

    def execute(self, dataset, classifier=None ):
        x = dataset.train_X
        y = dataset.train_Y

        self.clf.fit(x,y)
        return self.clf, dataset





class TrainRanforStep:


    def __init__(self):
        self.clf = RandomForestRegressor()

    def execute(self,dataset, classifier=None):
        x = dataset.train_X
        y = dataset.train_Y

        self.clf.fit(x,y)
        return self.clf, dataset



class TrainSVMStep:

    def __init__(self):
        self.clf = SVC()

    def execute(self, dataset ,classifier=None):
        x = dataset.train_X
        y = dataset.train_Y

        self.clf.fit(x,y)
        return self.clf, dataset



class PredictStep:

    def execute(self, dataset, classifier=None):

        dataset.pred_y = classifier.predict(dataset.test_X)

        return None,dataset