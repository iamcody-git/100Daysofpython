
import streamlit as st
from send_email import send_mail

st.header("Contact Me")

with st.form(key="form"):
    user_email = st.text_input("Your email address: ")
    user_msg = st.text_area("Enter your message:")
    msg_text = f"""
    
    Subject: New mail from {user_email}
    
    From:{user_email}
            {user_msg}
    """
    button = st.form_submit_button("Submit")
    
    if button:
        send_mail(msg_text)
        st.info("Mail is send successfully.")