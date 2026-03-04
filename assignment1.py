import streamlit as st

st.title("Choose Programming language")

Language = st.selectbox("Choose a programming language:",
                         ["Python", "Java", "JavaScript", "C++"])

st.success(f"You have selected: {Language} Good choice!!")

if Language == "Python":
    st.info("Python is a great choice for beginners and experienced developers alike!")
elif Language == "Java":
    st.info("Java is a robust and widely used programming language, especially in enterprise applications.")
elif Language == "JavaScript":
    st.info("JavaScript is essential for web development and allows you to create interactive websites.")
elif Language == "C++":
    st.info("C++ is a powerful language often used for system/software development and game programming.")