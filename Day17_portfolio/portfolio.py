import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("./Images\seen.jpg", width=300)

with col2:
    st.title("Prashant Adhikari:CODY")
    content = """
    Hi, I am cody, I am web developer.
    """
    st.info(content)

content2 = """ 
Below tou can find some of that app. I have built in different language. okay!!
"""

st.info(content2)