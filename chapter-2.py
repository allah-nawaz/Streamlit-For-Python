import streamlit as st
st.title("Chai Maker app")


tea_type = st.radio("Choose your tea base:", ["Milk", "Water"])
st.write(f"You selected {tea_type} as your tea base.")


Elachi = st.checkbox("Do you want Elachi in your chai?")
Adrak  = st.checkbox("Do you want Adrak in your chai?")
if Elachi:
    st.info("Elachi has been added to your chai.")
if Adrak:
    st.info("Adrak has been added to your chai.")
if Elachi and Adrak:
    st.info("Your chai has both Elachi and Adrak. Enjoy Your chai!")


flavor = st.selectbox("Choose your flavor:", ["Masala", "Ginger", "Cardamom"])
st.write(f"Your selected flavor is {flavor}")


sugar = st.slider("Select sugar spoon:", 0, 5, 1)
st.write(f"Your selected sugar spoon is {sugar}")


cups = st.number_input("How many cups you want to order?", min_value=1, max_value=10, step=1)
st.write(f"You ordered {cups} cups of chai.")

name = st.text_input("Enter you name:")
if name:
    st.write(f"Hello {name}! Your chai is on the way.")


DOB = st.date_input("Enter you date of birth:")
st.write(f"Your date of birth is {DOB}")


if st.button("Make Chai"):
    st.success("Your chai has been brewed")
