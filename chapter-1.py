import streamlit as st

st.title("My streamlit app")

name = st.text_input("Enter your name")

if name:
    st.write(f"Hello, {name}!")

Chai = st.selectbox("Your favourite chai is:", ["Masala Chai", "Ginger Chai", "Cardamom Chai", "Plain Chai"])

st.write(f"You choose {Chai} as your favourite chai. Great choice!")

st.success("Your chai has been brewed")