import streamlit as st
from datetime import date

# Title
st.title("Calculator App")

# Subheader
st.subheader("Basic Calculator and Age Calculator")

# User can select which calculator they want to use
option = st.radio("Choose calculator you want to use:", ["Basic Calculator", "Age Calculator"])

# Basic Calculator
if option == "Basic Calculator":

    st.subheader("Basic Calculator")

    num1 = st.number_input("Enter First Number", value=1)
    num2 = st.number_input("Enter Second Number", value=1)

    operation = st.selectbox("Select Operation",
                             ["Addition", "Subtraction", "Multiplication", "Division"])

    show_details = st.checkbox("Show Calculation Details")

    if st.button("Calculate"):

        if operation == "Addition":
            result = num1 + num2

        elif operation == "Subtraction":
            result = num1 - num2

        elif operation == "Multiplication":
            result = num1 * num2

        elif operation == "Division":
            if num2 != 0:
                result = num1 / num2
            else:
                st.warning("Cannot divide by zero!")
                
        if result is not None:
            st.success(f"Result is: {result}")

    if show_details:
            st.write("You selected:", operation)
            st.write("First number:", num1)
            st.write("Second number:", num2)


# Age calculator
elif option == "Age Calculator":

    st.subheader("Age Calculator")

    # Fixed year range(2001–2030)
    dob = st.date_input(
        "Select your Date of Birth",
        min_value=date(2001, 1, 1),
        max_value=date(2030, 12, 31)
    )

    today = date.today()

    if st.button("Calculate Age"):

        age = today.year - dob.year
        st.success(f"You are {age} years old.")

        st.write("Your Birth Year is:", dob.year)
        st.write("Current Year is:", today.year)