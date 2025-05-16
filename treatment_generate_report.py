from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QTextEdit, QMessageBox
)
from PyQt6.QtCore import Qt
import json
import re
from datetime import datetime


class TreatmentReportWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Final Treatment Report")
        self.setMinimumSize(700, 600)

        layout = QVBoxLayout()

        self.report_view = QTextEdit()
        self.report_view.setReadOnly(True)
        self.report_view.setPlaceholderText("Click the button below to generate the final report...")

        self.generate_button = QPushButton("Generate Final Treatment Report")
        self.generate_button.clicked.connect(self.generate_report)

        layout.addWidget(self.generate_button)
        layout.addWidget(self.report_view)
        self.setLayout(layout)

    def load_patient_data(self):
        try:
            with open("data/patient_data.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load patient_data.json:\n{str(e)}")
            return {}

    def load_daily_entries(self):
        try:
            with open("data/demo_data.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load demo_data.json:\n{str(e)}")
            return {}

    def detect_risk_phrases(self, notes):
        flagged = []
        keywords = [
            r"suicide", r"want to die", r"can't go on", r"depressed", r"hopeless",
            r"intihar", r"ölmek istiyorum", r"dayanamıyorum", r"ümitsiz", r"yok olmak"
        ]
        for date, note in notes.items():
            for pattern in keywords:
                if re.search(pattern, note, re.IGNORECASE):
                    flagged.append((date, note))
                    break
        return flagged

    def generate_report(self):
        patient = self.load_patient_data()
        entries = self.load_daily_entries()

        if not patient or not entries:
            return

        sorted_dates = sorted(entries.keys())
        start_date = sorted_dates[0]
        end_date = sorted_dates[-1]
        days = len(sorted_dates)

        sleep_scores = []
        alertness_scores = []
        stress_scores = []
        medication_total = 0
        medication_days = 0
        notes = {}

        for date, entry in entries.items():
            sleep_scores.append(entry["sleep_quality"])
            alertness_scores.append(entry["alertness_score"])
            stress_scores.append(entry["stress_level"])

            note = entry.get("daily_note", "")
            if note:
                notes[date] = note

            try:
                dose = int(entry.get("medication_dose", 0))
                if dose > 0:
                    medication_total += dose
                    medication_days += 1
            except:
                continue

        risk_flags = self.detect_risk_phrases(notes)

        avg_sleep = sum(sleep_scores) / len(sleep_scores)
        avg_alert = sum(alertness_scores) / len(alertness_scores)
        avg_stress = sum(stress_scores) / len(stress_scores)
        avg_dose = medication_total / medication_days if medication_days else 0

        report = []

        report.append("========== Final Treatment Report ==========\n")
        report.append(f"📅 Duration: {start_date} to {end_date} ({days} days)")
        report.append(f"🧠 Diagnosis: {patient.get('Sleep Disorder Type', 'N/A')}")
        report.append(f"📌 Other Conditions: {patient.get('Chronic Diseases', 'None')}")
        report.append(f"👤 Patient Info: Age: {patient.get('Age', '?')} | Gender: {patient.get('Gender', '?')} | Profession: {patient.get('Profession', '?')}\n")

        report.append("----- Treatment Summary -----")
        report.append(f"• Average Sleep Quality: {avg_sleep:.2f}")
        report.append(f"• Average Alertness: {avg_alert:.2f}")
        report.append(f"• Average Stress Level: {avg_stress:.2f}")
        report.append(f"• Total Medication Used: {medication_total} mg")
        report.append(f"• Average Daily Dose: {avg_dose:.1f} mg\n")

        report.append("----- Psychological Risk Flags -----")
        if risk_flags:
            for date, note in risk_flags:
                report.append(f"⚠️ {date}: {note}")
        else:
            report.append("✅ No critical risk expressions found.\n")

        report.append("----- Initial Notes & Recommendations -----")
        report.append(f"Initial Note: {patient.get('Initial Note', 'N/A')}")
        report.append("⚠️ Follow-up with a healthcare provider is recommended if symptoms persist.")
        report.append("📊 For researchers: consider further trend analysis if dataset grows.\n")

        report.append("=============================================\n")

        full_text = "\n".join(report)
        self.report_view.setPlainText(full_text)

        try:
            with open("treatment_report.txt", "w", encoding="utf-8") as file:
                file.write(full_text)
        except Exception as e:
            QMessageBox.warning(self, "Save Error", f"Failed to save report:\n{str(e)}")
        else:
            QMessageBox.information(self, "Success", "Report successfully saved as treatment_report.txt")
