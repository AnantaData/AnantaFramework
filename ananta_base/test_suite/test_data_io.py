__author__ = 'laksheen'

import unittest
import pandas as pd
from ananta_base.data_io import FileLoadingProfile,FileLoadStep
from ananta_base.data_set import TrainingSet

class TestDataIO(unittest.TestCase):

    def setUp(self):
        self.projects = TrainingSet()

    '''
    File loading profile testing
    '''
    def test_file_loading(self):
        print 'in test_file_loading'
        flp1 = FileLoadingProfile()
        s1 = FileLoadStep("csv", "zoo.csv")
        flp1.addStep(s1)
        flp1.execute(self.projects)
        print self.projects
        self.assertFalse(pd.isnull(self.projects))

if __name__ == '__main__':
    unittest.main()
