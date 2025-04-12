import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant", layout="wide", page_icon="🧑‍⚕️")

# Custom CSS for styling
st.markdown("""
    <style>
    .stForm button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        height: 3em;
        width: 100%;
    }
    .stForm button:hover {
        background-color: #45a049;
    }
    .big-font {
        font-size:22px !important;
        font-weight: bold;
    }
    .prediction-box {
        background-color: #f5f5f5;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Load models
working_dir = os.path.dirname(os.path.abspath(__file__))
diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open(f'{working_dir}/saved_models/parkinsons_model.sav', 'rb'))

# Sidebar Navigation
with st.sidebar:
    selected = option_menu(
        menu_title='🩺 Health Assistant',
        options=['Diabetes Prediction', 'Heart Disease Prediction', "Parkinsons Prediction"],
        icons=['activity', 'heart-pulse', 'person'],
        menu_icon='hospital',
        default_index=0
    )

# ------------------- Diabetes Prediction -------------------
if selected == 'Diabetes Prediction':
    st.markdown("## 🧪 Diabetes Prediction")
    st.markdown("Fill in the form to check for diabetes risk.")

    with st.form(key='diabetes_form'):
        col1, col2, col3 = st.columns(3)
        with col1:
            Pregnancies = st.number_input('👶 Number of Pregnancies', min_value=0)
            SkinThickness = st.number_input('🧍 Skin Thickness')
            BMI = st.number_input('📏 BMI')
        with col2:
            Glucose = st.number_input('🍬 Glucose Level')
            Insulin = st.number_input('💉 Insulin Level')
            DiabetesPedigreeFunction = st.number_input('🧬 Pedigree Function')
        with col3:
            BloodPressure = st.number_input('🩸 Blood Pressure')
            Age = st.number_input('📅 Age')

        submitted = st.form_submit_button("🔍 Predict Diabetes")

        if submitted:
            user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
            prediction = diabetes_model.predict([user_input])
            with st.container():
                st.markdown('<div class="prediction-box">', unsafe_allow_html=True)
                if prediction[0] == 0:
                    st.success("✅ The person is **not diabetic**.")
                else:
                    st.error("⚠️ The person **is diabetic**.")
                st.markdown('</div>', unsafe_allow_html=True)

# ------------------- Heart Disease Prediction -------------------
elif selected == 'Heart Disease Prediction':
    st.markdown("## ❤️ Heart Disease Prediction")
    st.markdown("Fill in the form to check for heart disease risk.")

    with st.form(key='heart_form'):
        col1, col2, col3 = st.columns(3)
        with col1:
            age = st.number_input('📅 Age')
            trestbps = st.number_input('🩺 Resting Blood Pressure')
            restecg = st.number_input('📉 ECG Results')
            oldpeak = st.number_input('📊 ST Depression')
            thal = st.number_input('🧪 Thal (0=normal, 1=fixed, 2=reversible)')
        with col2:
            sex = st.selectbox('⚧️ Sex', ['0 - Female', '1 - Male'])
            chol = st.number_input('🧈 Serum Cholesterol')
            thalach = st.number_input('🏃 Max Heart Rate')
            slope = st.number_input('📈 Slope of ST Segment')
        with col3:
            cp = st.number_input('💓 Chest Pain Type')
            fbs = st.number_input('🧪 Fasting Blood Sugar > 120 (1=True, 0=False)')
            exang = st.number_input('🏋️ Exercise Induced Angina')
            ca = st.number_input('🔬 Major Vessels (0–3)')

        submitted = st.form_submit_button("🔍 Predict Heart Disease")

        if submitted:
            user_input = [age, int(sex[0]), cp, trestbps, chol, fbs, restecg,
                          thalach, exang, oldpeak, slope, ca, thal]
            prediction = heart_disease_model.predict([user_input])
            with st.container():
                st.markdown('<div class="prediction-box">', unsafe_allow_html=True)
                if prediction[0] == 0:
                    st.success("✅ The person **does not have heart disease**.")
                else:
                    st.error("⚠️ The person **has heart disease**.")
                st.markdown('</div>', unsafe_allow_html=True)

# ------------------- Parkinson's Prediction -------------------
elif selected == "Parkinsons Prediction":
    st.markdown("## 🧠 Parkinson's Disease Prediction")
    st.markdown("Enter the required voice parameters:")

    with st.form(key='parkinsons_form'):
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            fo = st.number_input('Fo (Hz)')
            RAP = st.number_input('RAP')
            APQ3 = st.number_input('APQ3')
            HNR = st.number_input('HNR')
            spread1 = st.number_input('Spread1')
            PPE = st.number_input('PPE')
        with col2:
            fhi = st.number_input('Fhi (Hz)')
            PPQ = st.number_input('PPQ')
            APQ5 = st.number_input('APQ5')
            RPDE = st.number_input('RPDE')
            spread2 = st.number_input('Spread2')
        with col3:
            flo = st.number_input('Flo (Hz)')
            DDP = st.number_input('DDP')
            APQ = st.number_input('APQ')
            DFA = st.number_input('DFA')
            D2 = st.number_input('D2')
        with col4:
            Jitter_percent = st.number_input('Jitter (%)')
            Jitter_Abs = st.number_input('Jitter (Abs)')
            Shimmer = st.number_input('Shimmer')
            Shimmer_dB = st.number_input('Shimmer (dB)')
            DDA = st.number_input('DDA')
            NHR = st.number_input('NHR')

        submitted = st.form_submit_button("🔍 Predict Parkinson's")

        if submitted:
            user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP,
                          Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR,
                          RPDE, DFA, spread1, spread2, D2, PPE]
            prediction = parkinsons_model.predict([user_input])
            with st.container():
                st.markdown('<div class="prediction-box">', unsafe_allow_html=True)
                if prediction[0] == 0:
                    st.success("✅ The person **does not have Parkinson's disease**.")
                else:
                    st.error("⚠️ The person **has Parkinson's disease**.")
                st.markdown('</div>', unsafe_allow_html=True)
