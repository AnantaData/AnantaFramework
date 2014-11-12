from PyQt4.QtGui import QWidget
from ananta_views import  file_load_prof_widget_view
import set_params_dialog
from ananta_profile import  profile_finder

class FileLoadProfWidget(QWidget):

    def __init__(self, parent=None):
        super(FileLoadProfWidget, self).__init__(parent)
        self.main_window_ui = file_load_prof_widget_view.Ui_fileLoadProfWidget()
        self.main_window_ui.setupUi(self)

    def openSetParamsDialog(self):
        self.paramsDialog = set_params_dialog.SetParamsDialog(self)
        fileName = self.profileName+".xml"
        no = self.index
        self.paramsDialog.ui.textEdit.setText(profile_finder.getProfileTag(str(fileName),no))
        self.paramsDialog.exec_()




