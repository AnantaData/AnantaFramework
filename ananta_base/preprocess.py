__author__ = 'lakmal'

import base

class DataCleaningProfile(base.Profile):

    def set(self, params):
        print "Setting parameters in data cleaning subprofile "

    def execute(self, miningprofile):
        print "Executing data cleaning subprofile "

    def show(self, params):
        print "Showing stats in cleaned data"
