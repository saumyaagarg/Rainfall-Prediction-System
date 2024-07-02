import streamlit as st
import pickle
import numpy as np
import os
import joblib
import pandas as pd
from streamlit_option_menu import option_menu

# Loading all the models
working_dir = os.path.dirname(os.path.abspath(__file__))
rainfall_model = pickle.load(open(f'{working_dir}/Rainfall_Ridge.sav', 'rb'))

st.set_page_config(
    page_title="Rainfall Prediction App",
    page_icon="🌧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Set background color
st.markdown( 
   """
    <style>
    body {
        background-color: #70BAFF !important;
    }
    .sidebar .sidebar-content {
        background-color: #5F79FF !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = "About"

# Sidebar
st.sidebar.title("Rainfall Predictor")
if st.sidebar.button("About"):
    st.session_state.page = "About"
if st.sidebar.button("Rainfall Predicition"):
    st.session_state.page = "Rainfall Prediction"

# Rainfall Prediction
if st.session_state.page == "Rainfall Prediction":
    st.title("Rainfall Prediction")
    st.write("Provide the following information to predict rainfall:")
    st.write("""
    - **Subdivision**: Select your geographical area.
    - **Year**: Enter the year for which you wish to predict rainfall.
    - **May Rainfall (mm)**: Amount of rainfall in May.
    - **June Rainfall (mm)**: Amount of rainfall in June.
    - **July Rainfall (mm)**: Amount of rainfall in July.
    - **August Rainfall (mm)**: Amount of rainfall in August.
    - **September Rainfall (mm)**: Amount of rainfall in September.
    """)
    # Define all subdivisions
    subdivisions = [
        'ANDAMAN & NICOBAR ISLANDS', 'ARUNACHAL PRADESH', 'ASSAM & MEGHALAYA', 'NAGA MANI MIZO TRIPURA',
        'SUB HIMALAYAN WEST BENGAL & SIKKIM', 'GANGETIC WEST BENGAL', 'ORISSA', 'JHARKHAND', 'BIHAR',
        'EAST UTTAR PRADESH', 'WEST UTTAR PRADESH', 'UTTARAKHAND', 'HARYANA DELHI & CHANDIGARH', 'PUNJAB',
        'HIMACHAL PRADESH', 'JAMMU & KASHMIR', 'WEST RAJASTHAN', 'EAST RAJASTHAN', 'WEST MADHYA PRADESH',
        'EAST MADHYA PRADESH', 'GUJARAT REGION', 'SAURASHTRA & KUTCH', 'KONKAN & GOA', 'MADHYA MAHARASHTRA',
        'MATATHWADA', 'VIDARBHA', 'CHHATTISGARH', 'COASTAL ANDHRA PRADESH', 'TELANGANA', 'RAYALSEEMA',
        'TAMIL NADU', 'COASTAL KARNATAKA', 'NORTH INTERIOR KARNATAKA', 'SOUTH INTERIOR KARNATAKA', 'KERALA',
        'LAKSHADWEEP'
    ]
    
    subdivision = st.selectbox("Subdivision", subdivisions)
    year = st.number_input("Year", min_value=1900, max_value=2100, value=2024)
    may = st.number_input("May Rainfall (mm)", min_value=0.0, value=0.0)
    jun = st.number_input("June Rainfall (mm)", min_value=0.0, value=0.0)
    jul = st.number_input("July Rainfall (mm)", min_value=0.0, value=0.0)
    aug = st.number_input("August Rainfall (mm)", min_value=0.0, value=0.0)
    sep = st.number_input("September Rainfall (mm)", min_value=0.0, value=0.0)
    
    if st.button("Predict Rainfall"):
        if subdivision and year:
            rainfall_input = {
                'SUBDIVISION': [subdivision],
                'YEAR': [year],
                'MAY': [may],
                'JUN': [jun],
                'JUL': [jul],
                'AUG': [aug],
                'SEP': [sep]
            }
            rainfall_input_df = pd.DataFrame(rainfall_input)
            
            # Predict if all inputs are provided
            if all(rainfall_input_df.iloc[0, 2:]):
                rainfall_prediction = rainfall_model.predict(rainfall_input_df)
                st.success(f"Predicted Rainfall: {rainfall_prediction[0]}")
            else:
                st.error("Please enter valid values")
        else:
            st.error("Please enter subdivision and year")



# Home
else:
    img = "img5.jpg"
    st.title("RainVision")
    st.write("##### Welcome to RainVision, your ultimate Rainfall Prediction App!")
    st.image(img, width=750)
    
    st.write("")  # Leave some space after the image
    st.write("RainVision is a cutting-edge application designed to assist farmers in making informed decisions based on precise annual rainfall predictions. By providing information such as subdivision, year, and rainfall in a few months in mm, users can know the annual rainfall prediction for that subdivision in the mentioned year in mm.")

    st.write("""
        ### How to Use the App
        1. Navigate to the "Rainfall Prediction" section.
        2. Enter the values in the input fields.
        3. Click the "Predict" button to get the rainfall prediction.
    """)

    st.write("""
        ### Contact Us
        If you have any questions or feedback about the project, feel free to reach out:
        - **Email**: saumyaagarg1720@gmail.com
        - **Github**: https://github.com/saumyaagarg
    """)
