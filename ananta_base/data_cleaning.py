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
    def ignore_tuple(self, column_no,nparray):
        loop = 0
        while loop < np.alen(nparray):
            if str(nparray[loop, column_no]) == 'nan':
                nparray = np.delete(nparray, loop, 0)
                loop = loop
            else:
                loop = loop + 1
        return nparray

    #------------- Use global constant-----------------#
    def fill_global_constant(self, column_no,constant,nparray):
        loop = 0
        while loop < np.alen(nparray):
            if str(nparray[loop, column_no]) == 'nan':
                nparray[loop,column_no] = constant
            loop = loop + 1
        return nparray

    #------------- Attribute mean mode median ----------#
    def attribute_mean(self, column_no,nparray):
        selct_column_array = np.asarray(nparray[:,column_no])
        get_mean= np.nanmean(list(selct_column_array))
        return self.use_global_constant(column_no,get_mean,nparray)

    def attribute_median(self, column_no,nparray):
        selct_column_array = np.asarray(nparray[:,column_no])
        get_median= np.median(list(selct_column_array))
        return self.use_global_constant(column_no,get_median,nparray)

    def attribute_mode(self, column_no,nparray):
        get_mode = mode(nparray[:,column_no])[0][0]
        return self.use_global_constant(column_no,get_mode,nparray)

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
        while loop < np.alen(nparray):
            nparray[loop, column_no] = attribute
            loop = loop + 1
        return nparray

class IgnoreTupleStep:

    def __init__(self):
        self.type = "ignore_tuple"

class FillGlobalConstStep():

    def __init__(self):
        self.type = "fill_global_constant"

class FillAttrMeanStep():

    def __init__(self):
        self.type = "fill_attribute_mean"
