import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton


# ---------- DAILY ENTRY FORM ----------
class DailyEntryForm(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/daily_entry_form_end.ui", self)
        self.setWindowTitle("Daily Entry Form")


# ---------- MONTHLY ANALYSIS FORM ----------
class MonthlyAnalysisForm(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/monthly_analysis.ui", self)
        self.setWindowTitle("Monthly Analysis")

        # Bileşenleri bul
        self.comboBox_month = self.findChild(QtWidgets.QComboBox, "comboBox_month")
        self.textEdit_summary = self.findChild(QtWidgets.QTextEdit, "textEdit_summary")
        self.btn_back = self.findChild(QtWidgets.QPushButton, "btn_back")

        # Ayları ekle
        self.comboBox_month.addItems([
            "January", "February", "March", "April",
            "May", "June", "July", "August",
            "September", "October", "November", "December"
        ])

        # Varsayılan seçim
        self.comboBox_month.setCurrentIndex(0)
        self.update_summary("January")

        # Olaylar
        self.comboBox_month.currentTextChanged.connect(self.update_summary)
        self.btn_back.clicked.connect(self.close)

    def update_summary(self, month):
        self.textEdit_summary.setPlainText(
            f"📊 Analysis summary for {month}:\n\n"
            "- Avg sleep quality: 7.2\n"
            "- Most effective medication: Modiwake\n"
            "- High stress days: 8\n\n"
            "💡 Suggestion: Reduce screen time before bed."
        )


# ---------- MAIN MENU ----------
class MainMenu(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/main_menu.ui", self)
        self.setWindowTitle("Sleep Tracker - Main Menu")

        # Butonları bul ve bağla
        self.btn_daily_entry = self.findChild(QPushButton, "btn_daily_entry")
        self.btn_monthly_analysis = self.findChild(QPushButton, "btn_monthly_analysis")
        self.btn_treatment_end = self.findChild(QPushButton, "btn_treatment_end")
        self.btn_logout = self.findChild(QPushButton, "btn_logout")

        self.btn_daily_entry.clicked.connect(self.open_daily_entry)
        self.btn_monthly_analysis.clicked.connect(self.open_monthly_analysis)
        self.btn_treatment_end.clicked.connect(self.open_treatment_report)
        self.btn_logout.clicked.connect(self.logout)

    def open_daily_entry(self):
        print(">> Opening Daily Entry Form")
        self.daily_entry_window = DailyEntryForm()
        self.daily_entry_window.show()

    def open_monthly_analysis(self):
        print(">> Opening Monthly Analysis")
        self.monthly_analysis_window = MonthlyAnalysisForm()
        self.monthly_analysis_window.show()

    def open_treatment_report(self):
        print(">> Treatment Report button clicked (not implemented)")

    def logout(self):
        print(">> Logout button clicked (not implemented)")


# ---------- UYGULAMA BAŞLAT ----------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainMenu()
    window.show()
    sys.exit(app.exec())

