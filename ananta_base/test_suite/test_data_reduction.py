__author__ = 'laksheen'

import unittest
from ananta_base.data_io import FileLoadingProfile, FileLoadStep
from ananta_base.data_set import TrainingSet
from ananta_base.data_reduction import DataReductionProfile, DropColumnsByNameStep, VarianceThresholdStep

class TestDataReduction(unittest.TestCase):

    def setUp(self):
        print 'in setup'
        self.projects = TrainingSet()
        flp1 = FileLoadingProfile()
        s1 = FileLoadStep("csv", "zoo.csv")
        flp1.addStep(s1)
        flp1.execute(self.projects)

    '''
    Drop columns by names step testing
    '''
    def test_drop_columns_by_names(self):
        print 'in test_drop_columns_by_names'
        original_no_columns = self.projects.data.shape[1]
        print 'Dataset has ',original_no_columns,' columns'
        drop_list = ['catsize','breathes']
        print 'drop column/s ',drop_list

        drp = DataReductionProfile()
        step0 = DropColumnsByNameStep(drop_list)
        drp.addStep(step0)
        drp.execute(self.projects)

        new_no_columns = self.projects.data.shape[1]
        print 'Now dataset has only',new_no_columns,' columns'

        self.assertTrue(original_no_columns > new_no_columns)

    '''
    Variance Threshold step testing
    '''
    def test_variance_threshold(self):
        print 'in test_variance_threshold'
        original_no_columns = self.projects.data.shape[1]
        print 'Dataset has ',original_no_columns,' columns'

        var_thresh = 0.24
        drp = DataReductionProfile()
        step0 = VarianceThresholdStep(var_thresh)
        drp.addStep(step0)
        drp.execute(self.projects)

        new_no_columns = self.projects.data.shape[1]
        print 'Now dataset has only',new_no_columns,' columns'

        self.assertTrue(original_no_columns > new_no_columns)

if __name__ == '__main__':
    unittest.main()
