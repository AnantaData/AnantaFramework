__author__ = 'laksheen'

import unittest
import pandas as pd
import numpy as np
from ananta_base.data_io import FileLoadingProfile, FileLoadStep
from ananta_base.data_set import TrainingSet
from ananta_base.data_cleaning_pan import DataCleaningProfile
from ananta_base.data_cleaning_pan import IgnoreTupleStep,UseGlobalConstantStep,UseAttributeMeanStep,UseAttributeMedianStep,UseAttributeModeStep

class TestDataCleaning(unittest.TestCase):

    def setUp(self):
        print 'in setup'
        self.projects = TrainingSet()
        flp1 = FileLoadingProfile()
        s1 = FileLoadStep("csv", "zoo.csv")
        flp1.addStep(s1)
        flp1.execute(self.projects)

    '''
    Ignoring tuples step testing
    '''
    def test_ignore_tuple_step(self):
        print 'in test_ignore_tuple'
        original_no_tuples =  self.projects.data.shape[0]
        print 'original tuples count = ',original_no_tuples
        dtp = DataCleaningProfile()
        list = ['hair','toothed']
        step0 = IgnoreTupleStep(list)
        dtp.addStep(step0)
        dtp.execute(self.projects)
        new_no_tuples = self.projects.data.shape[0]
        print 'tuples count after ignoring tuples= ',new_no_tuples
        self.assertTrue(original_no_tuples != new_no_tuples,'tuples with null values have not been removed')

    '''
    Global constant step testing
    '''
    def test_global_constant_step(self):
        print 'in test_global_constant'
        trueOrFalse =  pd.isnull(self.projects.data['hair'])
        print trueOrFalse
        dtp = DataCleaningProfile()
        step0 = UseGlobalConstantStep('true',['hair'])
        dtp.addStep(step0)
        dtp.execute(self.projects)
        trueOrFalse =  pd.isnull(self.projects.data['hair'])
        print trueOrFalse
        self.assertFalse(np.alltrue(trueOrFalse))
    '''
    Attribute mean step testing
    '''
    def test_attribute_mean_step(self):
        print 'in test_attribute_mean'
        list = pd.isnull(self.projects.data['eggs'])
        null_count = 0
        for l in list:
            if l==True:
                null_count += 1
        print 'there are ',null_count,' tuple/s with null values in eggs column'

        dtp = DataCleaningProfile()
        step0 = UseAttributeMeanStep(['eggs'])
        dtp.addStep(step0)
        dtp.execute(self.projects)

        list = pd.isnull(self.projects.data['eggs'])
        new_null_count = 0
        for l in list:
            if l==True:
                new_null_count += 1

        print 'there are ',new_null_count,' tuples with null values in eggs column after attribute mean step'
        self.assertTrue(new_null_count == 0,'still there exists null values in eggs column')

    '''
    Attribute median step testing
    '''
    def test_attribute_median_step(self):
        print 'in test_attribute_median'
        list = pd.isnull(self.projects.data['aquatic'])
        null_count = 0
        for l in list:
            if l==True:
                null_count += 1
        print 'there are ',null_count,' tuple/s with null values in aquatic column'

        dtp = DataCleaningProfile()
        step0 = UseAttributeMedianStep(['aquatic'])
        dtp.addStep(step0)
        dtp.execute(self.projects)

        list = pd.isnull(self.projects.data['aquatic'])
        new_null_count = 0
        for l in list:
            if l==True:
                new_null_count += 1

        print 'there are ',new_null_count,' tuples with null values in aquatic column after attribute median step'
        self.assertTrue(new_null_count == 0,'still there exists null values in aquatic column')

    '''
    Attribute mode step testing
    '''
    def test_attribute_mode_step(self):
        print 'in test_attribute_mode'
        list = pd.isnull(self.projects.data['feathers'])
        null_count = 0
        for l in list:
            if l==True:
                null_count += 1
        print 'there are ',null_count,' tuple/s with null values in feathers column'

        dtp = DataCleaningProfile()
        step0 = UseAttributeModeStep(['feathers'])
        dtp.addStep(step0)
        dtp.execute(self.projects)

        list = pd.isnull(self.projects.data['feathers'])
        new_null_count = 0
        for l in list:
            if l==True:
                new_null_count += 1

        print 'there are ',new_null_count,' tuples with null values in feathers column after attribute median step'
        self.assertTrue(new_null_count == 0,'still there exists null values in feathers column')

if __name__ == '__main__':
    unittest.main()
