__author__ = 'tiroshan'
import pandas as pd
import numpy as np

class DatacleaningProfile:
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
        for column in self.column_list:
            data = data.dropna(subset = [column])
        return data

class UseGlobalConstantStep:

    def __init__(self,constant,column_list):
        self.constant = constant
        self.column_list = column_list

    def execute(self,data):
        # self.constant
        cons_pos = 0
        for column in self.column_list:
            data[column] = data[column].fillna(self.constant[cons_pos])
            cons_pos +=1

        return data

class UseAttributeMeanStep:

    def __init__(self,column_list):
        self.column_list = column_list

    def execute(self,data):
        for column in self.column_list:
            data[column] = data.fillna(data.mean())
        return data

class UseAttributeModeStep:

    def __init__(self,column_list):
        self.column_list = column_list

    def execute(self,data):
        for column in self.column_list:
            data[column] = data.fillna(data.mode())
        return data

class UseAttributeMedianStep:

    def __init__(self,column_list):
        self.column_list = column_list

    def execute(self,data):
        for column in self.column_list:
            data[column] = data.fillna(data.median())
        return data

########