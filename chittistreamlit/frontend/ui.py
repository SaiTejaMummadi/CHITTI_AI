import streamlit as st
from backend.auth import authenticate_user
from backend.signup import signup_user

def login_ui():
    st.header("Login")

    # Input fields for login
    username = st.text_input("Username", key="login_username")
    password = st.text_input("Password", type="password", key="login_password")
    
    if st.button("Login"):
        # Authenticate user
        if authenticate_user(username, password):
            st.success("Login successful!")
            return True
        else:
            st.error("Invalid username or password.")
            return False

    if st.button("Go to Signup"):
        st.session_state['signup_mode'] = True

    return False

def signup_ui():
    st.header("Signup")

    # Input fields for signup
    username = st.text_input("Username", key="signup_username")
    email = st.text_input("Email", key="signup_email")
    password = st.text_input("Password", type="password", key="signup_password")
    confirm_password = st.text_input("Confirm Password", type="password", key="signup_confirm_password")
    
    if st.button("Create Account"):
        # Check if passwords match
        if password != confirm_password:
            st.error("Passwords do not match.")
            return False

        # Create user account
        signup_success = signup_user(username, email, password)
        if signup_success:
            return True
        else:
            st.error("Signup failed. Username or email might already exist.")
            return False

    if st.button("Go to Login"):
        st.session_state['signup_mode'] = False

    return False
