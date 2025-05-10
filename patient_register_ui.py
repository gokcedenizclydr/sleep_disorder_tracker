from PySide6 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(739, 671)

        self.lineEdit_name = QtWidgets.QLineEdit(Form)
        self.lineEdit_name.setGeometry(QtCore.QRect(20, 10, 200, 21))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_name.setPlaceholderText("Enter full name")

        self.lineEdit_age = QtWidgets.QLineEdit(Form)
        self.lineEdit_age.setGeometry(QtCore.QRect(20, 40, 200, 21))
        self.lineEdit_age.setObjectName("lineEdit_age")
        self.lineEdit_age.setPlaceholderText("Enter age")

        self.lineEdit_height = QtWidgets.QLineEdit(Form)
        self.lineEdit_height.setGeometry(QtCore.QRect(20, 70, 200, 21))
        self.lineEdit_height.setObjectName("lineEdit_height")
        self.lineEdit_height.setPlaceholderText("Enter height (cm)")

        self.lineEdit_weight = QtWidgets.QLineEdit(Form)
        self.lineEdit_weight.setGeometry(QtCore.QRect(20, 100, 200, 21))
        self.lineEdit_weight.setObjectName("lineEdit_weight")
        self.lineEdit_weight.setPlaceholderText("Enter weight (kg)")

        self.comboBox_gender = QtWidgets.QComboBox(Form)
        self.comboBox_gender.setGeometry(QtCore.QRect(20, 140, 200, 22))
        self.comboBox_gender.setObjectName("comboBox_gender")
        self.comboBox_gender.addItems(["Select gender", "Male", "Female", "Prefer not to say"])

        self.comboBox_disorderType = QtWidgets.QComboBox(Form)
        self.comboBox_disorderType.setGeometry(QtCore.QRect(20, 180, 300, 22))
        self.comboBox_disorderType.setObjectName("comboBox_disorderType")
        self.comboBox_disorderType.addItems([
            "Select sleep disorder type",
            "Idiopathic hypersomnia",
            "Narcolepsy",
            "Obstructive sleep apnea",
            "REM sleep behavior disorder",
            "Restless legs syndrome",
            "Insomnia",
            "Circadian rhythm sleep disorder",
            "Parasomnia",
            "Other (please explain)"
        ])

        self.lineEdit_profession = QtWidgets.QLineEdit(Form)
        self.lineEdit_profession.setGeometry(QtCore.QRect(20, 220, 200, 21))
        self.lineEdit_profession.setObjectName("lineEdit_profession")
        self.lineEdit_profession.setPlaceholderText("Enter profession")

        self.lineEdit_otherDisorder = QtWidgets.QLineEdit(Form)
        self.lineEdit_otherDisorder.setGeometry(QtCore.QRect(340, 180, 200, 21))
        self.lineEdit_otherDisorder.setObjectName("lineEdit_otherDisorder")
        self.lineEdit_otherDisorder.setPlaceholderText("If 'Other', explain here")

        self.plainTextEdit_medications = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_medications.setGeometry(QtCore.QRect(20, 250, 520, 41))
        self.plainTextEdit_medications.setObjectName("plainTextEdit_medications")
        self.plainTextEdit_medications.setPlaceholderText("Medications & Doses")

        self.plainTextEdit_chronicDisease = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_chronicDisease.setGeometry(QtCore.QRect(20, 300, 520, 41))
        self.plainTextEdit_chronicDisease.setObjectName("plainTextEdit_chronicDisease")
        self.plainTextEdit_chronicDisease.setPlaceholderText("Chronic Diseases (if any)")

        self.plainTextEdit_initialNote = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_initialNote.setGeometry(QtCore.QRect(20, 350, 520, 60))
        self.plainTextEdit_initialNote.setObjectName("plainTextEdit_initialNote")
        self.plainTextEdit_initialNote.setPlaceholderText("Initial notes or comments")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(230, 430, 120, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Save Record")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Patient Register"))
