# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/lakmal/Desktop/AnantaUI/newprojectdialog.ui'
#
# Created: Thu Nov  6 18:28:27 2014
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

class Ui_newProjectDialog(object):
    def setupUi(self, newProjectDialog):
        newProjectDialog.setObjectName(_fromUtf8("newProjectDialog"))
        newProjectDialog.resize(365, 133)
        self.newProjButtonBox = QtGui.QDialogButtonBox(newProjectDialog)
        self.newProjButtonBox.setGeometry(QtCore.QRect(20, 80, 321, 32))
        self.newProjButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.newProjButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.newProjButtonBox.setObjectName(_fromUtf8("newProjButtonBox"))
        self.projNameLbl = QtGui.QLabel(newProjectDialog)
        self.projNameLbl.setGeometry(QtCore.QRect(40, 36, 101, 21))
        self.projNameLbl.setObjectName(_fromUtf8("projNameLbl"))
        self.projectNameLineEdit = QtGui.QLineEdit(newProjectDialog)
        self.projectNameLineEdit.setGeometry(QtCore.QRect(160, 30, 181, 27))
        self.projectNameLineEdit.setObjectName(_fromUtf8("projectNameLineEdit"))

        self.retranslateUi(newProjectDialog)
        QtCore.QObject.connect(self.newProjButtonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), newProjectDialog.accept)
        QtCore.QObject.connect(self.newProjButtonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), newProjectDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(newProjectDialog)

    def retranslateUi(self, newProjectDialog):
        newProjectDialog.setWindowTitle(_translate("newProjectDialog", "Dialog", None))
        self.projNameLbl.setText(_translate("newProjectDialog", "Project Name", None))

