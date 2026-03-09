import streamlit as st
import pandas as pd
from fraud_detector import detect_fraud
from graph_visualizer import draw_graph

st.title("AI Fund Tracking for Fraud Detection")

df = pd.read_csv("transactions.csv")

st.subheader("Transaction Data")
st.write(df)

if st.button("Detect Fraud"):

    suspicious = detect_fraud(df)

    st.subheader("Suspicious Transactions")
    st.write(suspicious)

if st.button("Show Fund Flow Graph"):
    draw_graph(df)
