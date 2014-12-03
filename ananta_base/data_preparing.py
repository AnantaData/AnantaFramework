
__author__ = 'lakmal'


class DataPreparingProfile:

    def __init__(self):
        self.steps = []

    def addStep(self, step):
        self.steps.append(step)

    def execute(self, dataset):
        data = dataset.data
        for step in self.steps:
            data = step.execute(data)
        dataset.data = data


class DataSortStep:

    def __init__(self,fieldname):
        self.fieldname = fieldname

    def execute(self,data):
        return data.sort(self.fieldname)

class DataSelectStep:

    def __init__(self,selectlogic):
        self.selectlogic = selectlogic

    def execute(self,data):
        return eval(self.selectlogic)