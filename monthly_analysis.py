import json
import os
from datetime import datetime
from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from ui.monthly_analysis_with_plotCLOsdi_ui import Ui_MonthlyAnalysisForm

class MonthlyAnalysisWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MonthlyAnalysisForm()
        self.ui.setupUi(self)
        self.data_path = "data/demo_data.json"
        self.daily_data = {}

        self.load_data()
        self.perform_analysis()

    def load_data(self):
        if not os.path.exists(self.data_path):
            QMessageBox.critical(self, "Error", "Data file not found.")
            return

        with open(self.data_path, "r", encoding="utf-8") as f:
            self.daily_data = json.load(f)

        if len(self.daily_data) < 30:
            QMessageBox.critical(self, "Error", "At least 30 daily entries are required for monthly analysis.")
            return

    def perform_analysis(self):
        dates = sorted(self.daily_data.keys())[-30:]  # Only last 30 days
        alertness = []
        stress = []
        sleep_durations = []
        risky_days = []

        for date in dates:
            entry = self.daily_data[date]

            alertness.append(entry.get("alertness_score", 0))
            stress.append(entry.get("stress_level", 0))

            sleep_time = entry.get("sleep_time")
            wake_time = entry.get("wake_time")
            if sleep_time and wake_time:
                try:
                    fmt = "%H:%M"
                    sleep_dt = datetime.strptime(sleep_time, fmt)
                    wake_dt = datetime.strptime(wake_time, fmt)
                    duration = (wake_dt - sleep_dt).seconds / 3600 if wake_dt > sleep_dt else (wake_dt - sleep_dt).seconds / 3600 + 24
                    sleep_durations.append(duration)
                except:
                    sleep_durations.append(0)
            else:
                sleep_durations.append(0)

            notes = (entry.get("note", "") + " " + entry.get("day_summary", "")).lower()
            if any(word in notes for word in ["panic", "anxiety", "suicide", "worthless", "tired of life"]):
                risky_days.append(date)

        # Summary Text
        avg_alert = round(sum(alertness) / len(alertness), 2)
        avg_stress = round(sum(stress) / len(stress), 2)
        avg_sleep = round(sum(sleep_durations) / len(sleep_durations), 2)

        summary = f"""
Monthly Analysis Summary (Last 30 Days):

Average Alertness Score: {avg_alert}
Average Stress Level: {avg_stress}
Average Sleep Duration: {avg_sleep} hours
Flagged Risk Days: {len(risky_days)}
"""
        if avg_stress > 7 and avg_alert < 5:
            summary += "\n⚠️ High stress combined with low alertness detected. Possible medication-related fatigue."
        if len(risky_days) >= 3:
            summary += "\n⚠️ Multiple notes indicate potential psychological risk."

        self.ui.textEdit_summary.setText(summary)

        # Draw plot
        self.draw_plot(dates, alertness, stress, sleep_durations)

    def draw_plot(self, dates, alertness, stress, sleep):
        fig, ax = plt.subplots(3, 1, figsize=(8, 6), constrained_layout=True)

        ax[0].plot(dates, alertness, marker='o')
        ax[0].set_title("Alertness Score")
        ax[0].set_ylabel("Score (0–10)")

        ax[1].plot(dates, stress, marker='x', color='orange')
        ax[1].set_title("Stress Level")
        ax[1].set_ylabel("Level (0–10)")

        ax[2].plot(dates, sleep, marker='s', color='green')
        ax[2].set_title("Sleep Duration")
        ax[2].set_ylabel("Hours")
        ax[2].set_xticks(range(0, len(dates), max(1, len(dates)//5)))
        ax[2].set_xticklabels([dates[i] for i in range(0, len(dates), max(1, len(dates)//5))], rotation=45)

        canvas = FigureCanvas(fig)
        for i in reversed(range(self.ui.plot_widget.layout().count())):
            self.ui.plot_widget.layout().itemAt(i).widget().deleteLater()
        if not self.ui.plot_widget.layout():
            from PySide6.QtWidgets import QVBoxLayout
            self.ui.plot_widget.setLayout(QVBoxLayout())
        self.ui.plot_widget.layout().addWidget(canvas)
