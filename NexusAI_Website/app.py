
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="NexusAI Dashboard",
    page_icon="🧠",
    layout="wide"
)

BASE_DIR = Path(__file__).parent

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_csv(filename):
    path = BASE_DIR / filename
    if path.exists():
        return pd.read_csv(path)
    return pd.DataFrame()

cyber = load_csv("cybersecurity.csv")
health = load_csv("healthcare.csv")
agri = load_csv("agriculture.csv")
finance = load_csv("finance.csv")
city = load_csv("smart_city.csv")
business = load_csv("business.csv")

data = {
    "Cybersecurity": cyber,
    "Healthcare": health,
    "Agriculture": agri,
    "Finance": finance,
    "Smart City": city,
    "Business Analytics": business
}

# ---------------- SIDEBAR ----------------
st.sidebar.title("🧠 NexusAI")
st.sidebar.caption("AI-Driven Analytics Platform")

page = st.sidebar.radio(
    "NAVIGATION",
    [
        "Overview",
        "Cybersecurity",
        "Healthcare",
        "Agriculture",
        "Finance",
        "Smart City",
        "Business Analytics",
        "Security Demo"
    ]
)

st.sidebar.divider()
st.sidebar.success("6 Domains Connected")
st.sidebar.caption("Academic Demonstration")

# ---------------- HEADER ----------------
st.title("🧠 NexusAI")
st.caption("Integrated AI-Driven Multi-Domain Analytics Platform")

# ---------------- OVERVIEW ----------------
if page == "Overview":
    st.subheader("Platform Overview")

    total_records = sum(len(df) for df in data.values())

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Domains", "6")
    c2.metric("Total Records", f"{total_records:,}")
    c3.metric("AI Analysis", "2 Domains")
    c4.metric("Platform Status", "Active")

    st.info(
        "NexusAI combines data analytics, AI anomaly detection "
        "and privacy demonstrations across six domains."
    )

    summary = pd.DataFrame({
        "Domain": list(data.keys()),
        "Records": [len(df) for df in data.values()]
    })

    left, right = st.columns(2)

    with left:
        st.markdown("### Dataset Overview")
        fig = px.bar(
            summary,
            x="Domain",
            y="Records",
            color="Domain",
            title="Records Across Six Domains"
        )
        st.plotly_chart(fig, use_container_width=True)

    with right:
        st.markdown("### Project Modules")
        st.markdown("""
        **1. Data Engineering**
        
        Six datasets loaded from CSV files.

        **2. AI Engineering**
        
        Anomaly detection results from the notebook.

        **3. Security Engineering**
        
        Data masking and a role-selection demonstration.

        **4. Cloud Engineering**
        
        Web application deployment using Streamlit Cloud.
        """)

    st.markdown("### Domain Summary")
    st.dataframe(summary, use_container_width=True, hide_index=True)

# ---------------- CYBERSECURITY ----------------
elif page == "Cybersecurity":
    st.subheader("🛡️ Cybersecurity Analytics")

    if not cyber.empty:
        if "AI_Result" in cyber.columns:
            counts = cyber["AI_Result"].value_counts().reset_index()
            counts.columns = ["Result", "Count"]
            st.plotly_chart(
                px.pie(counts, names="Result", values="Count",
                       title="AI Anomaly Detection Results"),
                use_container_width=True
            )

        if "Suspicious_Activity" in cyber.columns:
            counts = cyber["Suspicious_Activity"].value_counts().reset_index()
            counts.columns = ["Activity", "Count"]
            st.plotly_chart(
                px.bar(counts, x="Activity", y="Count",
                       title="Suspicious Activity Summary"),
                use_container_width=True
            )

        if {"Failed_Logins", "Network_Traffic_MB"}.issubset(cyber.columns):
            color_col = "AI_Result" if "AI_Result" in cyber.columns else None
            fig = px.scatter(
                cyber,
                x="Failed_Logins",
                y="Network_Traffic_MB",
                color=color_col,
                title="Failed Logins vs Network Traffic"
            )
            st.plotly_chart(fig, use_container_width=True)

        st.markdown("### Cybersecurity Records")
        st.dataframe(cyber, use_container_width=True)
    else:
        st.warning("Cybersecurity CSV not found.")

# ---------------- HEALTHCARE ----------------
elif page == "Healthcare":
    st.subheader("🏥 Healthcare Analytics")

    if not health.empty:
        a, b, c = st.columns(3)

        if "Patients" in health.columns:
            a.metric("Total Patients", f"{health['Patients'].sum():,}")

        if "Beds_Available" in health.columns:
            b.metric("Available Beds", f"{health['Beds_Available'].sum():,}")

        if "Hospital_ID" in health.columns:
            c.metric("Hospital Records", health["Hospital_ID"].nunique())

        if {"Hospital_ID", "Patients", "Beds_Available"}.issubset(health.columns):
            fig = px.bar(
                health,
                x="Hospital_ID",
                y=["Patients", "Beds_Available"],
                barmode="group",
                title="Patients and Available Beds"
            )
            st.plotly_chart(fig, use_container_width=True)

        st.dataframe(health, use_container_width=True)
    else:
        st.warning("Healthcare CSV not found.")

