#Simple Calculator
import streamlit as st
st.title("Calculator")
num1= st.number_input("Enter the first number")
num2= st.number_input("Enter the second number")

selection = st.selectbox("Select",["Add","Substract","Multiplication","Division"])
result = None
if st.button("Submit"):
    if selection =="Add":
        result = num1 + num2
    elif selection =="Substract":
        result = num1 - num2
    elif selection =="Multiplication":
        result = num1 * num2
    elif selection =="Division":
        result = num1/num2
    else:
        result = None
        
if result:
    st.success(f"Result is:  {result}" )   
