# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/lakmal/Desktop/AnantaUI/anantamainwindow.ui'
#
# Created: Thu Nov  6 17:37:19 2014
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(663, 478)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.miningProfWidget = QtGui.QWidget(self.centralwidget)
        self.miningProfWidget.setGeometry(QtCore.QRect(10, 10, 641, 381))
        self.miningProfWidget.setObjectName(_fromUtf8("miningProfWidget"))
        self.miningProfLbl = QtGui.QLabel(self.miningProfWidget)
        self.miningProfLbl.setGeometry(QtCore.QRect(156, 9, 331, 31))
        self.miningProfLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.miningProfLbl.setObjectName(_fromUtf8("miningProfLbl"))
        self.gridLayoutWidget = QtGui.QWidget(self.miningProfWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 40, 601, 321))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.miningProfGridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.miningProfGridLayout.setMargin(0)
        self.miningProfGridLayout.setObjectName(_fromUtf8("miningProfGridLayout"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 663, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuANANTA = QtGui.QMenu(self.menubar)
        self.menuANANTA.setObjectName(_fromUtf8("menuANANTA"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionAddFlProfile = QtGui.QAction(MainWindow)
        self.actionAddFlProfile.setObjectName(_fromUtf8("actionAddFlProfile"))
        self.actionDataCleaningProfile = QtGui.QAction(MainWindow)
        self.actionDataCleaningProfile.setObjectName(_fromUtf8("actionDataCleaningProfile"))
        self.actionNew_Project = QtGui.QAction(MainWindow)
        self.actionNew_Project.setObjectName(_fromUtf8("actionNew_Project"))
        self.actionOpen_Project = QtGui.QAction(MainWindow)
        self.actionOpen_Project.setObjectName(_fromUtf8("actionOpen_Project"))
        self.menuANANTA.addAction(self.actionNew_Project)
        self.menuANANTA.addAction(self.actionOpen_Project)
        self.menubar.addAction(self.menuANANTA.menuAction())
        self.toolBar.addAction(self.actionAddFlProfile)
        self.toolBar.addAction(self.actionDataCleaningProfile)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actionNew_Project.triggered.connect(MainWindow.openNewProjectDialog)
        self.actionOpen_Project.triggered.connect(MainWindow.openOpenProjectDialog)
        self.actionAddFlProfile.triggered.connect(MainWindow.addFlProfile)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.miningProfLbl.setText(_translate("MainWindow", "MINING PROFILE - ANANTA1", None))
        self.menuANANTA.setTitle(_translate("MainWindow", "ANANTA", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionAddFlProfile.setText(_translate("MainWindow", "File Loading Profile", None))
        self.actionAddFlProfile.setToolTip(_translate("MainWindow", "Adds a new file loading profile", None))
        self.actionDataCleaningProfile.setText(_translate("MainWindow", "Data Cleaning Profile", None))
        self.actionDataCleaningProfile.setToolTip(_translate("MainWindow", "Adds a new Data Cleaning Profile", None))
        self.actionNew_Project.setText(_translate("MainWindow", "New Project", None))
        self.actionOpen_Project.setText(_translate("MainWindow", "Open Project", None))

