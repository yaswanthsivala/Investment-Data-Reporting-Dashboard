import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Investment Reporting Dashboard", layout="wide")

# Load data
df = pd.read_csv("data/processed/consolidated_report.csv")

# Title
st.title("📊 Investment Data Reporting Dashboard")

st.markdown("""
This dashboard provides an executive-level overview of portfolio performance,
asset allocation, and compliance status to support investment decision-making.
""")

# Sidebar filters
st.sidebar.header("Filters")
asset_filter = st.sidebar.multiselect(
    "Select Asset Class",
    options=df["asset_class"].unique(),
    default=df["asset_class"].unique()
)

df_filtered = df[df["asset_class"].isin(asset_filter)]

# KPI Section
st.subheader("Key Portfolio Metrics")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Portfolio Value", f"${df_filtered['market_value'].sum():,.0f}")

with col2:
    st.metric("Number of Holdings", df_filtered.shape[0])

with col3:
    compliant_value = df_filtered[df_filtered["compliance_status_standardized"] == "Compliant"]["market_value"].sum()
    st.metric("Compliant Exposure", f"${compliant_value:,.0f}")

# Asset Allocation Chart
st.subheader("Asset Allocation")
asset_data = df_filtered.groupby("asset_class")["market_value"].sum()

fig1, ax1 = plt.subplots()
ax1.pie(asset_data, labels=asset_data.index, autopct="%1.1f%%", startangle=90)
ax1.axis("equal")
st.pyplot(fig1)

# Compliance Chart
st.subheader("Compliance Status")
compliance_data = df_filtered.groupby("compliance_status_standardized")["market_value"].sum()

fig2, ax2 = plt.subplots()
ax2.bar(compliance_data.index, compliance_data.values)
ax2.set_ylabel("Market Value")
st.pyplot(fig2)

# Data Table
st.subheader("Detailed Portfolio Data")
st.dataframe(df_filtered)
