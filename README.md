---

# ❤️ Heart Disease Prediction using Machine Learning and Flask

This project aims to predict the presence of heart disease in patients using machine learning and provide a simple web interface built with Flask. Early diagnosis can enable timely treatment and improve survival rates.

---

## 📊 Project Overview

- **Problem**: Heart disease remains one of the leading causes of death globally. Early detection is vital.
- **Solution**: A machine learning model trained to detect heart disease based on patient health data.
- **Goal**: Develop an accurate prediction model and make it accessible through a web-based tool.

---

## 📁 Dataset

- **Source**: [UCI Heart Disease Dataset](https://archive.ics.uci.edu/ml/datasets/heart+Disease)
- **Attributes Used**:
  - Age  
  - Sex  
  - Chest pain type  
  - Resting blood pressure  
  - Serum cholesterol  
  - Fasting blood sugar  
  - Resting ECG results  
  - Max heart rate achieved  
  - Exercise-induced angina  
  - ST depression  
  - Slope of the ST segment  
  - Number of major vessels  
  - Thalassemia  
  - **Target** (0 = no disease, 1 = disease)

---

## ⚙️ Technologies Used

- **Python**
- **Pandas, NumPy** for data processing
- **Matplotlib, Seaborn** for data visualization
- **Scikit-learn** for ML modeling
- **Flask** for web application
- **HTML/CSS** for front-end

---

## 🚀 Models Trained

- Logistic Regression  
- Decision Tree  
- Random Forest ✅ *(Best performance)*  
- Support Vector Machine  
- K-Nearest Neighbors

---

## 📈 Evaluation Metrics

- Accuracy  
- Precision  
- Recall  
- F1-Score  
- Confusion Matrix  
- ROC-AUC Curve

---

## 🖥️ Web Application

A simple and intuitive **Flask-based web app** is built to interact with the ML model. Users can input health parameters and receive instant predictions.

### 🌐 App Features

- User-friendly input form for medical data
- Real-time prediction result (Heart Disease: Yes/No)
- Model loaded using `joblib`
- Pages:
  - `/` → Input Form
  - `/predict` → Prediction result

---

## 🏗️ Project Structure

```
heart-disease-predictor/
├── app.py                      # Flask application
├── models/
│   └── model.joblib            # Trained model
├── templates/
│   ├── index.html              # Input form UI
│   └── result.html             # Output UI
├── notebook/
│   └── Heart_Disease_Prediction.ipynb  # ML model development
├── static/                     # CSS or assets
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

### 💻 Run the Machine Learning Notebook

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/heart-disease-predictor.git
   cd heart-disease-predictor
   ```

2. Install required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Open and run the notebook:
   ```bash
   jupyter notebook notebook/Heart_Disease_Prediction.ipynb
   ```

### 🌐 Run the Flask Web App

1. Make sure `model.joblib` exists in the `models/` directory.

2. Start the Flask app:
   ```bash
   python app.py
   ```

3. Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

---

## 🏥 Real-World Applications

- Assist doctors with early screening
- Use in health camps and mobile clinics
- Add-on for digital health platforms

---

## 🔮 Future Work

- Mobile-friendly interface
- Model interpretability with SHAP or LIME
- Integration with health wearables
- Deploy on cloud (Heroku, Render, etc.)

---

## 🤝 Contributing

Pull requests are welcome! Please open an issue first to discuss major changes.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♀️ Author

**Bhumi Jain**  
*Data Science & Machine Learning Enthusiast*  
---
