import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Simulated customer data
customer = {
    "Current Plan": "$20 - 5GB",
    "Data Used (GB)": 8.2,
    "Call Minutes": 312,
    "Texts Sent": 168,
    "Roaming": "No"
}



st.set_page_config(page_title="2degrees AI Recommender", layout="centered")

# Title
st.title("📱 AI-Powered Plan Recommender")

st.markdown(
    "<h1 style='color:#0078C8;'>Kia ora Micole! 👋</h1><h3>Here’s how you’ve been using your plan this month:</h3>",
    unsafe_allow_html=True
)

st.toast("📢 Based on your usage, we think you could save $15/month by switching to the $25 Carryover Plan!", icon="📱")


# Customer Profile Overview
st.subheader("Customer Usage Summary")
st.markdown(f"""
- **Current Plan**: {customer['Current Plan']}
- **Monthly Data Usage**: {customer['Data Used (GB)']} GB
- **Call Minutes**: {customer['Call Minutes']}
- **Texts Sent**: {customer['Texts Sent']}
- **Roaming**: {customer['Roaming']}
""")

# Data Usage Chart
st.subheader("📊 Data Usage vs Plan Limit")

plan_limit = 5
usage = customer['Data Used (GB)']

fig, ax = plt.subplots(figsize=(4, 1.2))
ax.barh(['Data Used'], [usage], color='skyblue', label='Used')
ax.barh(['Data Used'], [plan_limit], color='lightgrey', left=0, alpha=0.3, label='Plan Limit')
ax.set_xlim(0, max(plan_limit, usage) + 2)
ax.set_xlabel('GB')
ax.legend(loc='upper right')
ax.set_yticks([])

st.pyplot(fig)

# Buttons
col1, col2 = st.columns(2)
with col1:
    st.button("📲 Switch Now")
with col2:
    st.button("🔁 Remind Me Later")
