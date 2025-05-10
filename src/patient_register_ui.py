# patient_register_ui.py

# Bu dosya Qt Designer'dan oluşturulan arayüz kodunu içerir.

from PySide6 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(739, 671)

        self.lineEdit_name = QtWidgets.QLineEdit(Form)
        self.lineEdit_name.setGeometry(QtCore.QRect(20, 10, 113, 21))
        self.lineEdit_name.setObjectName("lineEdit_name")

        self.lineEdit_age = QtWidgets.QLineEdit(Form)
        self.lineEdit_age.setGeometry(QtCore.QRect(20, 40, 113, 21))
        self.lineEdit_age.setObjectName("lineEdit_age")

        self.lineEdit_height = QtWidgets.QLineEdit(Form)
        self.lineEdit_height.setGeometry(QtCore.QRect(20, 70, 113, 21))
        self.lineEdit_height.setObjectName("lineEdit_height")

        self.lineEdit_weight = QtWidgets.QLineEdit(Form)
        self.lineEdit_weight.setGeometry(QtCore.QRect(20, 100, 113, 21))
        self.lineEdit_weight.setObjectName("lineEdit_weight")

        self.comboBox_gender = QtWidgets.QComboBox(Form)
        self.comboBox_gender.setGeometry(QtCore.QRect(20, 140, 68, 22))
        self.comboBox_gender.setObjectName("comboBox_gender")
        self.comboBox_gender.addItem("Gender:")
        self.comboBox_gender.addItem("male")
        self.comboBox_gender.addItem("female")
        self.comboBox_gender.addItem("prefer not to say")

        self.comboBox_disorderType = QtWidgets.QComboBox(Form)
        self.comboBox_disorderType.setGeometry(QtCore.QRect(20, 180, 131, 22))
        self.comboBox_disorderType.setObjectName("comboBox_disorderType")
        self.comboBox_disorderType.addItems([
            "Sleep Disorder Type:",
            "idiopathic hypersomnia",
            "narcolepsy",
            "obstructive sleep apnea",
            "REM sleep behavior disorder",
            "restless legs syndrome",
            "insomnia",
            "circadian rhythm sleep disorder",
            "parasomnia",
            "other(if other,please explain)"
        ])

        self.lineEdit_profession = QtWidgets.QLineEdit(Form)
        self.lineEdit_profession.setGeometry(QtCore.QRect(20, 220, 113, 21))
        self.lineEdit_profession.setObjectName("lineEdit_profession")

        self.lineEdit_otherDisorder = QtWidgets.QLineEdit(Form)
        self.lineEdit_otherDisorder.setGeometry(QtCore.QRect(160, 180, 113, 21))
        self.lineEdit_otherDisorder.setObjectName("lineEdit_otherDisorder")

        self.plainTextEdit_medications = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_medications.setGeometry(QtCore.QRect(20, 250, 381, 41))
        self.plainTextEdit_medications.setObjectName("plainTextEdit_medications")

        self.plainTextEdit_chronicDisease = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_chronicDisease.setGeometry(QtCore.QRect(20, 300, 381, 41))
        self.plainTextEdit_chronicDisease.setObjectName("plainTextEdit_chronicDisease")

        self.plainTextEdit_initialNote = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_initialNote.setGeometry(QtCore.QRect(20, 350, 381, 41))
        self.plainTextEdit_initialNote.setObjectName("plainTextEdit_initialNote")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(240, 390, 75, 24))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit_name.setText(_translate("Form", "Full Name:"))
        self.lineEdit_age.setText(_translate("Form", "Age:"))
        self.lineEdit_height.setText(_translate("Form", "Height:"))
        self.lineEdit_weight.setText(_translate("Form", "Weight:"))
        self.lineEdit_profession.setText(_translate("Form", "Profession:"))
        self.plainTextEdit_medications.setPlainText(_translate("Form", "Medications&Doses:"))
        self.plainTextEdit_chronicDisease.setPlainText(_translate("Form", "Chronic Diseases:"))
        self.plainTextEdit_initialNote.setPlainText(_translate("Form", "Initial Note:"))
        self.pushButton.setText(_translate("Form", "Save record"))
