

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(985, 671)
        self.btn_register = QPushButton(Form)
        self.btn_register.setObjectName(u"btn_register")
        self.btn_register.setGeometry(QRect(330, 590, 211, 24))
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(30, 35, 841, 516))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 1)

        self.lineEdit_fullname = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_fullname.setObjectName(u"lineEdit_fullname")

        self.gridLayout.addWidget(self.lineEdit_fullname, 0, 1, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.lineEdit_age = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_age.setObjectName(u"lineEdit_age")

        self.gridLayout.addWidget(self.lineEdit_age, 1, 1, 1, 1)

        self.lineEdit_profession = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_profession.setObjectName(u"lineEdit_profession")

        self.gridLayout.addWidget(self.lineEdit_profession, 7, 1, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.comboBox_gender = QComboBox(self.gridLayoutWidget)
        self.comboBox_gender.addItem("")
        self.comboBox_gender.addItem("")
        self.comboBox_gender.addItem("")
        self.comboBox_gender.addItem("")
        self.comboBox_gender.setObjectName(u"comboBox_gender")

        self.gridLayout.addWidget(self.comboBox_gender, 4, 1, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)

        self.comboBox_disorder = QComboBox(self.gridLayoutWidget)
        self.comboBox_disorder.addItem("")
        self.comboBox_disorder.addItem("")
        self.comboBox_disorder.addItem("")
        self.comboBox_disorder.addItem("")
        self.comboBox_disorder.addItem("")
        self.comboBox_disorder.addItem("")
        self.comboBox_disorder.addItem("")
        self.comboBox_disorder.addItem("")
        self.comboBox_disorder.addItem("")
        self.comboBox_disorder.addItem("")
        self.comboBox_disorder.setObjectName(u"comboBox_disorder")

        self.gridLayout.addWidget(self.comboBox_disorder, 5, 1, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)

        self.lineEdit_height = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_height.setObjectName(u"lineEdit_height")

        self.gridLayout.addWidget(self.lineEdit_height, 2, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 9, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.lineEdit_weight = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_weight.setObjectName(u"lineEdit_weight")

        self.gridLayout.addWidget(self.lineEdit_weight, 3, 1, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.lineEdit_otherDisorder = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_otherDisorder.setObjectName(u"lineEdit_otherDisorder")

        self.gridLayout.addWidget(self.lineEdit_otherDisorder, 5, 2, 1, 1)

        self.textEdit_medications = QPlainTextEdit(self.gridLayoutWidget)
        self.textEdit_medications.setObjectName(u"textEdit_medications")

        self.gridLayout.addWidget(self.textEdit_medications, 6, 1, 1, 1)

        self.textEdit_chronic = QPlainTextEdit(self.gridLayoutWidget)
        self.textEdit_chronic.setObjectName(u"textEdit_chronic")

        self.gridLayout.addWidget(self.textEdit_chronic, 8, 1, 1, 1)

        self.textEdit_note = QPlainTextEdit(self.gridLayoutWidget)
        self.textEdit_note.setObjectName(u"textEdit_note")

        self.gridLayout.addWidget(self.textEdit_note, 9, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_register.setText(QCoreApplication.translate("Form", u"Save record", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Chronic Diseases:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Height :", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Medications&Doses :", None))
        self.comboBox_gender.setItemText(0, "")
        self.comboBox_gender.setItemText(1, QCoreApplication.translate("Form", u"male", None))
        self.comboBox_gender.setItemText(2, QCoreApplication.translate("Form", u"female", None))
        self.comboBox_gender.setItemText(3, QCoreApplication.translate("Form", u"prefer not to say", None))

        self.label_8.setText(QCoreApplication.translate("Form", u"Job :", None))
        self.comboBox_disorder.setItemText(0, "")
        self.comboBox_disorder.setItemText(1, QCoreApplication.translate("Form", u"idiopathic hypersomnia", None))
        self.comboBox_disorder.setItemText(2, QCoreApplication.translate("Form", u"narcolepsy", None))
        self.comboBox_disorder.setItemText(3, QCoreApplication.translate("Form", u"obstructive sleep apnea", None))
        self.comboBox_disorder.setItemText(4, QCoreApplication.translate("Form", u"REM sleep behavior disorder", None))
        self.comboBox_disorder.setItemText(5, QCoreApplication.translate("Form", u"restless legs sydrome", None))
        self.comboBox_disorder.setItemText(6, QCoreApplication.translate("Form", u"insomnia", None))
        self.comboBox_disorder.setItemText(7, QCoreApplication.translate("Form", u"circadian rhythm sleep disorder", None))
        self.comboBox_disorder.setItemText(8, QCoreApplication.translate("Form", u"parasomnia", None))
        self.comboBox_disorder.setItemText(9, QCoreApplication.translate("Form", u"other(if other,please explain)", None))

        self.label.setText(QCoreApplication.translate("Form", u"Gender :", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Sleep Disorder Type :", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Full Name :", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Initial Note (optional) :", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Age :", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Weight :", None))
    # retranslateUi

