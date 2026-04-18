import streamlit as st

st.title("Finance Analyzer Dashboard")

uploaded_file = st.file_uploader("Choose a file", type=["csv"])

if uploaded_file:
    st.subheader("Raw Data")
    st.subheader("Total Spending")
    st.subheader("Average Spending")
    st.subheader("Category Analysis")
    st.subheader("Monthly Trend")
    st.subheader("Heatmap")