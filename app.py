import streamlit as st
import pandas as pd

# ---------------------- Plan Database ----------------------
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

confidence_scores = {
    "$20 Carryover Plan": 0.75,
    "$25 Carryover Plan": 0.90,
    "$32.50 Carryover Plan": 0.60
}

# ---------------------- Streamlit Setup ----------------------
st.set_page_config(page_title="PlanPal AI Assistant", page_icon="📱", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stButton>button { color: white; background-color: #0074c2; }
    .st-chat-message { background-color: #E6F4FB; border-radius: 10px; padding: 10px; }
    </style>
""", unsafe_allow_html=True)

# ---------------------- Header ----------------------
st.title("📱 PlanPal AI Assistant")
st.subheader("Kia ora, Micole 👋")
st.write("We’ve analysed your mobile usage for the past month. Here’s what we found:")

# ---------------------- Input Sliders ----------------------
data_used = st.slider("Monthly Data Used (GB)", 0.0, 100.0, 4.5)
calls_made = st.slider("Call Minutes Used", 0, 1000, 150)
texts_sent = st.slider("Texts Sent", 0, 1000, 200)

# ---------------------- AI Model Logic ----------------------
if data_used < 6:
    recommendation = plans[0]
elif data_used < 30:
    recommendation = plans[1]
else:
    recommendation = plans[2]

sorted_plans = sorted(plans, key=lambda p: confidence_scores[p["name"]], reverse=True)
top = sorted_plans[0]
second = sorted_plans[1]

# ---------------------- Recommendation Output ----------------------
st.markdown("---")
st.subheader("📢 AI-Powered Recommendation")
st.success(f"**Top Recommendation:** {top['name']} ({int(confidence_scores[top['name']] * 100)}% match)")
st.info(top['recommendation_reason'])

# ---------------------- Explainable AI ----------------------
st.markdown("### 🤖 Why this plan?")
st.write(f"""
Your recent data usage of **{data_used}GB**, combined with {calls_made} call minutes and {texts_sent} texts, places you in a **moderate usage cluster**.

Based on your pattern, the AI suggests **{top['name']}** as it balances cost and flexibility. Daily Free Data Hour and carryover features align well with your habits.
""")

# ---------------------- Secondary Option ----------------------
with st.expander("🤖 See other strong options"):
    st.write(f"**Next Best Plan:** {second['name']} ({int(confidence_scores[second['name']] * 100)}% match)")
    st.write(second['recommendation_reason'])

# ---------------------- Data Table ----------------------
st.markdown("### 📊 Plan Comparison")
df = pd.DataFrame(plans)
df_display = df.rename(columns={
    "name": "Plan",
    "data_limit": "Data (GB)",
    "price": "Monthly Cost ($)",
    "recommendation_reason": "Why choose this plan"
})
st.dataframe(df_display, use_container_width=True)

# ---------------------- Retrain Option ----------------------
if st.button("🔀 Retrain AI on new data"):
    st.info("Model retrained! Recalculating recommendations... (simulated)")
