# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer_gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(811, 570)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 360, 811, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.testlabel2 = QtWidgets.QLabel(Dialog)
        self.testlabel2.setGeometry(QtCore.QRect(20, 20, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.testlabel2.setFont(font)
        self.testlabel2.setObjectName("testlabel2")
        self.testImage = QtWidgets.QLabel(Dialog)
        self.testImage.setGeometry(QtCore.QRect(20, 50, 300, 300))
        self.testImage.setFrameShape(QtWidgets.QFrame.Box)
        self.testImage.setFrameShadow(QtWidgets.QFrame.Plain)
        self.testImage.setText("")
        self.testImage.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.testImage.setObjectName("testImage")
        self.resImage = QtWidgets.QLabel(Dialog)
        self.resImage.setEnabled(False)
        self.resImage.setGeometry(QtCore.QRect(10, 410, 150, 150))
        self.resImage.setFrameShape(QtWidgets.QFrame.Box)
        self.resImage.setText("")
        self.resImage.setObjectName("resImage")
        self.resImage_2 = QtWidgets.QLabel(Dialog)
        self.resImage_2.setEnabled(False)
        self.resImage_2.setGeometry(QtCore.QRect(170, 410, 150, 150))
        self.resImage_2.setFrameShape(QtWidgets.QFrame.Box)
        self.resImage_2.setText("")
        self.resImage_2.setObjectName("resImage_2")
        self.resImage_3 = QtWidgets.QLabel(Dialog)
        self.resImage_3.setEnabled(False)
        self.resImage_3.setGeometry(QtCore.QRect(330, 410, 150, 150))
        self.resImage_3.setFrameShape(QtWidgets.QFrame.Box)
        self.resImage_3.setText("")
        self.resImage_3.setObjectName("resImage_3")
        self.resImage_4 = QtWidgets.QLabel(Dialog)
        self.resImage_4.setEnabled(False)
        self.resImage_4.setGeometry(QtCore.QRect(490, 410, 150, 150))
        self.resImage_4.setFrameShape(QtWidgets.QFrame.Box)
        self.resImage_4.setText("")
        self.resImage_4.setObjectName("resImage_4")
        self.resImage_5 = QtWidgets.QLabel(Dialog)
        self.resImage_5.setEnabled(False)
        self.resImage_5.setGeometry(QtCore.QRect(650, 410, 150, 150))
        self.resImage_5.setFrameShape(QtWidgets.QFrame.Box)
        self.resImage_5.setText("")
        self.resImage_5.setObjectName("resImage_5")
        self.randomizeButton = QtWidgets.QPushButton(Dialog)
        self.randomizeButton.setGeometry(QtCore.QRect(690, 290, 101, 23))
        self.randomizeButton.setObjectName("randomizeButton")
        self.matchLabel = QtWidgets.QLabel(Dialog)
        self.matchLabel.setGeometry(QtCore.QRect(10, 390, 47, 13))
        self.matchLabel.setObjectName("matchLabel")
        self.matchLabel_2 = QtWidgets.QLabel(Dialog)
        self.matchLabel_2.setGeometry(QtCore.QRect(170, 390, 47, 13))
        self.matchLabel_2.setObjectName("matchLabel_2")
        self.matchLabel_3 = QtWidgets.QLabel(Dialog)
        self.matchLabel_3.setGeometry(QtCore.QRect(330, 390, 47, 13))
        self.matchLabel_3.setObjectName("matchLabel_3")
        self.matchLabel_4 = QtWidgets.QLabel(Dialog)
        self.matchLabel_4.setGeometry(QtCore.QRect(490, 390, 47, 13))
        self.matchLabel_4.setObjectName("matchLabel_4")
        self.matchLabel_5 = QtWidgets.QLabel(Dialog)
        self.matchLabel_5.setGeometry(QtCore.QRect(650, 390, 47, 13))
        self.matchLabel_5.setObjectName("matchLabel_5")
        self.matchRate = QtWidgets.QLabel(Dialog)
        self.matchRate.setGeometry(QtCore.QRect(110, 390, 47, 13))
        self.matchRate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.matchRate.setObjectName("matchRate")
        self.matchRate_2 = QtWidgets.QLabel(Dialog)
        self.matchRate_2.setGeometry(QtCore.QRect(270, 390, 47, 13))
        self.matchRate_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.matchRate_2.setObjectName("matchRate_2")
        self.matchRate_3 = QtWidgets.QLabel(Dialog)
        self.matchRate_3.setGeometry(QtCore.QRect(430, 390, 47, 13))
        self.matchRate_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.matchRate_3.setObjectName("matchRate_3")
        self.matchRate_4 = QtWidgets.QLabel(Dialog)
        self.matchRate_4.setGeometry(QtCore.QRect(590, 390, 47, 13))
        self.matchRate_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.matchRate_4.setObjectName("matchRate_4")
        self.matchRate_5 = QtWidgets.QLabel(Dialog)
        self.matchRate_5.setGeometry(QtCore.QRect(750, 390, 47, 13))
        self.matchRate_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.matchRate_5.setObjectName("matchRate_5")
        self.loadDatabaseButton = QtWidgets.QPushButton(Dialog)
        self.loadDatabaseButton.setGeometry(QtCore.QRect(690, 20, 101, 23))
        self.loadDatabaseButton.setObjectName("loadDatabaseButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(350, 10, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(350, 190, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(660, 0, 21, 371))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(330, 0, 20, 371))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(340, 30, 331, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(340, 180, 331, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(Dialog)
        self.line_6.setGeometry(QtCore.QRect(340, 220, 331, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.loadImageButton = QtWidgets.QPushButton(Dialog)
        self.loadImageButton.setGeometry(QtCore.QRect(690, 110, 101, 23))
        self.loadImageButton.setObjectName("loadImageButton")
        self.batchProcessButton = QtWidgets.QPushButton(Dialog)
        self.batchProcessButton.setGeometry(QtCore.QRect(690, 260, 101, 23))
        self.batchProcessButton.setObjectName("batchProcessButton")
        self.loadDirectoryButton = QtWidgets.QPushButton(Dialog)
        self.loadDirectoryButton.setGeometry(QtCore.QRect(690, 80, 101, 23))
        self.loadDirectoryButton.setObjectName("loadDirectoryButton")
        self.currentDirLabel = QtWidgets.QLabel(Dialog)
        self.currentDirLabel.setGeometry(QtCore.QRect(350, 240, 311, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.currentDirLabel.setFont(font)
        self.currentDirLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.currentDirLabel.setWordWrap(True)
        self.currentDirLabel.setObjectName("currentDirLabel")
        self.currentDbLabel = QtWidgets.QLabel(Dialog)
        self.currentDbLabel.setGeometry(QtCore.QRect(350, 50, 311, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.currentDbLabel.setFont(font)
        self.currentDbLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.currentDbLabel.setWordWrap(True)
        self.currentDbLabel.setObjectName("currentDbLabel")
        self.saveDbButton = QtWidgets.QPushButton(Dialog)
        self.saveDbButton.setGeometry(QtCore.QRect(690, 50, 101, 23))
        self.saveDbButton.setObjectName("saveDbButton")
        self.cosRadioButton = QtWidgets.QRadioButton(Dialog)
        self.cosRadioButton.setGeometry(QtCore.QRect(690, 170, 101, 17))
        self.cosRadioButton.setChecked(True)
        self.cosRadioButton.setObjectName("cosRadioButton")
        self.euclidRadioButton = QtWidgets.QRadioButton(Dialog)
        self.euclidRadioButton.setGeometry(QtCore.QRect(690, 190, 111, 17))
        self.euclidRadioButton.setObjectName("euclidRadioButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Tubes Kenal Muka - Awoo-Bot"))
        self.testlabel2.setText(_translate("Dialog", "Test Image - Label"))
        self.randomizeButton.setText(_translate("Dialog", "Randomize"))
        self.matchLabel.setText(_translate("Dialog", "Match 1"))
        self.matchLabel_2.setText(_translate("Dialog", "Match 2"))
        self.matchLabel_3.setText(_translate("Dialog", "Match 3"))
        self.matchLabel_4.setText(_translate("Dialog", "Match 4"))
        self.matchLabel_5.setText(_translate("Dialog", "Match 5"))
        self.matchRate.setText(_translate("Dialog", "-"))
        self.matchRate_2.setText(_translate("Dialog", "-"))
        self.matchRate_3.setText(_translate("Dialog", "-"))
        self.matchRate_4.setText(_translate("Dialog", "-"))
        self.matchRate_5.setText(_translate("Dialog", "-"))
        self.loadDatabaseButton.setText(_translate("Dialog", "Load Database"))
        self.label.setText(_translate("Dialog", "Current Database"))
        self.label_2.setText(_translate("Dialog", "Current Directory"))
        self.loadImageButton.setText(_translate("Dialog", "Load Image"))
        self.batchProcessButton.setText(_translate("Dialog", "Batch Process"))
        self.loadDirectoryButton.setText(_translate("Dialog", "Load Directory"))
        self.currentDirLabel.setText(_translate("Dialog", "No Directory selected"))
        self.currentDbLabel.setText(_translate("Dialog", "No Database selected. Load database first, or load directory then batch process to load to RAM."))
        self.saveDbButton.setText(_translate("Dialog", "Save Database"))
        self.cosRadioButton.setText(_translate("Dialog", "Cosine Similarity"))
        self.euclidRadioButton.setText(_translate("Dialog", "Euclidean Distance"))
