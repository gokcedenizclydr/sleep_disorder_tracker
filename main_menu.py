import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton

class DailyEntryForm(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/daily_entry_form_end.ui", self)
        self.setWindowTitle("Daily Entry Form")

class MainMenu(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/main_menu.ui", self)  # 🟢 DİKKAT: Dosya yolu güncellendi

        self.findChild(QPushButton, "btn_daily_entry").clicked.connect(self.open_daily_entry)
        self.findChild(QPushButton, "btn_monthly_analysis").clicked.connect(self.open_monthly_analysis)
        self.findChild(QPushButton, "btn_treatment_end").clicked.connect(self.open_treatment_report)
        self.findChild(QPushButton, "btn_logout").clicked.connect(self.logout)

    def open_daily_entry(self):
        print(">> Opening Daily Entry Form")
        self.daily_entry_window = DailyEntryForm()
        self.daily_entry_window.show()

    def open_monthly_analysis(self):
        print(">> Monthly Analysis button clicked")

    def open_treatment_report(self):
        print(">> Treatment Report button clicked")

    def logout(self):
        print(">> Logout button clicked")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainMenu()
    window.setWindowTitle("Sleep Tracker - Main Menu")
    window.show()
    sys.exit(app.exec())
