from PyQt4.QtGui import QDialog
from ananta_views import set_params_dialog_view
from ananta_profile import profile_finder
__author__ = 'lakmal'



class SetParamsDialog(QDialog):

    def __init__(self,parent =None):
        super(QDialog,self).__init__(parent)
        self.ui = set_params_dialog_view.Ui_Dialog()
        self.ui.setupUi(self)

    def accept(self):
        tag = self.ui.textEdit.toPlainText()
        fileName = self.parent().profileName+".xml"
        no = self.parent().index
        profile_finder.setProfileTag(str(fileName),no,str(tag))
        super(SetParamsDialog,self).accept()