import streamlit as st

# Page Title
st.title("Simple Calculator App")

# Description
st.write("Perform basic arithmetic operations")

# Input Numbers
num1 = st.number_input("Enter First Number", value=0.0)
num2 = st.number_input("Enter Second Number", value=0.0)

# Operation Selection
operation = st.selectbox(
    "Select Operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

# Calculate Button
if st.button("Calculate"):

    if operation == "Addition":
        result = num1 + num2
        st.success(f"Result: {result}")

    elif operation == "Subtraction":
        result = num1 - num2
        st.success(f"Result: {result}")

    elif operation == "Multiplication":
        result = num1 * num2
        st.success(f"Result: {result}")

    elif operation == "Division":

        if num2 == 0:
            st.error("Cannot divide by zero")
        else:
            result = num1 / num2
            st.success(f"Result: {result}")