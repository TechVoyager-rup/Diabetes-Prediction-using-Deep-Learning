#!/usr/bin/env python3
"""Diabetes Predictor – Streamlit app with enhanced UI and lifestyle advice
===========================================================================
Adds detailed positive guidance for healthy users and actionable, cautionary
advice for users flagged as diabetic. Core prediction logic untouched.
"""
import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras import models

# -----------------------------------------------------------------------------
# 🎨 Page config & CSS
# -----------------------------------------------------------------------------

st.set_page_config(
    page_title="Diabetes Predictor",
    page_icon="💉",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
        body { background: linear-gradient(120deg,#fdfbfb 0%,#ebedee 100%); font-family:'Segoe UI',sans-serif; }
        h1.title { color:#D7263D; text-align:center; padding-bottom:0.2em; margin-bottom:0.5em; border-bottom:4px solid #F46036; }
        table { border-collapse:collapse; width:100%; }
        thead th { background:#1F77B4; color:white; }
        tbody tr:nth-child(odd) { background:#F1F3F4; }
        .stNotification.success { background-color:#E0F7FA; color:#006064; }
        .stNotification.warning { background-color:#FFF8E1; color:#F57F17; }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------------------------------------------------------
# 📊 Data & scaler
# -----------------------------------------------------------------------------

df = pd.read_csv("diabetes.csv")
X = df.drop("Outcome", axis=1)
y = df["Outcome"]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# retain split for completeness
_, _, _, _ = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# -----------------------------------------------------------------------------
# 🖥️ Layout
# -----------------------------------------------------------------------------

st.markdown("<h1 class='title'>Diabetes Predictor</h1>", unsafe_allow_html=True)

with st.sidebar:
    st.header("📝 Patient Details")
    patient_name = st.text_input("Patient Name", "")
    st.markdown("---")
    st.subheader("Health Metrics")
    pg = st.slider("Pregnancies", 0, 17, 1)
    glucose = st.slider("Glucose", 0, 300, 120)
    bp = st.slider("Blood Pressure (Systolic, mm Hg)", 60, 180, 120)
    skin = st.slider("Skin Thickness (mm)", 0, 100, 20)
    insulin = st.slider("Insulin (μU/mL)", 0, 850, 80)
    bmi = st.slider("BMI", 0.0, 80.0, 24.0)
    heritability = st.slider("Diabetes Pedigree Function", 0.0, 3.0, 0.4)
    age = st.slider("Age", 21, 90, 21)

    user_record = {
        "Pregnancies": pg,
        "Glucose": glucose,
        "BloodPressure": bp,
        "SkinThickness": skin,
        "Insulin": insulin,
        "BMI": bmi,
        "DiabetesPedigreeFunction": heritability,
        "Age": age,
    }

# -----------------------------------------------------------------------------
# ⚙️ Prediction
# -----------------------------------------------------------------------------

user_df = pd.DataFrame(user_record, index=[0])
user_scaled = scaler.transform(user_df)
model = models.load_model("Models/ann_model.h5")
prediction = model.predict(user_scaled)[0][0]

# -----------------------------------------------------------------------------
# 📋 Output
# -----------------------------------------------------------------------------

col1, col2 = st.columns(2, gap="large")

with col1:
    st.subheader("🔎 Entered Data")
    if patient_name:
        st.write(f"**Patient Name:** {patient_name}")
    st.table(user_df.T.rename(columns={0: "Value"}))

with col2:
    st.subheader("🩺 Diagnostic Report")
    if prediction <= 0.5:
        st.success("You are healthy 🎉")
        st.markdown(
            """
            **Keep up the good work!** Here are evidence‑based habits to maintain optimal metabolic health:
            - **Stay active:** Aim for at least *150 minutes* of moderate‑intensity exercise (e.g., brisk walking, cycling) each week.
            - **Balanced plate:** Fill half your plate with colourful vegetables, one quarter with lean protein, and one quarter with whole‑grain carbs.
            - **Limit added sugars & ultra‑processed foods**—they spike glucose and promote weight gain.
            - **Hydrate wisely:** Water or unsweetened drinks instead of sugary sodas or juices.
            - **Sleep 7–8 hours nightly:** Poor sleep increases insulin resistance.
            - **Stress management:** Practice yoga, meditation, or deep‑breathing; chronic stress raises cortisol and blood sugar.
            - **Annual check‑up:** Include fasting glucose / HbA1c to catch any early changes.
            """,
            unsafe_allow_html=False,
        )
    else:
        st.warning("You are Diabetic ⚠️")
        st.markdown(
            """
            **Action plan to regain control:**
            - **Consult a diabetologist or certified diabetes educator** to personalise medication and lifestyle targets.
            - **Adopt a low‑GI, high‑fibre diet:** swap white rice/bread for brown rice, oats, and legumes; increase non‑starchy veggies.
            - **Structured exercise:** Mix *150–300 minutes* of aerobic activity with 2 days of resistance training weekly to improve insulin sensitivity.
            - **Weight management:** Losing just *5–7 %* of body weight can markedly reduce HbA1c.
            - **Regular self‑monitoring:** Track fasting glucose and (if prescribed) post‑meal levels; keep a log for your clinician.
            - **Stay hydrated & avoid sugary drinks**; choose water, soda‑water with lime, or unsweetened tea.
            - **Quit smoking & limit alcohol**—both impair glucose control and raise cardiovascular risk.
            - **Stress reduction:** Mindfulness, journaling, or counselling can blunt cortisol‑driven glucose surges.
            Remember, small consistent steps outperform drastic unsustainable changes.
            """,
            unsafe_allow_html=False,
        )

# -----------------------------------------------------------------------------
# 🔚 Footer
# -----------------------------------------------------------------------------

st.markdown(
    """
    <hr/>
    <div style='text-align:center;'>
        <small>Made with ❤️ by RUPANJAN GHOSH</small>
    </div>
    """,
    unsafe_allow_html=True,
)
