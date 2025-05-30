# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'monthly_analysis.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MonthlyAnalysisForm(object):
    def setupUi(self, MonthlyAnalysisForm):
        if not MonthlyAnalysisForm.objectName():
            MonthlyAnalysisForm.setObjectName(u"MonthlyAnalysisForm")
        MonthlyAnalysisForm.resize(800, 600)
        self.verticalLayout = QVBoxLayout(MonthlyAnalysisForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_month = QHBoxLayout()
        self.horizontalLayout_month.setObjectName(u"horizontalLayout_month")
        self.label_month = QLabel(MonthlyAnalysisForm)
        self.label_month.setObjectName(u"label_month")

        self.horizontalLayout_month.addWidget(self.label_month)

        self.combo_month = QComboBox(MonthlyAnalysisForm)
        self.combo_month.setObjectName(u"combo_month")

        self.horizontalLayout_month.addWidget(self.combo_month)


        self.verticalLayout.addLayout(self.horizontalLayout_month)

        self.textEdit_summary = QTextEdit(MonthlyAnalysisForm)
        self.textEdit_summary.setObjectName(u"textEdit_summary")
        self.textEdit_summary.setReadOnly(True)
        self.textEdit_summary.setMinimumHeight(150)

        self.verticalLayout.addWidget(self.textEdit_summary)

        self.plot_widget = QWidget(MonthlyAnalysisForm)
        self.plot_widget.setObjectName(u"plot_widget")
        self.plot_widget.setMinimumHeight(250)

        self.verticalLayout.addWidget(self.plot_widget)

        self.btn_back = QPushButton(MonthlyAnalysisForm)
        self.btn_back.setObjectName(u"btn_back")

        self.verticalLayout.addWidget(self.btn_back)


        self.retranslateUi(MonthlyAnalysisForm)

        QMetaObject.connectSlotsByName(MonthlyAnalysisForm)
    # setupUi

    def retranslateUi(self, MonthlyAnalysisForm):
        MonthlyAnalysisForm.setWindowTitle(QCoreApplication.translate("MonthlyAnalysisForm", u"Monthly Analysis", None))
        self.label_month.setText(QCoreApplication.translate("MonthlyAnalysisForm", u"Select Month:", None))
        self.textEdit_summary.setPlaceholderText(QCoreApplication.translate("MonthlyAnalysisForm", u"Summary will appear here", None))
        self.btn_back.setText(QCoreApplication.translate("MonthlyAnalysisForm", u"Back", None))
    # retranslateUi

