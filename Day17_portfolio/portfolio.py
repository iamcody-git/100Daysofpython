import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("./Images\seen.jpg", width=200)

with col2:
    st.title("Prashant Adhikari:CODY")
    content = """
    Hi, I am cody. I am web developer.
    """
    st.info(content)

content2 = """ 
Below you can find some of my project. I have built project in different language. okay!!
"""

st.info(content2)


cols3,cols4 = st.columns(2)

df = pandas.read_csv("portfolio dataset.csv", sep=";")

with cols3:
    for index,row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("Images/" + row["image"])
        st.write("[Source code]({row['url']})")

with cols4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("Images/" + row["image"])
        st.write("[Source Code]({row['url']})")