import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QMessageBox,
    QVBoxLayout, QHBoxLayout, QLineEdit, QSpinBox, QTimeEdit, QPushButton, QLabel, QFrame
)
from patient_register_ui import Ui_Form as RegisterForm
from daily_entry_form_end_ui import Ui_Form as DailyForm


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Patient Registration")
        self.ui = RegisterForm()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.save_patient_data)
        self.show()

    def save_patient_data(self):
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
            with open("patient_data.txt", "a", encoding="utf-8") as file:
                file.write("---- NEW RECORD ----\n")
                for key, value in data.items():
                    file.write(f"{key}: {value}\n")
                file.write("\n")
            QMessageBox.information(self, "Success", "Patient data saved!")
            self.open_daily_form()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Could not save data:\n{e}")

    def open_daily_form(self):
        self.daily_window = DailyEntryForm()
        self.daily_window.show()
        self.close()


class DailyEntryForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Daily Entry Form")
        self.ui = DailyForm()
        self.ui.setupUi(self)
        self.ui.button_add_medication.clicked.connect(self.add_medication_entry)
        self.ui.pushButton_save.clicked.connect(self.save_daily_data)
        self.medication_entries = []

    def add_medication_entry(self):
        container = QFrame()
        layout = QHBoxLayout(container)

        name = QLineEdit()
        name.setPlaceholderText("Name")

        dose = QSpinBox()
        dose.setSuffix(" mg")
        dose.setMaximum(1000)

        time = QTimeEdit()
        delay = QSpinBox()
        delay.setSuffix(" hrs")
        delay.setMaximum(24)

        layout.addWidget(QLabel("Name:"))
        layout.addWidget(name)
        layout.addWidget(QLabel("Dose:"))
        layout.addWidget(dose)
        layout.addWidget(QLabel("Time:"))
        layout.addWidget(time)
        layout.addWidget(QLabel("Effect Delay:"))
        layout.addWidget(delay)

        self.ui.medication_entries_layout.addWidget(container)
        self.medication_entries.append((name, dose, time, delay))

    def save_daily_data(self):
        try:
            with open("daily_entry.txt", "a", encoding="utf-8") as file:
                file.write("=== DAILY ENTRY ===\n")
                file.write(f"Date: {self.ui.dateEdit.text()}\n")
                file.write(f"Sleep: {self.ui.timeEdit_sleep.text()} - {self.ui.timeEdit_wake.text()}\n")
                file.write(f"Sleep Quality: {self.ui.spinBox_quality.value()}\n")

                file.write("Medications:\n")
                for name, dose, time, delay in self.medication_entries:
                    file.write(
                        f"- {name.text()} | {dose.value()} mg | {time.text()} | {delay.value()} hrs delay\n"
                    )

                file.write(f"Alertness: {self.ui.spinBox_alertness.value()}\n")
                file.write(f"Screen Time: {self.ui.spinBox_screen.value()} hours\n")
                file.write(f"Activity Level: {self.ui.combo_activity.currentText()}\n")
                file.write(f"Stress: {self.ui.spinBox_stress.value()}/5\n")
                file.write(f"Mood: {self.ui.combo_mood.currentText()}\n")
                file.write(f"Meals: {self.ui.spinBox_meals.value()}\n")
                file.write(f"Smoking/Alcohol: {'Yes' if self.ui.checkBox_smoke.isChecked() else 'No'}\n")
                file.write(f"Detail: {self.ui.lineEdit_smoke_detail.text()}\n")
                file.write(f"Social: {self.ui.combo_social.currentText()}\n")
                file.write(f"Caffeine: {self.ui.combo_caffeine.currentText()}\n")
                file.write(f"Daily Summary: {self.ui.combo_day_summary.currentText()}\n")
                file.write(f"Note: {self.ui.textedit_daily_note.toPlainText()}\n")
                file.write("\n")
            QMessageBox.information(self, "Saved", "Daily entry saved successfully.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error saving data:\n{e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
