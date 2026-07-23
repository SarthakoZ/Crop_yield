# Crop Yield Prediction — Linear Regression

Predicting crop yield (tons/hectare) from agricultural and environmental features using a linear regression pipeline built with `pandas` and `scikit-learn`.

**Author:** [SarthakoZ](https://github.com/SarthakoZ)

**🔗 Live App:** [cropyield-4mtk2x4lubhk8bxu4qutqn.streamlit.app](https://cropyield-4mtk2x4lubhk8bxu4qutqn.streamlit.app/)

---

## 📌 Project Overview

This project cleans a messy, real-world-style agricultural dataset, builds a `scikit-learn` preprocessing + modeling pipeline, and predicts `yield_ton_per_hectare` based on features like state, district, crop, season, soil type, rainfall, temperature, humidity, fertilizer usage, and irrigation status. The final model is deployed as an interactive Streamlit app.

## 📂 Dataset

**File:** `Crop_Yield_Messy_Dataset_500.xlsx`

| Property | Value |
|---|---|
| Rows | 510 |
| Columns | 15 |
| Target column | `yield_ton_per_hectare` |

**Columns:**

| Column | Type | Notes |
|---|---|---|
| State | categorical | inconsistent casing/abbreviations (e.g. `WB`, `westbengal`) |
| District | categorical | |
| Crop | categorical | 30 unique crop types |
| Season | categorical | Kharif / Rabi / Zaid |
| Area_Hectare | numeric | contains missing values |
| Rainfall_mm | numeric | contains missing values |
| Temperature_C | numeric | contains missing values |
| Humidity | numeric | contains missing values |
| Soil_Type | categorical | contains missing values |
| Nitrogen | numeric | contains missing values |
| Phosphorus | numeric | contains missing values |
| Potassium | numeric | contains missing values |
| Fertilizer_Used | numeric | contains missing values |
| Irrigation | categorical (Yes/No) | contains missing values |
| Yield_ton_per_hectare | numeric | **target variable** |

The dataset is intentionally messy: mixed-case text, inconsistent state naming, negative values used as sentinel errors, and missing values scattered across most numeric and a few categorical columns.

## 🧹 Data Cleaning & Preprocessing

The notebook (`Source.ipynb`) performs the following steps:

1. Load the Excel file, strip/lowercase column names, and drop duplicate rows.
2. Treat negative numeric values as invalid → converted to `NaN`.
3. Standardize categorical text (strip + lowercase) across all object columns.
4. Fix inconsistent state naming (e.g. `wb` → `west bengal`).
5. Train/test split (80/20, `random_state=42`) **before** any imputing or encoding, to avoid data leakage.
6. Build a `ColumnTransformer` with two branches:
   - **Numeric pipeline:** median imputation (`SimpleImputer`) → `MinMaxScaler`.
   - **Categorical pipeline:** most-frequent imputation → `OneHotEncoder(handle_unknown="ignore")`.
7. Wrap the preprocessor and estimator together in a single `sklearn.pipeline.Pipeline`, so imputing, scaling, and encoding are all fit only on training data and applied consistently at inference time.

## 🤖 Model Training & Selection

Three regression models were trained on the same preprocessing pipeline and compared on the held-out test set (R²):

| Model | R² Score (test split) | Avg. R² (5-fold CV) | Status |
|---|---|---|---|
| **Linear Regression** | highest | **0.6764** | ✅ Selected |
| Random Forest Regressor | — | 0.6324 | Evaluated |
| XGBoost Regressor | — | 0.6040 | Evaluated |

Model selection was based on 5-fold cross-validation (`cross_val_score`, `scoring="r2"`) rather than a single train/test split, for a more robust comparison. **Linear Regression** was chosen as the final model since it achieved the highest average cross-validation R² (0.6764) among all three.

Additional evaluation performed:
- MAE, MSE, RMSE, and R² on the held-out test set for each model.
- Coefficient-based feature importance analysis on the final Linear Regression pipeline (via `get_feature_names_out()` on the fitted preprocessor).

The final fitted pipeline (preprocessing + Linear Regression) is serialized with `joblib` as `crop_yield_prediction_model.pkl`.

## 🖥️ Streamlit App

A Streamlit front end (`dev.py`) wraps the saved pipeline in an interactive form:

- Inputs are grouped into four columns — **Crop Information**, **Soil Information**, **Weather Conditions**, and **Farming Details** — with cascading dropdowns (state → district/soil options, season → crop options).
- Clicking **🌾 Predict Crop Yield** builds a single-row DataFrame from the inputs, runs it through the pipeline, and displays the predicted yield along with the submitted details.
- The sidebar and main page surface the model choice and its average cross-validation R² score (0.6764), plus a comparison table against Random Forest and XGBoost.

**Try it live:** https://cropyield-7gfdgahslcjw3fxo6uf2kj.streamlit.app/

## 🛠️ Tech Stack

- Python 3.10+
- pandas, numpy
- scikit-learn
- xgboost
- streamlit
- joblib
- openpyxl (Excel file support)
- jupyter / notebook

## 🚀 Getting Started

```bash
# 1. Clone the repo
git clone https://github.com/SarthakoZ/crop-yield-regression.git
cd crop-yield-regression

# 2. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4a. Launch the notebook (data cleaning + training)
jupyter notebook Source.ipynb

# 4b. Or run the Streamlit app directly (uses the saved model)
streamlit run dev.py
```

Update the dataset path in the first notebook cell if needed — it currently points to a local Windows path and should be changed to a relative path such as `data/Crop_Yield_Messy_Dataset_500.xlsx`.

## 📁 Project Structure

```
.
├── Source.ipynb                        # Main notebook: cleaning + pipeline + model comparison
├── app.py                              # Streamlit app (loads crop_yield_prediction_final_model.pkl)
├── crop_yield_prediction_final_model.pkl     # Serialized final pipeline (Linear Regression)
├── Crop_Yield_Messy_Dataset_500.xlsx   # Raw dataset
├── README.md
├── CONTEXT.md
├── requirements.txt
└── .gitignore
```

## ✅ Status

The project is complete and deployed. Try the live app: https://cropyield-4mtk2x4lubhk8bxu4qutqn.streamlit.app/
