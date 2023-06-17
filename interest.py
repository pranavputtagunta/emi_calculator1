import streamlit as st

def calculate_emi(p, n, r):
	emi = p*(r/100)*((1+(r/100))**n)/((1+r/100)**n-1)
	return emi

st.title("EMI Calculator")

n = st.slider("Choose the value of n: ", 5, 10)
r = st.slider("Choose the value of r: ", 0.01, 0.5)
p = st.slider("Choose the value of p: ", 1, 10000)

st.write("The emi is", calculate_emi(p, n, r))