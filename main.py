from PySide2 import QtWidgets
from App import ques
from App import createit
from PySide2 import QtCore
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import os
import sys
import datetime
from datetime import timedelta


class CreateFile(QtWidgets.QMainWindow):
    def __init__(self, folder_path, time_delta, lang):
        super(CreateFile, self).__init__()
        self.ques_with_ext = None
        self.folder_path = folder_path
        self.time_delta = time_delta
        self.lang = lang
        global temp_ques
        self.question_list = temp_ques
        self.name = None
        self.dirName(self.time_delta)
        self.createDir()
        self.strip_split_name()
        self.create_file_final()
        self.successful()
        sys.exit()

    def dirName(self, delta):
        dir_date = datetime.datetime.now()
        dir_date = (dir_date - timedelta(days=delta))
        dir_date = dir_date.strftime("%d_%b_%Y")
        dir_date = str(dir_date)
        self.name = dir_date


    def strip_split_name(self):
        name = self.question_list
        ext = self.lang
        x = []

        for i in name:
            a = i.strip()
            a = a.split()
            x.append('_'.join(a)+self.lang)
        self.ques_with_ext = x

    def create_file_final(self):
        file_f = self.ques_with_ext
        for i in file_f:
            self.File_make(i)

    def successful(self):
        QMessageBox.information(self, "Success", "HURRAY! DONE")
        return None

    def createDir(self):
        os.chdir(self.folder_path)
        try:
            os.mkdir(self.name)
        except OSError:
            pass
        os.chdir(self.name)

    @staticmethod
    def File_make(a):
        f = open(a, "w")
        f.write("")
        f.close()


class Ques_window(ques.Ui_Question, QtWidgets.QMainWindow):
    def __init__(self):
        super(Ques_window, self).__init__()
        self.ques_list = []
        self.setupUi(self)
        self.q_ok_btn.clicked.connect(self.ques_finding)
        self.q_cancel_btn.clicked.connect(self.ToClose)

    def ToClose(self):
        self.close()

    def ques_finding(self):
        global temp_ques
        for i in range(12):
            t = self.ques_table.item(i, 0)
            if t and len(t.text()):
                self.ques_list.append(t.text())
        temp_ques = self.ques_list
        self.close()


class MyQtApp(createit.Ui_CreateIt, QtWidgets.QMainWindow):
    def __init__(self):
        # variable
        self.fileCretion = None
        self.q_win = None
        self.language = '.cpp'
        self.path_of_folder = None
        self.time_delta = None
        # -------
        super(MyQtApp, self).__init__()
        self.setupUi(self)
        self.browse.clicked.connect(self.browse_folder)
        regexp = QtCore.QRegExp('^[0-9]*$')
        validator = QRegExpValidator(regexp)
        self.time_delta_input.setValidator(validator)
        self.cplus.setChecked(True)
        self.cplus.clicked.connect(self.set_cplus)
        self.java.clicked.connect(self.set_java)
        self.python.clicked.connect(self.set_python)
        self.add_file_btn.clicked.connect(self.open_add_window)
        self.create_btn.clicked.connect(self.create_submit)

    def create_submit(self):
        if self.validate_path():
            if self.get_time_delta():
                if self.validate_file_name():
                    self.fileCretion = CreateFile(self.path_of_folder, self.time_delta, self.language)

    def get_time_delta(self):
        value = self.time_delta_input.text()
        if value:
            self.time_delta = int(value)
            return True
        else:
            QMessageBox.information(self, 'INFO', 'ENTER VALID TIME DELTA')
            return False

    def validate_path(self):
        if self.path_of_folder:
            return True
        else:
            QMessageBox.information(self, 'INFO', 'PATH NOT SELECTED')
            return False

    def validate_file_name(self):
        if temp_ques:
            return True
        else:
            QMessageBox.information(self, 'INFO', 'ENTER FILE NAME : NO FILE NAME FOUND')
            return False

    def open_add_window(self):
        self.q_win = Ques_window()
        self.q_win.show()

    def set_cplus(self):
        self.language = '.cpp'

    def set_java(self):
        self.language = '.java'

    def set_python(self):
        self.language = '.py'

    def browse_folder(self):
        folder_path = QtWidgets.QFileDialog.getExistingDirectoryUrl(self,
                                                                    'Select Folder',
                                                                    )
        folder_path = folder_path.toString()
        folder_path = folder_path[8:]
        self.path_of_folder = folder_path
        self.input_path.setText(self.path_of_folder)


if __name__ == '__main__':
    temp_ques = None
    app = QtWidgets.QApplication()
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()
