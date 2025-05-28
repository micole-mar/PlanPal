import streamlit as st
import random

# Set page config
st.set_page_config(
    page_title="PlanPal AI Recommender",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom styling to mimic 2degrees
st.markdown("""
    <style>
        body, .stApp {
            background-color: #ffffff;
            font-family: 'Segoe UI', sans-serif;
        }
        .big-font {
            font-size: 24px;
            font-weight: 600;
            color: #0072CE;
        }
        .plan-card {
            background-color: #f1f8ff;
            padding: 1em;
            border-radius: 10px;
            margin-bottom: 1em;
            border: 1px solid #0072CE33;
        }
    </style>
""", unsafe_allow_html=True)

# Title greeting
st.markdown("<div class='big-font'>Kia ora, Micole! 👋</div>", unsafe_allow_html=True)
st.write("Let's help you find the best mobile plan for your current usage with a little help from AI ✨")

# Input section
st.subheader("📲 Your Usage Snapshot")
data_usage = st.slider("Monthly Data Usage (in GB)", 0, 100, 12)
call_minutes = st.slider("Monthly Call Minutes", 0, 1000, 250)
texts_sent = st.slider("Monthly Texts Sent", 0, 1000, 150)
roaming = st.selectbox("Are you currently roaming?", ["No", "Yes"])

# Dummy recommendation logic
def recommend_plan(data, calls, texts, roam):
    if data > 40 or calls > 800:
        return ("$65 Unlimited Plan", "You’re a power user! The Unlimited plan gives you 80GB, unlimited NZ & Aussie calls, and 5G hotspotting support.")
    elif data > 10 or calls > 300:
        return ("$50 10GB Plan", "A great balance with 10GB Carryover Data, daily Free Data Hour, and plenty of talk and text.")
    else:
        return ("$40 5GB Plan", "Perfect for light usage! 5GB Carryover Data and unlimited 2degrees calls with flexibility to grow.")

if st.button("🔍 Get My AI Recommendation"):
    plan, explanation = recommend_plan(data_usage, call_minutes, texts_sent, roaming)
    st.markdown("""
        <div style='border: 2px solid #0072CE; padding: 15px; border-radius: 10px; background-color: #e6f2ff;'>
            <strong>🤖 PlanPal AI Suggestion:</strong><br>
            <span style='font-size: 20px; color: #0072CE'><strong>{}</strong></span><br>
            {}
        </div>
    """.format(plan, explanation), unsafe_allow_html=True)

# Footer
st.write("---")
st.caption("Built for 2degrees assessment centre • Streamlit mockup by Micole")
