
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Question(object):
    def setupUi(self, Question):
        if not Question.objectName():
            Question.setObjectName(u"Question")
        Question.resize(420, 450)
        Question.setMinimumSize(QSize(420, 450))
        Question.setMaximumSize(QSize(420, 450))
        self.primary_widget = QWidget(Question)
        self.primary_widget.setObjectName(u"primary_widget")
        self.sec_wig = QFrame(self.primary_widget)
        self.sec_wig.setObjectName(u"sec_wig")
        self.sec_wig.setGeometry(QRect(0, 0, 420, 450))
        font = QFont()
        font.setFamily(u"Consolas")
        font.setPointSize(10)
        self.sec_wig.setFont(font)
        self.sec_wig.setFrameShape(QFrame.StyledPanel)
        self.sec_wig.setFrameShadow(QFrame.Raised)
        self.ques_table = QTableWidget(self.sec_wig)
        if (self.ques_table.columnCount() < 1):
            self.ques_table.setColumnCount(1)
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.ques_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.ques_table.rowCount() < 12):
            self.ques_table.setRowCount(12)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.ques_table.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.ques_table.setItem(0, 0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.ques_table.setItem(1, 0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.ques_table.setItem(2, 0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.ques_table.setItem(3, 0, __qtablewidgetitem5)
        self.ques_table.setObjectName(u"ques_table")
        self.ques_table.setGeometry(QRect(10, 0, 291, 401))
        self.ques_table.setGridStyle(Qt.NoPen)
        self.ques_table.setSortingEnabled(False)
        self.ques_table.setWordWrap(False)
        self.ques_table.setRowCount(12)
        self.ques_table.horizontalHeader().setCascadingSectionResizes(False)
        self.ques_table.horizontalHeader().setProperty("showSortIndicator", False)
        self.ques_table.horizontalHeader().setStretchLastSection(True)
        self.widget = QWidget(self.sec_wig)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(320, 10, 83, 54))
        self.q_layout = QFormLayout(self.widget)
        self.q_layout.setObjectName(u"q_layout")
        self.q_layout.setContentsMargins(0, 0, 0, 0)
        self.q_ok_btn = QPushButton(self.widget)
        self.q_ok_btn.setObjectName(u"q_ok_btn")

        self.q_layout.setWidget(0, QFormLayout.LabelRole, self.q_ok_btn)

        self.q_cancel_btn = QPushButton(self.widget)
        self.q_cancel_btn.setObjectName(u"q_cancel_btn")

        self.q_layout.setWidget(1, QFormLayout.LabelRole, self.q_cancel_btn)

        Question.setCentralWidget(self.primary_widget)
        self.menubar = QMenuBar(Question)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 420, 21))
        Question.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Question)
        self.statusbar.setObjectName(u"statusbar")
        Question.setStatusBar(self.statusbar)

        self.retranslateUi(Question)

        QMetaObject.connectSlotsByName(Question)
    # setupUi

    def retranslateUi(self, Question):
        Question.setWindowTitle(QCoreApplication.translate("Question", u"Question Window", None))
        ___qtablewidgetitem = self.ques_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Question", u"QUESTION", None));
        ___qtablewidgetitem1 = self.ques_table.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Question", u"1", None));

        __sortingEnabled = self.ques_table.isSortingEnabled()
        self.ques_table.setSortingEnabled(False)
        self.ques_table.setSortingEnabled(__sortingEnabled)

        self.q_ok_btn.setText(QCoreApplication.translate("Question", u"OK", None))
        self.q_cancel_btn.setText(QCoreApplication.translate("Question", u"Cancel", None))
    # retranslateUi

