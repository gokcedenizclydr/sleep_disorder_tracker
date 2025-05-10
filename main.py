import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from patient_register_ui import Ui_Form

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.save_data)
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
            with open("patient_data.txt", "a", encoding="utf-8") as file:
                file.write("---- NEW RECORD ----\n")
                for key, value in data.items():
                    file.write(f"{key}: {value}\n")
                file.write("\n")
            QMessageBox.information(self, "Success", "Data saved successfully!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Could not save data:\n{e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())



