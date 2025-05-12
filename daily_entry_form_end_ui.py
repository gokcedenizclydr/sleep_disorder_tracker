# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'daily_entry_form_endELkrjm.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPlainTextEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSpinBox, QTimeEdit,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(900, 616)
        self.verticalLayout_main = QVBoxLayout(Form)
        self.verticalLayout_main.setObjectName(u"verticalLayout_main")
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 868, 745))
        self.verticalLayout_scroll = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_scroll.setObjectName(u"verticalLayout_scroll")
        self.horizontalLayout_date = QHBoxLayout()
        self.horizontalLayout_date.setObjectName(u"horizontalLayout_date")
        self.spacer_left = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_date.addItem(self.spacer_left)

        self.label_date = QLabel(self.scrollAreaWidgetContents)
        self.label_date.setObjectName(u"label_date")

        self.horizontalLayout_date.addWidget(self.label_date)

        self.dateEdit = QDateEdit(self.scrollAreaWidgetContents)
        self.dateEdit.setObjectName(u"dateEdit")

        self.horizontalLayout_date.addWidget(self.dateEdit)

        self.spacer_right = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_date.addItem(self.spacer_right)


        self.verticalLayout_scroll.addLayout(self.horizontalLayout_date)

        self.groupBox_sleep = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_sleep.setObjectName(u"groupBox_sleep")
        self.gridLayout_sleep = QGridLayout(self.groupBox_sleep)
        self.gridLayout_sleep.setObjectName(u"gridLayout_sleep")
        self.label_sleep_time = QLabel(self.groupBox_sleep)
        self.label_sleep_time.setObjectName(u"label_sleep_time")

        self.gridLayout_sleep.addWidget(self.label_sleep_time, 0, 0, 1, 1)

        self.timeEdit_sleep = QTimeEdit(self.groupBox_sleep)
        self.timeEdit_sleep.setObjectName(u"timeEdit_sleep")

        self.gridLayout_sleep.addWidget(self.timeEdit_sleep, 0, 1, 1, 1)

        self.label_wake_time = QLabel(self.groupBox_sleep)
        self.label_wake_time.setObjectName(u"label_wake_time")

        self.gridLayout_sleep.addWidget(self.label_wake_time, 1, 0, 1, 1)

        self.timeEdit_wake = QTimeEdit(self.groupBox_sleep)
        self.timeEdit_wake.setObjectName(u"timeEdit_wake")

        self.gridLayout_sleep.addWidget(self.timeEdit_wake, 1, 1, 1, 1)

        self.label_quality = QLabel(self.groupBox_sleep)
        self.label_quality.setObjectName(u"label_quality")

        self.gridLayout_sleep.addWidget(self.label_quality, 2, 0, 1, 1)

        self.spinBox_quality = QSpinBox(self.groupBox_sleep)
        self.spinBox_quality.setObjectName(u"spinBox_quality")
        self.spinBox_quality.setMinimum(1)
        self.spinBox_quality.setMaximum(10)

        self.gridLayout_sleep.addWidget(self.spinBox_quality, 2, 1, 1, 1)


        self.verticalLayout_scroll.addWidget(self.groupBox_sleep)

        self.groupBox_medication = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_medication.setObjectName(u"groupBox_medication")
        self.verticalLayout_medication = QVBoxLayout(self.groupBox_medication)
        self.verticalLayout_medication.setObjectName(u"verticalLayout_medication")
        self.button_add_medication = QPushButton(self.groupBox_medication)
        self.button_add_medication.setObjectName(u"button_add_medication")

        self.verticalLayout_medication.addWidget(self.button_add_medication)

        self.medication_entries_layout = QVBoxLayout()
        self.medication_entries_layout.setObjectName(u"medication_entries_layout")

        self.verticalLayout_medication.addLayout(self.medication_entries_layout)


        self.verticalLayout_scroll.addWidget(self.groupBox_medication)

        self.groupBox_daily_state = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_daily_state.setObjectName(u"groupBox_daily_state")
        self.gridLayout_daily_state = QGridLayout(self.groupBox_daily_state)
        self.gridLayout_daily_state.setObjectName(u"gridLayout_daily_state")
        self.label_alertness = QLabel(self.groupBox_daily_state)
        self.label_alertness.setObjectName(u"label_alertness")

        self.gridLayout_daily_state.addWidget(self.label_alertness, 0, 0, 1, 1)

        self.spinBox_alertness = QSpinBox(self.groupBox_daily_state)
        self.spinBox_alertness.setObjectName(u"spinBox_alertness")

        self.gridLayout_daily_state.addWidget(self.spinBox_alertness, 0, 1, 1, 1)

        self.label_screen = QLabel(self.groupBox_daily_state)
        self.label_screen.setObjectName(u"label_screen")

        self.gridLayout_daily_state.addWidget(self.label_screen, 1, 0, 1, 1)

        self.spinBox_screen = QSpinBox(self.groupBox_daily_state)
        self.spinBox_screen.setObjectName(u"spinBox_screen")

        self.gridLayout_daily_state.addWidget(self.spinBox_screen, 1, 1, 1, 1)

        self.label_activity = QLabel(self.groupBox_daily_state)
        self.label_activity.setObjectName(u"label_activity")

        self.gridLayout_daily_state.addWidget(self.label_activity, 2, 0, 1, 1)

        self.combo_activity = QComboBox(self.groupBox_daily_state)
        self.combo_activity.addItem("")
        self.combo_activity.addItem("")
        self.combo_activity.addItem("")
        self.combo_activity.addItem("")
        self.combo_activity.setObjectName(u"combo_activity")

        self.gridLayout_daily_state.addWidget(self.combo_activity, 2, 1, 1, 1)

        self.label_stress = QLabel(self.groupBox_daily_state)
        self.label_stress.setObjectName(u"label_stress")

        self.gridLayout_daily_state.addWidget(self.label_stress, 3, 0, 1, 1)

        self.spinBox_stress = QSpinBox(self.groupBox_daily_state)
        self.spinBox_stress.setObjectName(u"spinBox_stress")

        self.gridLayout_daily_state.addWidget(self.spinBox_stress, 3, 1, 1, 1)

        self.label_mood = QLabel(self.groupBox_daily_state)
        self.label_mood.setObjectName(u"label_mood")

        self.gridLayout_daily_state.addWidget(self.label_mood, 4, 0, 1, 1)

        self.combo_mood = QComboBox(self.groupBox_daily_state)
        self.combo_mood.addItem("")
        self.combo_mood.addItem("")
        self.combo_mood.addItem("")
        self.combo_mood.setObjectName(u"combo_mood")

        self.gridLayout_daily_state.addWidget(self.combo_mood, 4, 1, 1, 1)

        self.label_meals = QLabel(self.groupBox_daily_state)
        self.label_meals.setObjectName(u"label_meals")

        self.gridLayout_daily_state.addWidget(self.label_meals, 5, 0, 1, 1)

        self.spinBox_meals = QSpinBox(self.groupBox_daily_state)
        self.spinBox_meals.setObjectName(u"spinBox_meals")

        self.gridLayout_daily_state.addWidget(self.spinBox_meals, 5, 1, 1, 1)

        self.label_smoking = QLabel(self.groupBox_daily_state)
        self.label_smoking.setObjectName(u"label_smoking")

        self.gridLayout_daily_state.addWidget(self.label_smoking, 6, 0, 1, 1)

        self.checkBox_smoke = QCheckBox(self.groupBox_daily_state)
        self.checkBox_smoke.setObjectName(u"checkBox_smoke")

        self.gridLayout_daily_state.addWidget(self.checkBox_smoke, 6, 1, 1, 1)

        self.lineEdit_smoke_detail = QLineEdit(self.groupBox_daily_state)
        self.lineEdit_smoke_detail.setObjectName(u"lineEdit_smoke_detail")

        self.gridLayout_daily_state.addWidget(self.lineEdit_smoke_detail, 7, 0, 1, 2)

        self.label_social = QLabel(self.groupBox_daily_state)
        self.label_social.setObjectName(u"label_social")

        self.gridLayout_daily_state.addWidget(self.label_social, 8, 0, 1, 1)

        self.combo_social = QComboBox(self.groupBox_daily_state)
        self.combo_social.addItem("")
        self.combo_social.addItem("")
        self.combo_social.addItem("")
        self.combo_social.addItem("")
        self.combo_social.setObjectName(u"combo_social")

        self.gridLayout_daily_state.addWidget(self.combo_social, 8, 1, 1, 1)

        self.label_caffeine = QLabel(self.groupBox_daily_state)
        self.label_caffeine.setObjectName(u"label_caffeine")

        self.gridLayout_daily_state.addWidget(self.label_caffeine, 9, 0, 1, 1)

        self.combo_caffeine = QComboBox(self.groupBox_daily_state)
        self.combo_caffeine.addItem("")
        self.combo_caffeine.addItem("")
        self.combo_caffeine.addItem("")
        self.combo_caffeine.addItem("")
        self.combo_caffeine.addItem("")
        self.combo_caffeine.addItem("")
        self.combo_caffeine.setObjectName(u"combo_caffeine")

        self.gridLayout_daily_state.addWidget(self.combo_caffeine, 9, 1, 1, 1)


        self.verticalLayout_scroll.addWidget(self.groupBox_daily_state)

        self.groupBox_summary = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_summary.setObjectName(u"groupBox_summary")
        self.verticalLayout_summary = QVBoxLayout(self.groupBox_summary)
        self.verticalLayout_summary.setObjectName(u"verticalLayout_summary")
        self.horizontalLayout_summary_feel = QHBoxLayout()
        self.horizontalLayout_summary_feel.setObjectName(u"horizontalLayout_summary_feel")
        self.label_summary_feel = QLabel(self.groupBox_summary)
        self.label_summary_feel.setObjectName(u"label_summary_feel")

        self.horizontalLayout_summary_feel.addWidget(self.label_summary_feel)

        self.combo_day_summary = QComboBox(self.groupBox_summary)
        self.combo_day_summary.addItem("")
        self.combo_day_summary.addItem("")
        self.combo_day_summary.addItem("")
        self.combo_day_summary.addItem("")
        self.combo_day_summary.setObjectName(u"combo_day_summary")

        self.horizontalLayout_summary_feel.addWidget(self.combo_day_summary)


        self.verticalLayout_summary.addLayout(self.horizontalLayout_summary_feel)

        self.textedit_daily_note = QPlainTextEdit(self.groupBox_summary)
        self.textedit_daily_note.setObjectName(u"textedit_daily_note")
        self.textedit_daily_note.setMinimumSize(QSize(0, 80))

        self.verticalLayout_summary.addWidget(self.textedit_daily_note)


        self.verticalLayout_scroll.addWidget(self.groupBox_summary)

        self.pushButton_save = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_save.setObjectName(u"pushButton_save")

        self.verticalLayout_scroll.addWidget(self.pushButton_save)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_main.addWidget(self.scrollArea)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Daily Entry Form", None))
        self.label_date.setText(QCoreApplication.translate("Form", u"Date:", None))
        self.groupBox_sleep.setTitle(QCoreApplication.translate("Form", u"Sleep Info", None))
        self.label_sleep_time.setText(QCoreApplication.translate("Form", u"Sleep Time :", None))
        self.label_wake_time.setText(QCoreApplication.translate("Form", u"Wake-up Time:", None))
        self.label_quality.setText(QCoreApplication.translate("Form", u"Sleep Quality :", None))
        self.groupBox_medication.setTitle(QCoreApplication.translate("Form", u"Medication", None))
        self.button_add_medication.setText(QCoreApplication.translate("Form", u"Add Medication", None))
        self.groupBox_daily_state.setTitle(QCoreApplication.translate("Form", u"Daily State", None))
        self.label_alertness.setText(QCoreApplication.translate("Form", u"Daytime alertness level:", None))
        self.label_screen.setText(QCoreApplication.translate("Form", u"Screen time (hours):", None))
        self.label_activity.setText(QCoreApplication.translate("Form", u"Physical activity level:", None))
        self.combo_activity.setItemText(0, QCoreApplication.translate("Form", u"none", None))
        self.combo_activity.setItemText(1, QCoreApplication.translate("Form", u"low", None))
        self.combo_activity.setItemText(2, QCoreApplication.translate("Form", u"moderate", None))
        self.combo_activity.setItemText(3, QCoreApplication.translate("Form", u"intense", None))

        self.label_stress.setText(QCoreApplication.translate("Form", u"Stress level:", None))
        self.label_mood.setText(QCoreApplication.translate("Form", u"Mood after waking:", None))
        self.combo_mood.setItemText(0, QCoreApplication.translate("Form", u"groggy", None))
        self.combo_mood.setItemText(1, QCoreApplication.translate("Form", u"normal", None))
        self.combo_mood.setItemText(2, QCoreApplication.translate("Form", u"energetic", None))

        self.label_meals.setText(QCoreApplication.translate("Form", u"Number of meals today:", None))
        self.label_smoking.setText(QCoreApplication.translate("Form", u"Used smoking/alcohol today", None))
        self.lineEdit_smoke_detail.setPlaceholderText(QCoreApplication.translate("Form", u"if yes, specify amount", None))
        self.label_social.setText(QCoreApplication.translate("Form", u"How was your social environment today?", None))
        self.combo_social.setItemText(0, QCoreApplication.translate("Form", u"alone at home", None))
        self.combo_social.setItemText(1, QCoreApplication.translate("Form", u"with family or friends (at home)", None))
        self.combo_social.setItemText(2, QCoreApplication.translate("Form", u"outside in social settings", None))
        self.combo_social.setItemText(3, QCoreApplication.translate("Form", u"socially isolated avoided people", None))

        self.label_caffeine.setText(QCoreApplication.translate("Form", u"How much caffeine did you consume today?", None))
        self.combo_caffeine.setItemText(0, QCoreApplication.translate("Form", u"none", None))
        self.combo_caffeine.setItemText(1, QCoreApplication.translate("Form", u"1 small cup", None))
        self.combo_caffeine.setItemText(2, QCoreApplication.translate("Form", u"2-3 cups", None))
        self.combo_caffeine.setItemText(3, QCoreApplication.translate("Form", u"4+ cups", None))
        self.combo_caffeine.setItemText(4, QCoreApplication.translate("Form", u"energy drink/cola", None))
        self.combo_caffeine.setItemText(5, QCoreApplication.translate("Form", u"I don't remember", None))

        self.groupBox_summary.setTitle(QCoreApplication.translate("Form", u"Daily Summary", None))
        self.label_summary_feel.setText(QCoreApplication.translate("Form", u"How did you feel today?", None))
        self.combo_day_summary.setItemText(0, QCoreApplication.translate("Form", u"had trouble sleeping", None))
        self.combo_day_summary.setItemText(1, QCoreApplication.translate("Form", u"felt sleepy all day", None))
        self.combo_day_summary.setItemText(2, QCoreApplication.translate("Form", u"felt normal", None))
        self.combo_day_summary.setItemText(3, QCoreApplication.translate("Form", u"felt good/energetic", None))

        self.textedit_daily_note.setPlaceholderText(QCoreApplication.translate("Form", u"Daily Note (optional)", None))
        self.pushButton_save.setText(QCoreApplication.translate("Form", u"Save", None))
    # retranslateUi

