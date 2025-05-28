import streamlit as st
import matplotlib.pyplot as plt

# Set page config
st.set_page_config(page_title="PlanPal", layout="centered")

# Header section
st.markdown(
    """
    <div style="background-color:#00ADEF;padding:20px;border-radius:10px;color:white;text-align:center;">
        <h2>Kia ora Micole!</h2>
        <p>021 XXX XXXX</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("### Your Plan Snapshot")

# Data pie chart
labels = 'Used', 'Left'
sizes = [1.89, 4.61]
colors = ['#FFB703', '#00ADEF']

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=colors, startangle=90, autopct='%1.1fGB')
ax.axis('equal')
st.pyplot(fig)

# Breakdown
st.markdown("""
**Data Breakdown:**
- 📊 Plan Data: 1.50 GB  
- 💾 Carryover: 3.11 GB  
- 🔄 30 days to renew
""")

# Usage & Balance
col1, col2 = st.columns(2)
col1.metric("Minutes", "1308", "to NZ & Aussie")
col2.metric("Texts", "Unlimited*", "to NZ & Aussie")

col1, col2 = st.columns(2)
col1.button("💸 Spend")
col2.button("🔼 Top Up")

# Plan Info
st.markdown("""
### 📄 Current Plan
**$19 Monthly Prepay Plan**
- ✅ 1.5GB Carryover Data  
- ✅ 200 Carryover mins to NZ & Aussie  
- ✅ Unlimited* texts to NZ & Aussie  
- ✅ Hotspotting included  
- ✅ 5G ready
""")

# 🔔 AI Recommendation (simulated toast)
st.toast("📢 Based on your usage, try the $13 Monthly Plan to save $6/month and still get Free Data Hour! 💡")
