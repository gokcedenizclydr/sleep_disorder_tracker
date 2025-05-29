import sys
import os
import json
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton
from patient_register_ui import Ui_Form
from daily_entry_form_end_ui import Ui_Form as Ui_DailyForm
from treatment_generate_report import TreatmentReportForm
from monthly_analysis import MonthlyAnalysisForm


class DailyEntryFormEnd(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DailyForm()
        self.ui.setupUi(self)
        self.setWindowTitle("Daily Entry Form")


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Patient Registration")

        self.ui.pushButton.clicked.connect(self.save_data)

        self.daily_button = QPushButton("Fill Daily Entry", self)
        self.daily_button.move(20, 360)
        self.daily_button.clicked.connect(self.open_daily_entry)

        self.monthly_button = QPushButton("Monthly Analysis", self)
        self.monthly_button.move(20, 400)
        self.monthly_button.clicked.connect(self.open_monthly_analysis)
        self.monthly_button.setEnabled(self.check_30_days())

        self.report_button = QPushButton("End Treatment & Generate Report", self)
        self.report_button.move(20, 440)
        self.report_button.clicked.connect(self.open_report_window)

        self.show()

    def save_data(self):
        data = {
            "Full Name": self.ui.lineEdit_name.text(),
            "Age": self.ui.lineEdit_age.text(),
            "Height": self.ui.lineEdit_height.text(),
            "Weight": self.ui.lineEdit_weight.text(),
            "Gender": self.ui.comboBox_gender.currentText(),
            "Sleep Disorder Type": self.ui.comboBox_disorderType.currentText(),
            "Other Disorder": self.ui.lineEdit_otherDisorder.text(),
            "Profession": self.ui.lineEdit_profession.text(),
            "Medications": self.ui.plainTextEdit_medications.toPlainText(),
            "Chronic Diseases": self.ui.plainTextEdit_chronicDisease.toPlainText(),
            "Initial Note": self.ui.plainTextEdit_initialNote.toPlainText()
        }

        try:
            os.makedirs("data", exist_ok=True)
            with open("data/patient_data.json", "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
            QMessageBox.information(self, "Success", "Patient data saved!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Could not save data:\n{e}")

    def check_30_days(self):
        try:
            with open("data/demo_data.json", "r", encoding="utf-8") as f:
                data = json.load(f)
            return len(data) >= 30
        except:
            return False

    def open_daily_entry(self):
        self.daily_window = DailyEntryFormEnd()
        self.daily_window.show()

    def open_monthly_analysis(self):
        self.analysis_window = MonthlyAnalysisForm()
        self.analysis_window.show()

    def open_report_window(self):
        self.report_window = TreatmentReportForm()
        self.report_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

