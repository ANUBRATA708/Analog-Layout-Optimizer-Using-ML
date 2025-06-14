<h1 align="center">⚙️ Analog Layout Optimizer Using ML</h1>
<p align="center">
  A machine learning-powered tool to automate and accelerate full-custom analog IC layout estimation and ranking.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Streamlit-App-blue?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/ML%20Model-LinearRegression-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Netlist-.sp-yellow?style=for-the-badge"/>
</p>

---

## 🚀 Features

- ✅ Upload `.sp` netlist files  
- ✅ Automatic feature extraction:
  - Node count
  - Edge count
  - Average degree  
- ✅ Predict layout area using **Linear Regression**
- ✅ Rank circuits by predicted area and topological complexity  
- ✅ Generate **visual complexity charts**  
- ✅ Download ranked results as CSV  
- ✅ Launch via Streamlit Web UI (no command line!)

---

## 📁 Folder Structure


AnalogLayoutML/
├── app.py                      # Streamlit App Entry Point
├── Launch_analogtool.bat       # Launches the tool directly in browser
├── utils/
│   └── rank_circuits.py        # Circuit ranking logic
├── feature_extractor/
│   └── extract_features.py     # Netlist feature extraction
├── circuit_data/
│   └── netlists/               # Uploaded .sp netlist files
├── reports/
│   └── ranked_results.csv      # Auto-generated results
├── ml_model/
│   └── model.pkl               # Trained ML model (Linear Regression)
├── train_model.py              # One-time training script
├── requirements.txt            # Python dependencies
└── README.md                   # Project overview

## 💻 Installation & Launch Instructions
📥 Download or clone the repository

✅ Ensure Python and dependencies from requirements.txt are installed

📁 Place your .sp netlist files inside circuit_data/netlists/

🖱️ Double-click Launch_analogtool.bat

🌐 The tool opens automatically in your default web browser


## App Preview
![image](https://github.com/user-attachments/assets/3dc626fb-6eeb-458d-b846-00caa7a518f4)
![image](https://github.com/user-attachments/assets/8a7e3ee5-1855-475c-82ef-efe64ef0564f)
![image](https://github.com/user-attachments/assets/e41772d9-82f2-4104-a3a7-3de5a45f4dc9)

## 🛠 Built With
Python

Streamlit

scikit-learn

pandas / numpy

NetworkX

## 👨‍💻 Author
Anubrata Majumdar







