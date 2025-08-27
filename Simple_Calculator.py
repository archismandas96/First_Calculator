#Simple Calculator
import streamlit as st
st.title("Simple Calculator")
num1= st.number_input("Enter first number")
num2= st.number_input("Enter second number")
operation= st.radio("Operation:",["Add","Substract"])
if st.button("Calculate"):
    if operation=="Add":
        st.write("Result",num1+num2)
    else:
        st.write("Result",num1-num2)    