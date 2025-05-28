import streamlit as st
import pandas as pd
import numpy as np

# Simulated plan database
plans = [
    {
        "name": "$20 Carryover Plan",
        "data_limit": 5,
        "price": 20,
        "recommendation_reason": "You’re currently under your data limit – this plan offers great value and includes daily Free Data Hour."
    },
    {
        "name": "$25 Carryover Plan",
        "data_limit": 10,
        "price": 25,
        "recommendation_reason": "You’ve been using more data lately – this plan gives you extra breathing room for just $5 more."
    },
    {
        "name": "$32.50 Carryover Plan",
        "data_limit": 80,
        "price": 32.50,
        "recommendation_reason": "You’re a heavy data user – this plan gives you plenty of space and all the perks."
    }
]

# App UI setup
st.set_page_config(page_title="PlanPal AI Assistant", page_icon="📱", layout="centered")

st.markdown("""
    <style>
    .main {
        background-color: #ffffff;
    }
    .stButton>button {
        color: white;
        background-color: #0074c2;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📱 PlanPal AI Assistant")
st.subheader("Kia ora, Micole 👋")
st.write("We’ve analysed your mobile usage for the past month. Here’s what we found:")

# Simulated usage inputs
data_used = st.slider("Monthly Data Used (GB)", 0.0, 100.0, 4.5)
calls_made = st.slider("Call Minutes Used", 0, 1000, 150)
texts_sent = st.slider("Texts Sent", 0, 1000, 200)

# AI logic (simple threshold-based mock)
if data_used < 6:
    recommendation = plans[0]
elif data_used < 30:
    recommendation = plans[1]
else:
    recommendation = plans[2]

st.markdown("---")
st.subheader("📢 AI-Powered Recommendation")

st.success(f"**We recommend:** {recommendation['name']}")
st.info(recommendation['recommendation_reason'])

# Display comparison table
st.markdown("### 📊 Plan Comparison")
df = pd.DataFrame(plans)
df_display = df.rename(columns={
    "name": "Plan",
    "data_limit": "Data (GB)",
    "price": "Monthly Cost ($)",
    "recommendation_reason": "Why choose this plan"
})
st.dataframe(df_display, use_container_width=True)
