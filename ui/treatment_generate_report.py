from PySide6 import QtCore, QtGui, QtWidgets

class Ui_TreatmentReport(object):
    def setupUi(self, TreatmentReport):
        TreatmentReport.setObjectName("TreatmentReport")
        TreatmentReport.resize(480, 320)
        self.verticalLayout = QtWidgets.QVBoxLayout(TreatmentReport)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label_title = QtWidgets.QLabel(TreatmentReport)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setText("Treatment Report Generator")
        self.verticalLayout.addWidget(self.label_title)

        self.btn_generate = QtWidgets.QPushButton(TreatmentReport)
        self.btn_generate.setText("Generate Report")
        self.verticalLayout.addWidget(self.btn_generate)

        self.label_note = QtWidgets.QLabel(TreatmentReport)
        self.label_note.setText("This will analyze all tracked days and generate final treatment summary.")
        self.label_note.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label_note)

        QtCore.QMetaObject.connectSlotsByName(TreatmentReport)

