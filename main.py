import streamlit as st 
import pandas as pd 

st.title("Welcome to my first Web-application")
st.subheader("landscape to learning and experimenting python")

st.code(""" 
        I can show my code here 
        i can copy code directly from here 
        """)

st.header("Form")
name = st.text_input("Enter your first name: ")
surname = st.text_input("Enter your last name: ")
select_class = st.selectbox("select your class: ",(1,2,3,4,5))
address= st.text_area("Enter your address in detail: ")


st.header("dataset")
st.subheader("Transactions")
dataset= pd.read_csv("transactions.csv")
st.dataframe(dataset)