# ---------------- AGRICULTURE ----------------
elif page == "Agriculture":
    st.subheader("🌱 Agriculture Analytics")

    if not agri.empty:
        if {"Crop", "Soil_Moisture"}.issubset(agri.columns):
            crop_data = agri.groupby("Crop", as_index=False)["Soil_Moisture"].mean()
            fig = px.bar(
                crop_data,
                x="Crop",
                y="Soil_Moisture",
                color="Crop",
                title="Average Soil Moisture by Crop"
            )
            st.plotly_chart(fig, use_container_width=True)

        if {"Farm_ID", "Temperature_C"}.issubset(agri.columns):
            fig = px.line(
                agri,
                x="Farm_ID",
                y="Temperature_C",
                title="Farm Temperature Analysis"
            )
            st.plotly_chart(fig, use_container_width=True)

        if {"Farm_ID", "Rainfall_mm"}.issubset(agri.columns):
            fig = px.bar(
                agri,
                x="Farm_ID",
                y="Rainfall_mm",
                title="Rainfall by Farm"
            )
            st.plotly_chart(fig, use_container_width=True)

        st.dataframe(agri, use_container_width=True)
    else:
        st.warning("Agriculture CSV not found.")

# ---------------- FINANCE ----------------
elif page == "Finance":
    st.subheader("💳 Finance Analytics")

    if not finance.empty:
        a, b = st.columns(2)

        if "Amount" in finance.columns:
            a.metric("Total Transaction Amount",
                     f"{finance['Amount'].sum():,.2f}")

        if "AI_Result" in finance.columns:
            unusual = (finance["AI_Result"] == "Unusual").sum()
            b.metric("AI-Flagged Records", int(unusual))

            counts = finance["AI_Result"].value_counts().reset_index()
            counts.columns = ["Result", "Count"]
            st.plotly_chart(
                px.pie(counts, names="Result", values="Count",
                       title="AI Transaction Anomaly Results"),
                use_container_width=True
            )

        if {"Transaction_Type", "Amount"}.issubset(finance.columns):
            amounts = finance.groupby(
                "Transaction_Type", as_index=False
            )["Amount"].mean()

            st.plotly_chart(
                px.bar(amounts, x="Transaction_Type", y="Amount",
                       title="Average Transaction Amount"),
                use_container_width=True
            )

        st.dataframe(finance, use_container_width=True)
    else:
        st.warning("Finance CSV not found.")

# ---------------- SMART CITY ----------------
elif page == "Smart City":
    st.subheader("🏙️ Smart City Analytics")

    if not city.empty:
        a, b = st.columns(2)

        if "Traffic_Vehicles" in city.columns:
            a.metric("Total Traffic Count",
                     f"{city['Traffic_Vehicles'].sum():,}")

        if "Air_Quality_Index" in city.columns:
            b.metric("Average Air Quality Index",
                     f"{city['Air_Quality_Index'].mean():.1f}")

        if {"Traffic_Vehicles", "Air_Quality_Index"}.issubset(city.columns):
            st.plotly_chart(
                px.scatter(
                    city,
                    x="Traffic_Vehicles",
                    y="Air_Quality_Index",
                    title="Traffic vs Air Quality"
                ),
                use_container_width=True
            )

        if "Water_Usage_Liters" in city.columns:
            st.plotly_chart(
                px.histogram(
                    city,
                    x="Water_Usage_Liters",
                    title="Water Usage Distribution"
                ),
                use_container_width=True
            )

        st.dataframe(city, use_container_width=True)
    else:
        st.warning("Smart City CSV not found.")

# ---------------- BUSINESS ANALYTICS ----------------
elif page == "Business Analytics":
    st.subheader("📊 Business Analytics")

    if not business.empty:
        a, b = st.columns(2)

        if "Sales" in business.columns:
            a.metric("Total Sales", f"{business['Sales'].sum():,.2f}")

        if "Profit" in business.columns:
            b.metric("Total Profit", f"{business['Profit'].sum():,.2f}")

        if {"Region", "Sales"}.issubset(business.columns):
            sales = business.groupby("Region", as_index=False)["Sales"].sum()
            st.plotly_chart(
                px.bar(sales, x="Region", y="Sales",
                       color="Region", title="Sales by Region"),
                use_container_width=True
            )

        if {"Region", "Profit"}.issubset(business.columns):
            profits = business.groupby("Region", as_index=False)["Profit"].sum()
            st.plotly_chart(
                px.bar(profits, x="Region", y="Profit",
                       title="Profit by Region"),
                use_container_width=True
            )

        st.dataframe(business, use_container_width=True)
    else:
        st.warning("Business Analytics CSV not found.")

# ---------------- SECURITY DEMO ----------------
elif page == "Security Demo":
    st.subheader("🔐 Security and Privacy Demonstration")

    st.warning(
        "Academic demo only. This page does not provide real "
        "authentication or production-grade access control."
    )

    role = st.selectbox("Select demonstration role", ["Viewer", "Admin", "Guest"])

    users = pd.DataFrame({
        "User_ID": [1, 2, 3],
        "Name": ["User A", "User B", "User C"],
        "Phone": ["9876543210", "9123456780", "9988776655"]
    })

    users["Masked_Phone"] = users["Phone"].apply(
        lambda phone: "*" * (len(phone) - 4) + phone[-4:]
    )

    if role == "Admin":
        st.success("Admin demonstration: full sample data")
        st.dataframe(
            users[["User_ID", "Name", "Phone"]],
            use_container_width=True
        )
    elif role == "Viewer":
        st.info("Viewer demonstration: masked data")
        st.dataframe(
            users[["User_ID", "Name", "Masked_Phone"]],
            use_container_width=True
        )
    else:
        st.error("Access denied in this demonstration.")

# ---------------- FOOTER ----------------
st.divider()
st.caption(
    "NexusAI | Academic Prototype | Synthetic Demo Data"
)
