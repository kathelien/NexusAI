import streamlit as st

st.set_page_config(
    page_title="NexusAI",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 NexusAI")
st.subheader("AI-Driven Multi-Domain Analytics Platform")

st.success("NexusAI Website Created Successfully!")

st.write("Welcome to NexusAI Dashboard")

st.metric("Total Domains", 6)

st.markdown("### Our Six Domains")

col1, col2, col3 = st.columns(3)

col1.info("🛡️ Cybersecurity")
col2.info("🏥 Healthcare")
col3.info("🌱 Agriculture")

col4, col5, col6 = st.columns(3)

col4.info("💳 Finance")
col5.info("🏙️ Smart City")
col6.info("📊 Business Analytics")
