__author__ = 'tiroshan'
import pandas as pd
import numpy as np

class DataCleaningProfile:
    def __init__(self):
        self.steps = []

    def addStep(self, step):
        self.steps.append(step)

    def execute(self, dataset):
        data = dataset.data
        for step in self.steps:
            data = step.execute(data)
        dataset.data = data

class IgnoreTupleStep:

    def __init__(self,column_list):
        self.column_list = column_list

    def execute(self,data):
        print 'started Ignore tuple step'
        for column in self.column_list:
            data = data.dropna(axis = 0,subset = [column])
        print 'finished Ignore tuple step'
        return data

class UseGlobalConstantStep:

    def __init__(self,constant,column_list):
        self.constant = constant
        self.column_list = column_list

    def execute(self,data):
        print 'started global constant step'
        cons_pos = 0
        for column in self.column_list:
            data[column] = data[column].fillna(self.constant[cons_pos])
            cons_pos +=1
        print 'finished global constant step'
        return data

class UseAttributeMeanStep:

    def __init__(self,column_list):
        self.column_list = column_list

    def execute(self,data):
        print 'started attribute mean step'
        for column in self.column_list:
            data[column] = data.fillna(data.mean())
        print 'finished attribute mean step'
        return data

class UseAttributeModeStep:

    def __init__(self,column_list):
        self.column_list = column_list

    def execute(self,data):
        print 'started attribute mode step'
        for column in self.column_list:
            data[column] = data.fillna(data.mode())
        print 'finished attribute mode step'
        return data

class UseAttributeMedianStep:

    def __init__(self,column_list):
        self.column_list = column_list

    def execute(self,data):
        print 'started attribute median step'
        for column in self.column_list:
            data[column] = data.fillna(data.median())
        print 'started attribute mode step'
        return data

########