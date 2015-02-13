__author__ = 'laksheen'

import unittest
from ananta_base.data_io import FileLoadingProfile, FileLoadStep
from ananta_base.data_set import TrainingSet
from ananta_base.data_transformation import DataTransformationProfile, LabelEncodingStep

class TestDataTransformation(unittest.TestCase):

    def setUp(self):
        print 'in setup'
        self.projects = TrainingSet()
        flp1 = FileLoadingProfile()
        s1 = FileLoadStep("csv", "zoo.csv")
        flp1.addStep(s1)
        flp1.execute(self.projects)

    '''
    Label Encoding step testing
    '''
    def test_label_encoding(self):
        print 'in test_label_encoding'
        encode_list = ["hair","feathers","eggs","milk","airborne","aquatic","predator","toothed","backbone","breathes","venomous","fins","tail","domestic","catsize"]
        list = self.projects.data.dtypes           #list with original data types
        print 'list is ',list
        dtp = DataTransformationProfile()
        step0 = LabelEncodingStep(encode_list)
        dtp.addStep(step0)
        dtp.execute(self.projects)
        new_list = self.projects.data.dtypes       #list with data types after label encoding
        print 'new list is ',new_list

        for i in new_list:
            if i==bool:
                self.assertTrue(False,'bool columns still exist')
            else:
                self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
