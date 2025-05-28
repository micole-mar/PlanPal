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

# ---------------------- AI Logic (Dynamic Scoring) ----------------------
def calculate_score(plan, data_used):
    if data_used <= plan["data_limit"]:
        # The closer the usage is to the plan limit (without going over), the better
        score = 1 - abs(data_used - plan["data_limit"]) / plan["data_limit"]
    else:
        # Penalize plans that are under-provisioned
        score = 0.2 * plan["data_limit"] / data_used
    return round(score, 2)

for plan in plans:
    plan["score"] = calculate_score(plan, data_used)

best_plan = max(plans, key=lambda x: x["score"])
second_best = sorted(plans, key=lambda x: x["score"], reverse=True)[1]

# ---------------------- Output Recommendation ----------------------
st.markdown("---")
st.subheader("📢 AI-Powered Recommendation")
st.success(f"**Top Recommendation:** {best_plan['name']} ({int(best_plan['score'] * 100)}% match)")
st.info(best_plan["recommendation_reason"])

# ---------------------- Explainable AI ----------------------
st.markdown("### 🤖 Why this plan?")
st.write(f"""
Your recent data usage of **{data_used}GB**, combined with {calls_made} call minutes and {texts_sent} texts, places you in a **custom usage segment**.

Based on your pattern, the AI suggests **{best_plan['name']}** as it balances cost and flexibility.
""")

# ---------------------- Secondary Option ----------------------
with st.expander("🤖 See other strong options"):
    st.write(f"**Next Best Plan:** {second_best['name']} ({int(second_best['score'] * 100)}% match)")
    st.write(second_best['recommendation_reason'])

# ---------------------- Data Table ----------------------
st.markdown("### 📊 Plan Comparison")
df = pd.DataFrame(plans)
df_display = df.rename(columns={
    "name": "Plan",
    "data_limit": "Data (GB)",
    "price": "Monthly Cost ($)",
    "recommendation_reason": "Why choose this plan",
    "score": "AI Match Score"
})
st.dataframe(df_display[["Plan", "Data (GB)", "Monthly Cost ($)", "AI Match Score", "Why choose this plan"]],
             use_container_width=True)
