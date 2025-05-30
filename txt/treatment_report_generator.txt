import json
import os
from statistics import mean
from datetime import datetime
from collections import Counter

class TreatmentReportGenerator:
    def __init__(self,
                 demo_data: dict,
                 patient_data: dict,
                 report_folder="reports"):

        self.daily_data = demo_data
        self.patient_info = patient_data
        self.report_folder = report_folder
        self.dates = sorted(self.daily_data.keys())

    def compute_sleep_duration(self, sleep, wake):
        fmt = "%H:%M"
        sleep_dt = datetime.strptime(sleep, fmt)
        wake_dt = datetime.strptime(wake, fmt)
        delta = (wake_dt - sleep_dt).seconds / 3600
        if delta <= 0:
            delta += 24
        return delta

    def generate_report(self):
        alertness_scores = []
        sleep_durations = []
        stress_levels = []
        screen_times = []
        moods = []
        activities = []
        caffeine_types = []
        notes = []
        summary_tags = []
        med_times = []
        risk_days = []

        for date in self.dates:
            entry = self.daily_data[date]
            alertness_scores.append(entry["alertness_score"])
            stress_levels.append(entry["stress_level"])
            screen_times.append(entry["screen_time"])
            moods.append(entry["wake_mood"])
            activities.append(entry["physical_activity"])
            caffeine_types.append(entry["caffeine"])
            summary_tags.append(entry["day_summary"])
            med_times.append(entry["medication_time"])
            notes.append(entry["note"])

            sleep_durations.append(self.compute_sleep_duration(entry["sleep_time"], entry["wake_time"]))

            if entry["wake_mood"] == "groggy" and entry["caffeine"] in ["4+ cups", "energy drink/cola"]:
                risk_days.append(date)
            if entry["used_smoke_alcohol"]:
                risk_days.append(date)
            if any(k in entry["note"].lower() for k in ["fog", "drained", "tired", "exhausted", "struggled"]):
                risk_days.append(date)

        best_day = max(self.dates, key=lambda d: self.daily_data[d]["alertness_score"])
        worst_day = min(self.dates, key=lambda d: self.daily_data[d]["alertness_score"])

        most_common_caffeine = Counter(caffeine_types).most_common(1)[0][0]
        most_common_mood = Counter(moods).most_common(1)[0][0]
        most_common_activity = Counter(activities).most_common(1)[0][0]

        med_hours = [int(t.split(":")[0]) for t in med_times]
        med_hour_avg = mean(med_hours)
        hour_variance = max(med_hours) - min(med_hours)

        report_lines = [
            "----- Sleep Disorder Treatment Final Analysis -----\n",
            f"• Treatment Period: {self.dates[0]} to {self.dates[-1]}",
            f"• Total Days Tracked: {len(self.dates)}",
            "\n📊 Averages:",
            f"- Alertness Score: {round(mean(alertness_scores), 2)}",
            f"- Sleep Duration: {round(mean(sleep_durations), 2)} hours",
            f"- Stress Level: {round(mean(stress_levels), 2)}",
            f"- Screen Time: {round(mean(screen_times), 2)} hours",
            f"- Caffeine Intake: {most_common_caffeine}",
            f"- Physical Activity: mostly {most_common_activity}",
            f"- Mood Distribution: most often '{most_common_mood}'",
            "\n🧠 Best Day:",
            f"- {best_day} → Alertness {self.daily_data[best_day]['alertness_score']} | Note: {self.daily_data[best_day]['note']}",
            "\n🌧️ Worst Day:",
            f"- {worst_day} → Alertness {self.daily_data[worst_day]['alertness_score']} | Note: {self.daily_data[worst_day]['note']}",
            "\n⏰ Medication Pattern:",
            f"- Most common dose hour: ~{int(med_hour_avg)}:00",
            f"- Time variability: ±{hour_variance}h"
        ]

        if hour_variance >= 6:
            report_lines.append("⚠️ Possible inconsistency in medication schedule detected.")

        report_lines += [
            "\n🚩 Risk Indicators:",
            f"- {len(set(risk_days))} days flagged with behavioral or mood risks.",
            "\n📓 NLP Note Flags:",
            f"- Found keywords: {', '.join(set([w for n in notes for w in n.lower().split() if w in ['tired', 'drained', 'fog', 'exhausted', 'struggled']]))}",
            "\n💡 Recommendation:",
            "Consider stabilizing medication timing, reducing caffeine on groggy days, and reviewing emotional well-being if flagged terms persist."
        ]

        os.makedirs(self.report_folder, exist_ok=True)
        with open(os.path.join(self.report_folder, "final_report.txt"), "w", encoding="utf-8") as f:
            f.write("\n".join(report_lines))

        report_json = {
            "treatment_start": self.dates[0],
            "treatment_end": self.dates[-1],
            "total_days": len(self.dates),
            "averages": {
                "alertness": round(mean(alertness_scores), 2),
                "sleep_duration": round(mean(sleep_durations), 2),
                "stress": round(mean(stress_levels), 2),
                "screen_time": round(mean(screen_times), 2),
            },
            "common": {
                "caffeine": most_common_caffeine,
                "activity": most_common_activity,
                "mood": most_common_mood
            },
            "best_day": best_day,
            "worst_day": worst_day,
            "medication_hour_average": int(med_hour_avg),
            "medication_hour_variance": hour_variance,
            "risk_days": list(set(risk_days))
        }

        with open(os.path.join(self.report_folder, "final_summary.json"), "w", encoding="utf-8") as f:
            json.dump(report_json, f, indent=4, ensure_ascii=False)

        return report_lines
