import streamlit as st

# Add a proper title
st.title("Welcome App")

st.subheader("my first app")

# Use st.text_input directly (do not use input())
name = st.text_input("Enter your name:")

# Check if a name has been entered before displaying the welcome message
if name:
    # Use st.write or st.text to display output (do not use print())
    st.write(f"Welcome, {name}!")