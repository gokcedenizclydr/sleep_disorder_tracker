# 💤 Sleep Disorder Treatment Tracker

A personalized tracking and analysis system designed for patients with sleep disorders such as **idiopathic hypersomnia**, **narcolepsy**, and **sleep apnea**.  
Tracks daily data, provides monthly insights, and generates a comprehensive final treatment report.

---

## 📦 Features

✅ Patient registration system  
✅ Daily tracking of sleep, medication, mood, stress, caffeine, smoking, physical activity, and more  
✅ JSON-based data storage  
✅ Monthly analysis (after 30 days)  
✅ Final treatment report with behavioral, psychological, and dosage analysis  
✅ GUI-based, user-friendly interface (built with PySide6/Qt)  
✅ Anonymized & research-ready data exports (`.txt` and `.json`)

---

## 🧪 Target Users

- Patients undergoing treatment for sleep-related conditions  
- Doctors & researchers seeking treatment pattern analysis  
- Clinical engineers prototyping data-driven health tools

---

## 🚀 How to Run

### 🖥️ 1. Install requirements

```bash
pip install PySide6
```

> Optional (for development):
```bash
pip install pyside6-tools
```

### 📂 2. Folder Structure

```
sleep_disorder_tracker/
├── main.py
├── patient_register_ui.py
├── main_menu.py
├── daily_entry_form_end_ui.py
├── monthly_analysis.py
├── generate_report_window.py
├── treatment_report_generator.py
├── ui/
├── ├── patient_register.ui
│   ├── main_menu.ui
├── ├── daily_entry_form_end.ui
├── ├── monthly_analysis.ui
│   ├── treatment_generate_report.ui
│   └── treatment_generate_report.py
├── data/
│   ├── demo_data.json
│   └── patient_data.json
├── reports/
│   ├── final_report.txt
│   └── final_summary.json
```

---

### ▶️ 3. Launch the app

```bash
python main.py
```

---

## 📊 Example Output

📄 `reports/final_report.txt` – A readable treatment analysis  
📈 `reports/final_summary.json` – Data structured for research or doctor review

---

## 📌 Notes

- Minimum 30 days of daily data required to unlock monthly and final analysis
- Medication timing patterns and NLP-based psychological risk flags are included
- All outputs are anonymized

---

## 🤖 Developed With

- Python 3.11  
- PySide6 (Qt for Python)  
- JSON for data persistence  
- Qt Designer for UI layout

---

## 👩‍💻 Developer

**Gökce Deniz Çulaydar**  
Biomedical Engineering – Ankara University  

---

## 📜 License

This project is for research purposes.  

