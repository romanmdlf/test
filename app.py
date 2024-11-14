import os
import json
import requests
import time
import streamlit as st
from openai import AzureOpenAI
from dotenv import load_dotenv
import numpy as np
import pandas as pd
import GradS

client_df=pd.read_csv("client_info.csv")

st.title("GRADient Ascent")
st.subheader("Enter your Client Details")

with st.form(key='customer_form'):
    client_id=st.number_input("Enter Client Id")
    submit_button=st.form_submit_button(label='Submit')
    new_customer_button=st.form_submit_button(label="I am a new customer")

if new_customer_button:
    new_client_id = len(client_df)+1
    with st.form(key='new_customer_form'):
        new_name = st.text_input("Enter Client Name")
        new_dob = st.text_input("Enter Clint DOB (MM/DD/YYYY)")
        new_incomeytd = st.number_input("Enter annual salary")
        new_account_balance = st.number_input("Enter Account Balance")
        new_account_type = st.selectbox("Select account type",("Savings", "Checking", "Investment", "Mortgage"))
        new_employment_status = st.selectbox("Select employment status",("Retired", "Employed", "Self-Employed", "Student"))
        new_address = st.text_input("Enter Client address")
        new_email = st.text_input("Enter Client email address")
        new_phone_number = st.number_input("Enter Client phone number")
        new_credit_score = st.number_input("Enter Client credit score")

        new_customer_submit_button=st.form_submit_button("Submit")

    if new_customer_submit_button:
        
        new_client = pd.DataFrame({
            'clientid': [new_client_id],
            'name': [new_name],
            'dob': [new_dob],
            'incomeytd': [new_incomeytd],
            'account_balance': [new_account_balance],
            'account_type': [new_account_type],
            'employment_status': [new_employment_status],
            'address': [new_address],
            'email': [new_email],
            'phone_number': [new_phone_number],
            'credit_score': [new_credit_score]
        })
        client_df = pd.concat([client_df, new_client], ignore_index=True)
        # print(len(client_df))
        # print(client_df)

        st.write("Customer data successfully registered")

if submit_button:
    if client_id in client_df['clientid'].values:
        
        st.write("Client Id successfully found")
        st.header("Client Overview")

        st.subheader("Product Recommendations")
        product_recommendations = GradS.user_input_response(client_id, 1, "potential products")
        st.write(product_recommendations)

        st.subheader("Client Product Holdings")
        client_product_holdings = GradS.user_input_response(client_id, 3, "id, date, client product holdings")
        st.write(client_product_holdings)

        st.subheader("Transactional Activity")
        transactional_history = GradS.user_input_response(client_id, 5, "id, date, category, transaction amount, transactional activity")
        st.write(transactional_history)

        st.subheader("Historical Product Use")
        historical_product_use = GradS.user_input_response(client_id, 2, "time used, historical products")
        st.write(historical_product_use)

    else:
        st.write("Client Id not found, please re-enter Client Id")