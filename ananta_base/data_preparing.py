
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

    def execute(self,data):
        return data.sort(self.fieldname)

class DataSelectStep:

    def execute(self,data):
        return eval(self.selectlogic)