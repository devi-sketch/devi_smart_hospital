import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

st.set_page_config(page_title="Smart Hospital Patient Navigator", page_icon="🏥", layout="wide")

@st.cache_resource
def load_model():
    with open('hospital_model.pkl', 'rb') as f:
        return pickle.load(f)

bundle        = load_model()
model         = bundle['model']
scaler        = bundle['scaler']
features      = bundle['features']
cols_to_scale = bundle['cols_to_scale']
dept_map_inv  = bundle['dept_map_inv']
gender_map    = bundle['gender_map']
temp_map      = bundle['temp_map']
hr_map        = bundle['hr_map']
dur_map       = bundle['dur_map']
cc_map        = bundle['cc_map']
    
# ── Hero Header ───────────────────────────────────────────────────────────────
st.markdown("""
<div style="background:linear-gradient(135deg,#1e3a8a 0%,#1a56db 60%,#0ea5e9 100%);
            padding:3rem 2rem 2.5rem;margin:-1rem -1rem 2rem;text-align:center;">
    <div style="font-size:14px;font-weight:500;color:rgba(255,255,255,0.7);
                text-transform:uppercase;letter-spacing:0.1em;margin-bottom:12px;">
        🏥 Future Classroom · Machine Learning
    </div>
    <div style="font-size:36px;font-weight:700;color:#ffffff;margin-bottom:12px;
                letter-spacing:-0.02em;">
        Smart Hospital Patient Navigator
    </div>
    <div style="font-size:18px;color:rgba(255,255,255,0.85);font-weight:400;">
        Find the Right Department for Your Symptoms
    </div>
</div>
""", unsafe_allow_html=True)
