from numpy.core.multiarray import dtype

__author__ = 'tiroshan'
import numpy as np
from scipy.stats import mode
from scipy import stats
from sklearn.preprocessing import Imputer


class Cleaning:
    def __init__(self, nparray):
        self.nparray = nparray

    # ----------Data Cleaning-Missing Values-----------#

    # -----------Ignore the tuple----------------------#
    def ignoreTuple(self, column_no):
        loop = 0
        while loop < np.alen(self.nparray):
            if str(self.nparray[loop, column_no]) == 'nan':
                self.nparray = np.delete(self.nparray, loop, 0)
                loop = loop
            else:
                loop = loop + 1
        return self.nparray

    #------------- Use global constant-----------------#
    def use_global_constant(self, column_no,constant):
        loop = 0
        while loop < np.alen(self.nparray):
            if str(self.nparray[loop, column_no]) == 'nan':
                self.nparray[loop,column_no] = constant
            loop = loop + 1
        return self.nparray

    #------------- Attribute mean mode median ----------#
    def attribute_mean(self, column_no):
        selct_column_array = np.asarray(self.nparray[:,column_no])
        mean= np.nanmean(list(selct_column_array))
        return self.use_global_constant(column_no,mean)

    def attribute_median(self, column_no):
        selct_column_array = np.asarray(self.nparray[:,column_no])
        mean= np.median(list(selct_column_array))
        return self.use_global_constant(column_no,mean)

    def attribute_mode(self, column_no):
        get_mode = mode(self.nparray[:,column_no])[0][0]
        return self.use_global_constant(column_no,get_mode)

    #     Attribute mean for all samples belonging to the same class as the given tuple
    def attribute_mean_wrt_another(self, column_no, ref_column_no):
        print column_no + ' ' + ref_column_no

    def attribute_median_wrt_another(self, column_no, ref_column_no):
        print column_no + ' ' + ref_column_no

    def attribute_mode_wrt_another(self, column_no, ref_column_no):
        print column_no + ' ' + ref_column_no

    #     Most probable value to fill
    def aprobable_value(self, column_no):
        print column_no

    #---------------- Replace function ----------------
    def replace_by_attribute(self, attribute, column_no, nparray):
        loop = 0
        while loop < np.alen(self.nparray):
            nparray[loop, column_no] = attribute
            loop = loop + 1
        return nparray

    def myFirst(self):
        #print self.nparray[:,[3]]
        # print self.nparray
        snparray = self.nparray[np.isnan(self.nparray).any(axis=2)]
        print  snparray
