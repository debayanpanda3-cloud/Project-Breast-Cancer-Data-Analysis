# Breast Cancer Data Analysis & Pair Plot Visualization

A Python-based Exploratory Data Analysis (EDA) tool for visualizing cell nuclei features from breast cancer diagnostic datasets using **Seaborn** and **Matplotlib**.

This repository provides command-line utilities to generate pairwise scatter plots comparing mean cellular features (e.g., radius, texture, perimeter, area) color-coded by diagnosis label (benign vs. malignant).

---

##  Project Overview

Understanding the feature relationships in diagnostic datasets is a critical first step in medical data science and machine learning. This project allows users to:
- Inspect and list available mean numerical features from diagnostic CSV datasets.
- Generate multi-variable pair plots to visually detect patterns and feature separation between diagnostic classes.
- Export high-resolution scatterplot matrices (`.png`) for reporting or documentation.

---

##  Installation & Setup

### 1. Prerequisites
Ensure you have Python 3.8+ installed on your system.

### 2. Clone the Repository
```bash
git clone [https://github.com/debayanpanda3-cloud/Project-Breast-Cancer-Data-Analysis.git](https://github.com/debayanpanda3-cloud/Project-Breast-Cancer-Data-Analysis.git)
cd Project-Breast-Cancer-Data-Analysis
Install all required libraries listed in requirements.txt:

Bash
python3 -m pip install -r requirements.txt
** Usage Guide
List Available Features
To inspect the CSV dataset and print all available mean features to your terminal:

Bash
python3 plot_breast_cancer_pairs.py --list-features
Generate Default Pair Plot
If no features are specified, the script automatically plots the first four mean features:

Bash
python3 plot_breast_cancer_pairs.py
Custom Feature Selection
Pass exact CSV column names to compare specific measurements:

Bash
python3 plot_breast_cancer_pairs.py \
  --features "mean radius" "mean texture" "mean perimeter" "mean area"
Save Output to File
Save the generated plot directly as an image without opening a interactive GUI window:

Bash
python3 plot_breast_cancer_pairs.py \
  --features "mean radius" "mean texture" \
  --output breast-cancer-pairs.png
** Sample Output
The generated pair plots display:

Diagonal plots: Feature distribution per diagnosis class.

Scatter matrix: Inter-feature relationships colored by diagnosis (benign vs. malignant).

Legend: Visual indicator highlighting active features in green and inactive features in red.

**Repository Structure
Plaintext
├── breast_cancer.csv           # Diagnostic dataset
├── plot_breast_cancer_pairs.py # Main visualization CLI script
├── breast-cancer-pairs.png     # Exported sample visualization plot
├── requirements.txt            # Python dependencies (pandas, seaborn, matplotlib, scikit-learn)
└── README.md                   # Project documentation
## Author
Debayan Panda

GitHub: @debayanpanda3-cloud

Email: debayanpanda3@gmail.com



