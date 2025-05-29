import json
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt6 import uic
from PyQt6.QtWidgets import QWidget
from datetime import datetime
from collections import defaultdict

class MonthlyAnalysisForm(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/monthly_analysis_with_plot.ui", self)

        self.combo_month.currentIndexChanged.connect(self.update_analysis)
        self.btn_back.clicked.connect(self.close)

        self.data_path = "data/demo_data.json"
        self.data = self.load_data()

        self.month_map = self.get_months_from_data()
        self.combo_month.addItems(self.month_map.keys())

        self.update_analysis()

    def load_data(self):
        if not os.path.exists(self.data_path):
            return {}
        with open(self.data_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def get_months_from_data(self):
        month_map = defaultdict(list)
        for date_str in self.data:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
            month_label = date_obj.strftime("%B %Y")
            month_map[month_label].append(date_str)
        return dict(month_map)

    def update_analysis(self):
        month = self.combo_month.currentText()
        if not month:
            return
        dates = self.month_map.get(month, [])
        alertness_scores = []
        days = []
        summary_lines = []

        caffeine_effect = 0
        stress_sum = 0
        screen_sum = 0
        risky_notes = []

        for date in sorted(dates):
            entry = self.data.get(date, {})
            score = entry.get("alertness_score")
            if score is not None:
                alertness_scores.append(score)
                days.append(date)

            if entry.get("caffeine", "").lower().startswith("4"):
                caffeine_effect += 1
            if entry.get("stress_level") is not None:
                stress_sum += entry.get("stress_level")
            if entry.get("screen_time") is not None:
                screen_sum += entry.get("screen_time")

            notes = (entry.get("note", "") + " " + entry.get("day_summary", "")).lower()
            if any(risk_word in notes for risk_word in ["depressed", "tired", "no motivation", "hopeless", "suicid"]):
                risky_notes.append((date, notes.strip()))

        # Grafik çizimi
        self.plot_graph(days, alertness_scores)

        # Metinsel analiz
        summary_lines.append(f"Total Days in {month}: {len(dates)}")
        summary_lines.append(f"Average Alertness: {sum(alertness_scores)/len(alertness_scores):.2f}")
        summary_lines.append(f"High caffeine intake days (4+ cups): {caffeine_effect}")
        summary_lines.append(f"Avg. Stress Level: {stress_sum / len(dates):.1f}")
        summary_lines.append(f"Avg. Screen Time (hrs): {screen_sum / len(dates):.1f}")

        if risky_notes:
            summary_lines.append("\n⚠️ Psychological Risk Notes Detected:")
            for d, note in risky_notes:
                summary_lines.append(f"- {d}: {note[:60]}...")

        self.textEdit_summary.setPlainText("\n".join(summary_lines))

    def plot_graph(self, x_data, y_data):
        layout = self.plot_widget.layout()
        if layout is not None:
            for i in reversed(range(layout.count())):
                layout.itemAt(i).widget().setParent(None)

        fig, ax = plt.subplots()
        ax.plot(x_data, y_data, marker='o')
        ax.set_title("Alertness Over Time")
        ax.set_xlabel("Date")
        ax.set_ylabel("Alertness Score")
        ax.tick_params(axis='x', rotation=45)
        fig.tight_layout()

        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)

