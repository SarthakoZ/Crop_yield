# Project Context

This file gives background context on the project — useful for collaborators, future-you, or any AI assistant picking up this repo later.

## What this project is

A learning/portfolio project: cleaning a deliberately messy agricultural dataset and building a **Linear Regression** model to predict crop yield (`yield_ton_per_hectare`) from environmental and farming-practice features.

## Author

**SarthakoZ**

## Goal

- Practice a realistic end-to-end regression workflow: messy data → cleaning → train/test split → imputation → encoding → model training → evaluation.
- Not intended (yet) as a production system — it's a learning exercise that can be extended (see README "Future Upgradation" section).

## Why the dataset is "messy"

`Crop_Yield_Messy_Dataset_500.xlsx` was intentionally created/collected with realistic data quality issues to practice cleaning:

- Inconsistent casing and whitespace in text columns (`State`, `District`, `Crop`, `Season`, `Soil_Type`).
- Inconsistent naming for the same entity (e.g. `WB`, `westbengal`, `West Bengal` all refer to the same state).
- Negative values in numeric columns used as invalid/sentinel data (physically impossible, e.g. negative rainfall) — these are treated as missing.
- Missing values scattered across nearly every numeric column and a few categorical ones.
- Duplicate rows.

## Key design decisions made in the notebook

1. **Train/test split happens before imputation.** This is intentional and correct — imputing before splitting would leak information from the test set into training (data leakage). The imputer is `fit` only on `X_train` and then used to `transform` both `X_train` and `X_test`.
2. **Median imputation for numeric columns** — chosen over mean because it's more robust to outliers in the data (rainfall, humidity, etc. have wide ranges).
3. **Most-frequent imputation for categorical columns** — standard, simple baseline strategy for a small number of missing categorical entries.
4. **Label encoding for `irrigation`** — appropriate since it's binary (Yes/No), no ordinal relationship issue.
5. **One-hot encoding for `state`, `district`, `crop`, `season`, `soil_type`** — used because these are nominal categories with no inherent order. Note: `crop` (30 unique values) and `district` will create many new columns; this is flagged in the README as a future improvement (consider target encoding to reduce dimensionality).

## State of the notebook

The notebook currently stops right after preprocessing/feature engineering (cleaning, imputing, encoding). **Model training and evaluation have not been added yet** — that's the immediate next step (see README → "Model Training (Next Step)").

## Intended next steps (short term)

1. Re-run the notebook top to bottom to ensure all cells execute in order.
2. Actually fit `LinearRegression` on the processed features and evaluate on the test set (MAE, RMSE, R²).
3. Move the local Windows file path (`D:\PYTHON\...`) to a relative path so the project runs on any machine.

## How to resume work on this project

If you (or an AI assistant) are picking this back up:
1. Read `README.md` for setup and structure.
2. Open `crop_source.ipynb`, run all cells top-to-bottom.
3. Check the "Future Upgradation" checklist in the README for what's left to do.
