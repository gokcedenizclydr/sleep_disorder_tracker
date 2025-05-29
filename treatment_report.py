import json
from datetime import datetime
import os

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
                    s = datetime.strptime(sleep_time, fmt)
                    w = datetime.strptime(wake_time, fmt)
                    if w < s:
                        w = w.replace(day=w.day+1)
                    duration = (w - s).seconds / 3600
                    sleep_durations.append(duration)
                except:
                    pass

            if entry.get("medication_time"):
                medication_times.append(entry["medication_time"])

            if entry.get("stress_level") is not None:
                stress_levels.append(entry["stress_level"])

            notes = (entry.get("note", "") + " " + entry.get("day_summary", "")).lower()
            if any(risk_word in notes for risk_word in ["depressed", "tired", "no motivation", "hopeless", "suicid"]):
                risky_notes.append((date, notes.strip()))

        report_lines = []
        report_lines.append("TREATMENT ANALYSIS REPORT")
        report_lines.append("===========================\n")

        report_lines.append(f"Patient Name: {self.patient_info.get('Full Name', 'N/A')}")
        report_lines.append(f"Age: {self.patient_info.get('Age', 'N/A')}")
        report_lines.append(f"Gender: {self.patient_info.get('Gender', 'N/A')}")
        report_lines.append(f"Profession: {self.patient_info.get('Profession', 'N/A')}")
        report_lines.append(f"Chronic Diseases: {self.patient_info.get('Chronic Diseases', 'N/A')}")
        report_lines.append(f"Sleep Disorder Type: {self.patient_info.get('Sleep Disorder Type', 'N/A')}\n")

        report_lines.append(f"Treatment Duration: {total_days} days")
        report_lines.append(f"Average Alertness Score: {sum(alertness_scores)/len(alertness_scores):.2f}")
        report_lines.append(f"Average Sleep Duration: {sum(sleep_durations)/len(sleep_durations):.2f} hours")
        report_lines.append(f"Average Stress Level: {sum(stress_levels)/len(stress_levels):.2f}")

        if risky_notes:
            report_lines.append("\⚠️ Psychological Risk Notes Detected:")
            for d, note in risky_notes:
                report_lines.append(f"- {d}: {note[:60]}...")

        return "\n".join(report_lines)

    def generate_report_file(self, output_dir="reports"):
        os.makedirs(output_dir, exist_ok=True)
        dates = sorted(self.daily_data.keys())
        if not dates:
            return None

        start_date = dates[0].replace("-", "")
        end_date = dates[-1].replace("-", "")
        base_filename = f"treatment_report_{start_date}_to_{end_date}"

        # Save .txt report
        txt_path = os.path.join(output_dir, base_filename + ".txt")
        report_text = self.generate_report()
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write(report_text)

        # Save .csv raw data
        csv_path = os.path.join(output_dir, base_filename + ".csv")
        with open(csv_path, 'w', encoding='utf-8') as f:
            f.write("date,alertness_score,sleep_duration,stress_level,note\n")
            for date in dates:
                entry = self.daily_data[date]
                score = entry.get("alertness_score", "")
                stress = entry.get("stress_level", "")
                notes = (entry.get("note", "") + " " + entry.get("day_summary", "")).replace("\n", " ").replace(",", ";")
                duration = ""
                try:
                    s = datetime.strptime(entry.get("sleep_time", "00:00"), "%H:%M")
                    w = datetime.strptime(entry.get("wake_time", "00:00"), "%H:%M")
                    if w < s:
                        w = w.replace(day=w.day+1)
                    duration = round((w - s).seconds / 3600, 2)
                except:
                    duration = ""
                f.write(f"{date},{score},{duration},{stress},{notes}\n")

        return txt_path
