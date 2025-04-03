
import streamlit as st
import joblib

clf=joblib.load('C:/Users/KAVYA/OneDrive/New folder/likitha/loan.joblib')
st.title('LOAN APP')
g=st.number_input('Enter Gender 0:Male 1:Female')
m=st.number_input('Enter Maritial status 0:No 1:Yes')
ai=st.number_input('Enter Application Income in thousands')
la=st.number_input('Enter loan amount in thousands')
if st.button('PREDICT'):
    prediction=clf.predict([[g,m,ai,la]])
    if prediction=='Y':
        St.text('LOAN IS APPOVED')
    else:
        st.text('LOAN IS REJECTED')
        
