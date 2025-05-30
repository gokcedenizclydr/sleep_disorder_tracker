from PySide6.QtWidgets import QWidget, QMessageBox
from ui.treatment_generate_report import Ui_TreatmentReport
import json
import os
from treatment_report_generator import TreatmentReportGenerator

class GenerateReportWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TreatmentReport()
        self.ui.setupUi(self)
        self.setWindowTitle("Treatment Report Generator")

        self.ui.btn_generate.clicked.connect(self.handle_generate_report)

    def handle_generate_report(self):
        demo_path = "data/demo_data.json"
        patient_path = "data/patient_data.json"

        if not os.path.exists(demo_path) or not os.path.exists(patient_path):
            QMessageBox.warning(self, "Missing Data", "Required JSON files not found.")
            return

        try:
            with open(demo_path, "r", encoding="utf-8") as f:
                demo_data = json.load(f)

            with open(patient_path, "r", encoding="utf-8") as f:
                patient_data = json.load(f)

            generator = TreatmentReportGenerator(demo_data, patient_data)
            report_lines = generator.generate_report()

            QMessageBox.information(self, "Report Complete", "Report generated and saved to 'reports/' folder.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred:\n{str(e)}")


