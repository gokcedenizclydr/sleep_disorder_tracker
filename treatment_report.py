import json
from datetime import datetime
import os
import csv

class TreatmentReportGenerator:
    def __init__(self, demo_data_path="data/demo_data.json", patient_data_path="data/patient_data.json"):
        self.demo_data_path = demo_data_path
        self.patient_data_path = patient_data_path

        self.daily_data = self.load_json(demo_data_path)
        self.patient_info = self.load_json(patient_data_path)

    def load_json(self, path):
        if not os.path.exists(path):
            return {}
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def generate_report(self):
        dates = sorted(self.daily_data.keys())
        total_days = len(dates)

        alertness_scores = []
        sleep_durations = []
        medication_times = []
        stress_levels = []
        risky_notes = []

        for date in dates:
            entry = self.daily_data[date]

            if entry.get("alertness_score") is not None:
                alertness_scores.append(entry["alertness_score"])

            sleep_time = entry.get("sleep_time")
            wake_time = entry.get("wake_time")
            if sleep_time and wake_time:
                try:
                    fmt = "%H:%M"
                    sleep_dt = datetime.strptime(sleep_time, fmt)
                    wake_dt = datetime.strptime(wake_time, fmt)
                    duration = (wake_dt - sleep_dt).seconds / 3600 if wake_dt > sleep_dt else (wake_dt - sleep_dt).seconds / 3600 + 24
                    sleep_durations.append(duration)
                except Exception as e:
                    continue

            if entry.get("stress_level") is not None:
                stress_levels.append(entry["stress_level"])

            note_text = entry.get("note", "") + " " + entry.get("day_summary", "")
            if any(risk_word in note_text.lower() for risk_word in ["intihar", "kendine zarar", "ölmek", "yok olmak"]):
                risky_notes.append((date, note_text.strip()))

        avg_alertness = round(sum(alertness_scores) / len(alertness_scores), 2) if alertness_scores else "N/A"
        avg_sleep_duration = round(sum(sleep_durations) / len(sleep_durations), 2) if sleep_durations else "N/A"
        avg_stress = round(sum(stress_levels) / len(stress_levels), 2) if stress_levels else "N/A"

        patient_name = self.patient_info.get("Full Name", "Unknown")
        age = self.patient_info.get("Age", "Unknown")
        gender = self.patient_info.get("Gender", "Unknown")
        profession = self.patient_info.get("Profession", "Unknown")
        chronic_diseases = self.patient_info.get("Chronic Diseases", "None")

        report = f"""
----- Treatment Summary Report -----

Patient Name: {patient_name}
Age: {age} | Gender: {gender}
Profession: {profession}
Chronic Conditions: {chronic_diseases}

Total Days Tracked: {total_days}
Average Alertness Score: {avg_alertness}
Average Sleep Duration: {avg_sleep_duration} hours
Average Stress Level: {avg_stress}

-- Psychological Risk Notes --
"""

        if risky_notes:
            for date, note in risky_notes:
                report += f"\n{date}: {note}"
        else:
            report += "\nNo high-risk notes detected."

        report += "\n\n----------------------------------"
        return report

    def save_report_as_txt(self, filepath="treatment_summary.txt"):
        report = self.generate_report()
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"Report saved as TXT at: {filepath}")

    def save_report_as_csv(self, filepath="treatment_data.csv"):
        headers = [
            "Date", "Alertness Score", "Sleep Time", "Wake Time",
            "Sleep Quality", "Stress Level", "Caffeine", "Screen Time",
            "Physical Activity", "Social Environment", "Note", "Day Summary"
        ]

        with open(filepath, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(headers)

            for date in sorted(self.daily_data.keys()):
                entry = self.daily_data[date]
                row = [
                    date,
                    entry.get("alertness_score"),
                    entry.get("sleep_time"),
                    entry.get("wake_time"),
                    entry.get("sleep_quality"),
                    entry.get("stress_level"),
                    entry.get("caffeine"),
                    entry.get("screen_time"),
                    entry.get("physical_activity"),
                    entry.get("social_environment"),
                    entry.get("note"),
                    entry.get("day_summary"),
                ]
                writer.writerow(row)

        print(f"Report saved as CSV at: {filepath}")
