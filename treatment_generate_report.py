import os
from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox
from treatment_report import TreatmentReportGenerator

class GenerateReportWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("End Treatment & Generate Report")

        self.generate_report_button = QPushButton("Generate Final Report")
        self.generate_report_button.clicked.connect(self.handle_generate_report)

        layout = QVBoxLayout()
        layout.addWidget(self.generate_report_button)
        self.setLayout(layout)

    def handle_generate_report(self):
        try:
            # Klasör yoksa oluştur
            os.makedirs("reports", exist_ok=True)

            generator = TreatmentReportGenerator(
                demo_data_path="data/demo_data.json",
                patient_data_path="data/patient_data.json"
            )
            generator.save_report_as_txt("reports/treatment_summary.txt")
            generator.save_report_as_csv("reports/treatment_data.csv")

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Report Generated")
            msg.setText("Treatment summary and CSV report have been saved in the 'reports' folder.")
            msg.exec()

        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Error")
            msg.setText(f"An error occurred while generating the report:\n{e}")
            msg.exec()

