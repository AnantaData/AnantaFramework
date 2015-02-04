__author__ = 'gilgamesh'

import ananta_base.data_io as dio

profile = None
def load(tp="csv", f_path="testcsv.csv"):
    if profile is None:
        profile = dio.FileLoadingProfile()
    file_ = dio.FileLoadStep(tp, f_path)

    profile.addStep(file_)

    profile.execute()

    return "done"

def main(tp, f_path):
    return load(tp,f_path)
