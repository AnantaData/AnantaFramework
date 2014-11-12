# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/lakmal/Desktop/AnantaUI/newprojectdialog.ui'
#
# Created: Mon Nov  3 14:11:12 2014
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import shutil
from ananta_views import new_project_dialog_view
from PyQt4.QtGui import QDialog


class NewProjectDialog(QDialog):

    def __init__(self,parent=None):
        super(NewProjectDialog, self).__init__(parent)
        self.new_proj_ui = new_project_dialog_view.Ui_newProjectDialog()
        self.new_proj_ui.setupUi(self)

    def accept(self):
        proj_name = self.new_proj_ui.projectNameLineEdit.text()
        workspace = "AnantaWorkspace"
        seperator = "/"
        extension = ".xml"
        src = workspace+seperator+"Ananta"+extension
        dest = workspace+seperator+proj_name+extension
        f = open(dest,"w+")
        f.close()
        shutil.copyfile(src,dest)
        self.parent().main_window_ui.miningProfWidget.profileName = proj_name
        self.parent().refreshMiningWidget()
        super(NewProjectDialog,self).accept()

    def reject(self):
        super(NewProjectDialog,self).accept()

