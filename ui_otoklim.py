# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'otoklim_dialog_base.ui'
#
# Created: Mon Jul 03 13:07:11 2017
#      by: PyQt4 UI code generator 4.10.2
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

class Ui_OtoklimDialogBase(object):
    def setupUi(self, OtoklimDialogBase):
        OtoklimDialogBase.setObjectName(_fromUtf8("OtoklimDialogBase"))
        OtoklimDialogBase.resize(498, 592)
        self.verticalLayout = QtGui.QVBoxLayout(OtoklimDialogBase)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame_2 = QtGui.QFrame(OtoklimDialogBase)
        self.frame_2.setFrameShape(QtGui.QFrame.Box)
        self.frame_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayout_9 = QtGui.QGridLayout(self.frame_2)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.groupBox_2 = QtGui.QGroupBox(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAutoFillBackground(False)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.Input_CH_CSV = QtGui.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Input_CH_CSV.setFont(font)
        self.Input_CH_CSV.setDragEnabled(True)
        self.Input_CH_CSV.setObjectName(_fromUtf8("Input_CH_CSV"))
        self.gridLayout.addWidget(self.Input_CH_CSV, 0, 1, 1, 1)
        self.Browse_CH_CSV = QtGui.QPushButton(self.groupBox_2)
        self.Browse_CH_CSV.setMaximumSize(QtCore.QSize(50, 25))
        self.Browse_CH_CSV.setObjectName(_fromUtf8("Browse_CH_CSV"))
        self.gridLayout.addWidget(self.Browse_CH_CSV, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.input_csv = QtGui.QLineEdit(self.groupBox_2)
        self.input_csv.setMaximumSize(QtCore.QSize(25, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.input_csv.setFont(font)
        self.input_csv.setText(_fromUtf8(""))
        self.input_csv.setMaxLength(1)
        self.input_csv.setDragEnabled(True)
        self.input_csv.setObjectName(_fromUtf8("input_csv"))
        self.gridLayout.addWidget(self.input_csv, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.Heuristic = QtGui.QComboBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Heuristic.setFont(font)
        self.Heuristic.setObjectName(_fromUtf8("Heuristic"))
        self.Heuristic.addItem(_fromUtf8(""))
        self.Heuristic.addItem(_fromUtf8(""))
        self.Heuristic.addItem(_fromUtf8(""))
        self.Heuristic.addItem(_fromUtf8(""))
        self.Heuristic.addItem(_fromUtf8(""))
        self.Heuristic.addItem(_fromUtf8(""))
        self.Heuristic.addItem(_fromUtf8(""))
        self.Heuristic.addItem(_fromUtf8(""))
        self.Heuristic.addItem(_fromUtf8(""))
        self.Heuristic.addItem(_fromUtf8(""))
        self.Heuristic.addItem(_fromUtf8(""))
        self.Heuristic.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.Heuristic, 2, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.input_year = QtGui.QLineEdit(self.groupBox_2)
        self.input_year.setMaximumSize(QtCore.QSize(65, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.input_year.setFont(font)
        self.input_year.setText(_fromUtf8(""))
        self.input_year.setMaxLength(4)
        self.input_year.setDragEnabled(True)
        self.input_year.setObjectName(_fromUtf8("input_year"))
        self.gridLayout.addWidget(self.input_year, 3, 1, 1, 1)
        self.line = QtGui.QFrame(self.groupBox_2)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 4, 0, 1, 3)
        self.label_9 = QtGui.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 5, 0, 1, 1)
        self.mode_1 = QtGui.QRadioButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.mode_1.setFont(font)
        self.mode_1.setChecked(True)
        self.mode_1.setObjectName(_fromUtf8("mode_1"))
        self.gridLayout.addWidget(self.mode_1, 6, 0, 1, 1)
        self.mode_2 = QtGui.QRadioButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.mode_2.setFont(font)
        self.mode_2.setObjectName(_fromUtf8("mode_2"))
        self.gridLayout.addWidget(self.mode_2, 7, 0, 1, 1)
        self.mode_3 = QtGui.QRadioButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.mode_3.setFont(font)
        self.mode_3.setObjectName(_fromUtf8("mode_3"))
        self.gridLayout.addWidget(self.mode_3, 8, 0, 1, 1)
        self.mode_4 = QtGui.QRadioButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.mode_4.setFont(font)
        self.mode_4.setObjectName(_fromUtf8("mode_4"))
        self.gridLayout.addWidget(self.mode_4, 9, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtGui.QFrame(OtoklimDialogBase)
        self.frame_3.setEnabled(False)
        self.frame_3.setFrameShape(QtGui.QFrame.Box)
        self.frame_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.listView_menu = QtGui.QListView(self.frame_3)
        self.listView_menu.setObjectName(_fromUtf8("listView_menu"))
        self.horizontalLayout.addWidget(self.listView_menu)
        self.widget = QtGui.QWidget(self.frame_3)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.moveSelected = QtGui.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.moveSelected.setFont(font)
        self.moveSelected.setObjectName(_fromUtf8("moveSelected"))
        self.verticalLayout_2.addWidget(self.moveSelected)
        self.moveUnselected = QtGui.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.moveUnselected.setFont(font)
        self.moveUnselected.setObjectName(_fromUtf8("moveUnselected"))
        self.verticalLayout_2.addWidget(self.moveUnselected)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.widget)
        self.listView_selected = QtGui.QListView(self.frame_3)
        self.listView_selected.setObjectName(_fromUtf8("listView_selected"))
        self.horizontalLayout.addWidget(self.listView_selected)
        self.verticalLayout.addWidget(self.frame_3)
        self.button_box = QtGui.QDialogButtonBox(OtoklimDialogBase)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.verticalLayout.addWidget(self.button_box)

        self.retranslateUi(OtoklimDialogBase)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), OtoklimDialogBase.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), OtoklimDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(OtoklimDialogBase)

    def retranslateUi(self, OtoklimDialogBase):
        OtoklimDialogBase.setWindowTitle(_translate("OtoklimDialogBase", "Otoklim", None))
        self.groupBox_2.setTitle(_translate("OtoklimDialogBase", "Determine input Data, Mode And Parameter :", None))
        self.label.setText(_translate("OtoklimDialogBase", "Input CH File (CSV)", None))
        self.Browse_CH_CSV.setText(_translate("OtoklimDialogBase", "....", None))
        self.label_2.setText(_translate("OtoklimDialogBase", "Choose CSV Delimiter", None))
        self.label_3.setText(_translate("OtoklimDialogBase", "This Month", None))
        self.Heuristic.setItemText(0, _translate("OtoklimDialogBase", "Januari", None))
        self.Heuristic.setItemText(1, _translate("OtoklimDialogBase", "Februari", None))
        self.Heuristic.setItemText(2, _translate("OtoklimDialogBase", "Maret", None))
        self.Heuristic.setItemText(3, _translate("OtoklimDialogBase", "April", None))
        self.Heuristic.setItemText(4, _translate("OtoklimDialogBase", "Mei", None))
        self.Heuristic.setItemText(5, _translate("OtoklimDialogBase", "Juni", None))
        self.Heuristic.setItemText(6, _translate("OtoklimDialogBase", "Juli", None))
        self.Heuristic.setItemText(7, _translate("OtoklimDialogBase", "Agustus", None))
        self.Heuristic.setItemText(8, _translate("OtoklimDialogBase", "September", None))
        self.Heuristic.setItemText(9, _translate("OtoklimDialogBase", "Oktober", None))
        self.Heuristic.setItemText(10, _translate("OtoklimDialogBase", "November", None))
        self.Heuristic.setItemText(11, _translate("OtoklimDialogBase", "Desember", None))
        self.label_4.setText(_translate("OtoklimDialogBase", "This Year", None))
        self.label_9.setText(_translate("OtoklimDialogBase", "Choose Mode :", None))
        self.mode_1.setText(_translate("OtoklimDialogBase", "Jawa Timur Province Only", None))
        self.mode_2.setText(_translate("OtoklimDialogBase", "All Kabupaten Kota", None))
        self.mode_3.setText(_translate("OtoklimDialogBase", "All Kecamatan", None))
        self.mode_4.setText(_translate("OtoklimDialogBase", "Selected Region", None))
        self.moveSelected.setText(_translate("OtoklimDialogBase", ">", None))
        self.moveUnselected.setText(_translate("OtoklimDialogBase", "<", None))
