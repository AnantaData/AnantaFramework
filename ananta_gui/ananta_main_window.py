# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/lakmal/Desktop/AnantaUI/anantamainwindow.ui'
#
# Created: Mon Nov  3 14:00:16 2014
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!


from PyQt4 import QtGui
import sys
import os

from PyQt4.QtGui import QApplication, QMainWindow
from PyQt4.QtGui import QFileDialog

from ananta_gui import new_project_dialog
from ananta_profile import mining_profile_api
from ananta_views import ananta_main_window_view, file_load_prof_widget_view
import file_load_prof_widget

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.main_window_ui = ananta_main_window_view.Ui_MainWindow()
        self.main_window_ui.setupUi(self)

    def openNewProjectDialog(self):
        self.newProjDialog = new_project_dialog.NewProjectDialog(self)
        self.newProjDialog.exec_()

    def openOpenProjectDialog(self):
        self.fileToOpen = QFileDialog.getOpenFileName(
                         self,
                         "Select a file to open",
                         "AnantaWorkspace",
                         "XML files (*.xml)")
        head, tail = os.path.split(str(self.fileToOpen))
        fileName, fileExtension = os.path.splitext(tail)
        self.main_window_ui.miningProfWidget.profileName = fileName
        self.refreshMiningWidget()

    def refreshMiningWidget(self):
        self.main_window_ui.miningProfLbl.setText("MINING PROFILE - "+self.main_window_ui.miningProfWidget.profileName)
        fileName = 'AnantaWorkspace/'+self.main_window_ui.miningProfWidget.profileName+'.xml'
        #print fileName
        self.mining_profile = mining_profile_api.parse(str(fileName))
        self.generateMiningProfileUi(self.mining_profile)

    def generateMiningProfileUi(self,miningProfile):
        self.deleteAllWidgets(self.main_window_ui.miningProfGridLayout)
        self.main_window_ui.miningProfWidget.profWidgets = []
        count = 0
        verticalPos = 0
        profiles = miningProfile.Model.Profiles.Profile
        empty = False
        self.profWidgets = []
        for profile in profiles:
            if(count%2):
                verticalPos = verticalPos+100
            print profile.Type
            if(profile.Type == "file_load"):
                new_widget = file_load_prof_widget.FileLoadProfWidget()
                new_widget.index = profile.No_attr
                new_widget.profileName = self.main_window_ui.miningProfWidget.profileName
                print "No attr", profile.No_attr
                self.main_window_ui.miningProfWidget.profWidgets.append(new_widget)
                self.main_window_ui.miningProfGridLayout.addWidget(new_widget)
            count+=1

    def deleteAllWidgets(self,layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            widget.deleteLater()

    def addFlProfile(self):
        new_widget = file_load_prof_widget.FileLoadProfWidget()
        new_widget.index = len(self.main_window_ui.miningProfWidget.profWidgets)+1
        new_widget.profileName = self.main_window_ui.miningProfWidget.profileName
        print "No attr", new_widget.index
        self.main_window_ui.miningProfWidget.profWidgets.append(new_widget)
        self.main_window_ui.miningProfGridLayout.addWidget(new_widget)

app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec_()
