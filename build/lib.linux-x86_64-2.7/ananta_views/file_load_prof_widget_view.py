# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/lakmal/Desktop/AnantaUI/fileloadingprofile.ui'
#
# Created: Mon Nov  3 14:02:24 2014
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

class Ui_fileLoadProfWidget(object):
    def setupUi(self, fileLoadProfWidget):
        fileLoadProfWidget.setObjectName(_fromUtf8("fileLoadProfWidget"))
        fileLoadProfWidget.resize(280, 151)
        self.fileLoadProfShowPushButton = QtGui.QPushButton(fileLoadProfWidget)
        self.fileLoadProfShowPushButton.setGeometry(QtCore.QRect(190, 50, 81, 81))
        self.fileLoadProfShowPushButton.setObjectName(_fromUtf8("fileLoadProfShowPushButton"))
        self.fileLoadProfExecPushButton = QtGui.QPushButton(fileLoadProfWidget)
        self.fileLoadProfExecPushButton.setGeometry(QtCore.QRect(100, 50, 81, 81))
        self.fileLoadProfExecPushButton.setObjectName(_fromUtf8("fileLoadProfExecPushButton"))
        self.fileLoadProfLbl = QtGui.QLabel(fileLoadProfWidget)
        self.fileLoadProfLbl.setGeometry(QtCore.QRect(80, 10, 141, 21))
        self.fileLoadProfLbl.setObjectName(_fromUtf8("fileLoadProfLbl"))
        self.fileLoadingProfilePushButton = QtGui.QPushButton(fileLoadProfWidget)
        self.fileLoadingProfilePushButton.setGeometry(QtCore.QRect(10, 50, 81, 81))
        self.fileLoadingProfilePushButton.setObjectName(_fromUtf8("fileLoadingProfilePushButton"))

        self.retranslateUi(fileLoadProfWidget)
        QtCore.QMetaObject.connectSlotsByName(fileLoadProfWidget)
        self.fileLoadingProfilePushButton.clicked.connect(fileLoadProfWidget.openSetParamsDialog)

    def retranslateUi(self, fileLoadProfWidget):
        fileLoadProfWidget.setWindowTitle(_translate("fileLoadProfWidget", "Form", None))
        self.fileLoadProfShowPushButton.setText(_translate("fileLoadProfWidget", "Show", None))
        self.fileLoadProfExecPushButton.setText(_translate("fileLoadProfWidget", "Execute", None))
        self.fileLoadProfLbl.setText(_translate("fileLoadProfWidget", "File Loading Profile", None))
        self.fileLoadingProfilePushButton.setText(_translate("fileLoadProfWidget", "Profile", None))

