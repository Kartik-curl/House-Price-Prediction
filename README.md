# 🏠 House Price Prediction System

A Machine Learning web application built using **Flask**, **Pandas**, and **Scikit-learn** that predicts house prices based on user-provided features. The project follows an **ETL (Extract, Transform, Load) pipeline** for data preprocessing and uses a **Linear Regression** model for prediction.

---

## 📌 Features

* Predicts house prices from user inputs
* Web interface built with Flask
* Data preprocessing using an ETL pipeline
* Categorical feature encoding using Label Encoding
* Trained using Scikit-learn's Linear Regression
* Model serialization using Pickle
* Easy deployment and extension

---

## 🛠️ Tech Stack

* **Python 3**
* **Flask**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Pickle**

---

## 📂 Project Structure

```text
House-Price-Prediction/
│
├── templates/
│   └── index.html
│
├──dataset.csv
├── app.py
├── model.py
├── model.pkl
├── extracted.pkl
├── labelenc.pkl
├── requirements.txt
└── README.md
```

---

## 🔄 ETL Pipeline

### 1. Extract

* Load the housing dataset using Pandas.

### 2. Transform

* Handle missing values.
* Encode categorical features using Label Encoding.
* Perform necessary feature engineering and preprocessing.

### 3. Load

* Save the processed data and encoders.
* Train the Linear Regression model and save it as `model.pkl`.

---

## 🤖 Machine Learning Model

The project uses **Linear Regression** to learn the relationship between house features and price.

### Training Steps

1. Load dataset.
2. Preprocess data through the ETL pipeline.
3. Encode categorical columns.
4. Split data into training and testing sets.
5. Train the Linear Regression model.
6. Save:

   * `model.pkl` → Trained model
   * `labelenc.pkl` → Label encoder
   * `extracted.pkl` → Processed data/components

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/Kartik-curl/House-Price-Prediction.git

cd house-price-prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000/
```

---

## 📋 Requirements

Example `requirements.txt`:

```text
Flask
pandas
numpy
scikit-learn
```

---

## 📊 Workflow

```text
Dataset
   │
   ▼
Extract
   │
   ▼
Transform (Cleaning + Encoding)
   │
   ▼
Train Linear Regression
   │
   ▼
Save Model (.pkl)
   │
   ▼
Flask Application
   │
   ▼
User Input
   │
   ▼
Prediction
```

---
## 📈 Model Performance

The Linear Regression model achieved excellent predictive performance on the evaluation dataset.

| Metric                                    | Value         |
| ----------------------------------------- | ------------- |
| **Mean Absolute Percentage Error (MAPE)** | **2.1%**      |
| **R² Score**                              | **0.9999656** |
| **Approximate Prediction Accuracy**       | **99.99%**    |

### Performance Summary

* ✅ **Average MAPE:** **2.1%**, indicating that the model's predictions differ from the actual house prices by only about 2.1% on average.
* ✅ **R² Score:** **0.9999656**, showing that the model explains nearly all of the variance in the target variable.
* ✅ The model provides **approximately 99.99% accurate predictions** on the evaluated dataset, demonstrating a very strong fit for the available data.

> **Note:** The reported performance metrics are based on the dataset and evaluation methodology used during model development. Actual performance on unseen real-world data may vary depending on data distribution and input quality.
---

## 🎯 Future Improvements

* Support multiple ML algorithms.
* Add feature scaling and hyperparameter tuning.
* Integrate a database for storing predictions.
* Deploy the application on Render, Railway, or AWS.
* Improve UI using Bootstrap or React.

---

## 👨‍💻 Author

**Kartik Thakur**

AI & Machine Learning Enthusiast | Python Developer

---

## 📜 License

This project is for educational and learning purposes. Feel free to modify and extend it for your own use.
