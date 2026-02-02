import streamlit as st
from inference.predict import predict_loan
from llm.ollama_helper import explain_decision

st.set_page_config(page_title="Bank AI Loan Assistant")

st.title("🏦 Bank Loan Approval Using AI System")

st.subheader("Enter customer details")

age = st.number_input("Age", 18, 70)
income = st.number_input("Annual Income", 10000, 500000)
credit_score = st.number_input("Credit Score", 300, 900)
loan_amount = st.number_input("Loan Amount", 1000, 500000)

if st.button("Predict Loan Decision"):
    decision = predict_loan(age, income, credit_score, loan_amount)

    st.success(f"Loan Decision: **{decision}**")

    user_text = f"""
Age: {age}
Income: {income}
Credit Score: {credit_score}
Loan Amount: {loan_amount}
"""

    with st.spinner("AI explaining decision..."):
        explanation = explain_decision(user_text, decision)

    st.subheader("🤖 AI Explanation")
    st.write(explanation)