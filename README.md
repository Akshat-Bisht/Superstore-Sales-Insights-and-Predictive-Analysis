# Superstore Sales Insights & Predictive Analysis

**Role Fit**: *Data Science Engineer*  
**Author**: Akshat Bisht  
**Date**: August 13, 2025

This repository contains an end-to-end analytics project on the classic **Superstore** retail dataset (Kaggle-style). It demonstrates the full data science workflow:
- Data ingestion & cleaning
- Exploratory Data Analysis (EDA)
- Business insights & visualization
- Simple forecasting (baseline linear model)
- Reproducible code and artifacts

> ⚠️ Dataset is provided under `data/` as `Sample - Superstore.csv`.

---

## 1) Project Objectives
1. Identify revenue and profit drivers across **categories**, **regions**, and **discounting**.
2. Understand temporal sales patterns and trend shifts.
3. Build a **baseline monthly sales forecast** to support inventory and planning decisions.

## 2) Repository Structure
```
Superstore_Sales_Insights_And_Predictive_Analysis/
├─ data/
│  └─ Sample - Superstore.csv
├─ images/
│  ├─ monthly_sales.png
│  ├─ monthly_sales_trend.png
│  ├─ category_sales.png
│  ├─ region_profit.png
│  └─ correlation_heatmap.png
├─ notebooks/
│  └─ superstore_analysis.ipynb
├─ src/
│  └─ pipeline.py
├─ requirements.txt
└─ README.md
```

## 3) Quickstart
```bash
# (optional) create virtual environment
python -m venv .venv && . .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -r requirements.txt
jupyter lab  # or jupyter notebook
```

Open `notebooks/superstore_analysis.ipynb` to reproduce the analysis. All plots are also saved under `images/` for quick review.

## 4) Key Insights (Highlights)
- **Demand growth**: Monthly sales trend shows overall directionality with seasonal variability.
- **Category mix**: Certain categories/sub-categories dominate revenue; long tails remain important.
- **Discount-profit tension**: Higher discounting correlates with **lower profit** for many SKUs (see scatter).
- **Regional focus**: Top regions/states contribute disproportionately to profit.

## 5) Forecasting
A simple linear trend model is used to forecast **next 6 months** of sales as a baseline.  
Model: LinearRegression
R2: 0.251
MAE: 17457.73
RMSE: 21574.53
Next 6 months forecast: 69957.54, 70859.54, 71761.55, 72663.56, 73565.57, 74467.57

> Note: This is a baseline. For production, consider SARIMAX/Prophet or gradient-boosted models with richer features.

## 6) Reproducibility
- Deterministic sampling (random_state set where applicable)
- Code organized into a small pipeline (`src/pipeline.py`)
- Notebook contains full, executed analysis

## 7) Screenshots
See `/images` for all static visualizations.

## 8) License
This repo is intended for educational/portfolio demonstration.