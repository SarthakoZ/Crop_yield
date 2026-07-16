# Crop Yield Prediction — Linear Regression

Predicting crop yield (tons/hectare) from agricultural and environmental features using a linear regression pipeline built with `pandas` and `scikit-learn`.

**Author:** [SarthakoZ](https://github.com/SarthakoZ)

---

## 📌 Project Overview

This project cleans a messy, real-world-style agricultural dataset and trains a regression model to predict `yield_ton_per_hectare` based on features like state, district, crop, season, soil type, rainfall, temperature, humidity, fertilizer usage, and irrigation status.

## 📂 Dataset

**File:** `Crop_Yield_Messy_Dataset_500.xlsx`

| Property | Value |
|---|---|
| Rows | 510 |
| Columns | 15 |
| Target column | `Yield_ton_per_hectare` |

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

The notebook (`crop_source.ipynb`) performs the following steps:

1. Load the Excel file and drop duplicate rows.
2. Normalize column names (strip whitespace, lowercase).
3. Treat negative numeric values as invalid → converted to `NaN`.
4. Standardize categorical text (strip + lowercase) for `state`, `district`, `crop`, `season`.
5. Fix inconsistent state naming (e.g. `wb`, `westbengal` → `west bengal`).
6. Train/test split (80/20, `random_state=42`) **before** imputing, to avoid data leakage.
7. Impute missing numeric values with the **median** (`SimpleImputer`).
8. Impute missing categorical values with the **most frequent** value.
9. Encode `irrigation` (binary) with `LabelEncoder`.
10. One-hot encode `state`, `district`, `crop`, `season`, `soil_type` with `OneHotEncoder`.
11. Merge encoded columns back into the feature set for modeling.

## 🛠️ Tech Stack

- Python 3.10+
- pandas
- numpy
- scikit-learn
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

# 4. Launch the notebook
jupyter notebook crop_source.ipynb
```

Update the dataset path in the first cell if needed — it currently points to a local Windows path and should be changed to a relative path such as `data/Crop_Yield_Messy_Dataset_500.xlsx`.

## 📁 Project Structure

```
.
├── crop_source.ipynb                      # Main notebook: cleaning + preprocessing + model
├── Crop_Yield_Messy_Dataset_500.xlsx       # Raw dataset
├── README.md
├── CONTEXT.md
├── requirements.txt
└── .gitignore
```

## 📈 Model Training (Next Step)

Once preprocessing is fixed, the pipeline is ready for:

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("MAE:", mean_absolute_error(y_test, y_pred))
print("RMSE:", mean_squared_error(y_test, y_pred, squared=False))
print("R²:", r2_score(y_test, y_pred))
```

## 🔭 Future Upgradation

- [ ] Replace the hardcoded local file path with a relative path so the notebook is portable.
- [ ] Wrap the manual preprocessing (imputers, encoders) into a single `sklearn.pipeline.Pipeline` / `ColumnTransformer` to avoid train/test leakage risk and make the code reusable.
- [ ] Add exploratory data analysis (EDA): correlation heatmap, distribution plots, outlier detection.
- [ ] Try regularized linear models (`Ridge`, `Lasso`, `ElasticNet`) to handle multicollinearity from one-hot encoded categorical features.
- [ ] Compare against non-linear models (Random Forest, Gradient Boosting, XGBoost) as a benchmark.
- [ ] Add cross-validation (`KFold` / `cross_val_score`) instead of a single train/test split for more robust evaluation.
- [ ] Add residual analysis plots (predicted vs. actual, residuals vs. predicted) to check linear regression assumptions.
- [ ] Perform feature importance / coefficient analysis to identify which factors most affect yield.
- [ ] Handle high-cardinality categorical columns (e.g. `crop`, `district`) with target encoding instead of one-hot, to reduce dimensionality.
- [ ] Save the trained model with `joblib`/`pickle` and add a simple prediction script or API (e.g. Flask/FastAPI) for real-world use.
- [ ] Add unit tests for the preprocessing functions.
- [ ] Convert the notebook into modular `.py` scripts (`data_prep.py`, `train.py`, `predict.py`) for production readiness.
- [ ] Add logging and error handling instead of relying on manual notebook re-runs.
- [ ] Set up a CI workflow (GitHub Actions) to lint and test the code on every push.
