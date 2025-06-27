# 🩺 Diabetes Predictor

A Streamlit web-app that screens for Diabetes risk using Artificial Neural Network (ANN).  
Simply enter a patient’s basic health metrics and the app returns an **instant likelihood of diabetes** plus personalised lifestyle guidance.

---

## ✨ Key Features
| Category | Details |
|----------|---------|
| **One-click deploy** | Runs locally or on Streamlit Cloud with `streamlit run app.py`. |
| **Clean, modern UI** | Gradient background, big headline, responsive sidebar inputs. |
| **Accurate ANN model** | Trained on the Pima Indians Diabetes dataset; achieves ±⁠78-80 % test accuracy. |
| **Actionable feedback** | • **Healthy users**: positive habit checklist.<br>• **At-risk users**: step-by-step caution plan. |
| **Fully open-source** | All code, data and weights included for transparency and retraining. |

---

## 🗂️ Project Structure
```
├── app.py                # Streamlit UI & inference logic
├── Diabetes Prediction.ipynb  # Model training notebook
├── Models/
│   └── ann_model.h5      # Saved Keras model
├── diabetes.csv          # Raw dataset (768 × 9)
└── README.md             # <— you are here
```

---

## 🚀 Quick Start

```bash
# 1. Clone
git clone https://github.com/TechVoyager-rup/Diabetes-Prediction-using-Deep-Learning.git
cd Diabetes-Prediction-using-Deep-Learning

# 2. Create env (optional)
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3. Launch
streamlit run app.py
```

Then open the printed localhost URL in your browser.

---

## ⚙️ How It Works
1. **Input capture** – Pregnancies, Glucose, Blood Pressure, Skin Thickness, Insulin, BMI, Diabetes Pedigree Fn, Age.  
2. **Scaling** – Features normalised with `StandardScaler` fitted on the training set.  
3. **Inference** – Scaled vector passed to a Keras ANN (`ann_model.h5`).  
4. **Decision rule** – Probability ≤ 0.50 → _Healthy_; otherwise → _Diabetic_.  
5. **Guidance** – Markdown snippets rendered according to outcome.

---

## 📊 Dataset

| Field | Description |
|-------|-------------|
| Pregnancies | Number of pregnancies |
| Glucose | Plasma glucose (mg/dL) |
| BloodPressure | Diastolic BP (mm Hg) |
| SkinThickness | Triceps skinfold (mm) |
| Insulin | 2-hr serum insulin (µU / mL) |
| BMI | Body-Mass Index (kg / m²) |
| DiabetesPedigreeFunction | Family history score |
| Age | Years |
| Outcome | 0 = non-diabetic, 1 = diabetic |

> Source: Pima Indians Diabetes Database (UCI ML Repo / Kaggle).

---

## 🩹 Disclaimer  
This tool **does not provide a medical diagnosis**. It is intended for educational purposes. Always consult a qualified clinician before making health decisions.

---

## 🤝 Contributing
Pull requests are welcome! Please open an issue first to discuss your ideas.

---

## 🙏 Acknowledgements
* **UCI / Kaggle** for the Pima Indians Diabetes dataset  
* **Streamlit** for the rapid UI framework  
* **TensorFlow / Keras** for the deep-learning engine  
* CSS gradient: [https://uigradients.com](https://uigradients.com)

---

Made with ❤️ by **Rupanjan Ghosh**  
Feel free to connect on [LinkedIn](https://www.linkedin.com/in/rupanjan-ghosh/)!
