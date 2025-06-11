# Analog-Layout-Optimizer-Using-ML
A ML-powered tool to automate and accelerate full-custom analog IC layout estimation and ranking.

## 🚀 Features

✅ Upload `.sp` netlist files  
✅ Automatic feature extraction (nodes, edges, avg degree)  
✅ Predict layout area using Linear Regression  
✅ Rank by area and complexity  
✅ Visual complexity chart  
✅ Downloadable ranking results
✅ Streamlit web-based UI (no command line needed)  

## 📂 Folder Structure

AnalogLayoutML/

├── app.py   # Streamlit App Entry Point

├── utils/

│ └── rank_circuits.py    # Ranking Logic

├── feature_extractor/

│ └── extract_features.py     # Netlist Feature Extraction

├── circuit_data/

│ └── netlists/     # Uploaded .sp Netlists

├── reports/

│ └── ranked_results.csv     # Auto-Generated Rankings

├── ml_model/

│ └── model.pkl       # Trained Model

├── train_model.py     # One-Time Training Script

├── requirements.txt      # Project Dependencies

└── README.md       # Project Overview

└── Launch_analogtool.bat     #To run the tool directly in the default browser without command line

## Installation and Launch
Download all the provided files in the proper manner.
Double Click on "Launch_analogtool.bat".
The Tool will open in your default browser.

## App Preview
![image](https://github.com/user-attachments/assets/3dc626fb-6eeb-458d-b846-00caa7a518f4)
![image](https://github.com/user-attachments/assets/8a7e3ee5-1855-475c-82ef-efe64ef0564f)
![image](https://github.com/user-attachments/assets/e41772d9-82f2-4104-a3a7-3de5a45f4dc9)







