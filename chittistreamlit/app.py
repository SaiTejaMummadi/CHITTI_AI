import streamlit as st
from frontend.ui import login_ui, signup_ui
from frontend.llm_ui import llm_input_ui

# Main Streamlit Application
def main():
    st.title("CHITTI - General Purpose Multilingual AGENT ")
    st.header("Supports Hindi, English and Telugu")
    
    #%%%%%%%% Login Logic %%%%%%%%
    # if 'logged_in' not in st.session_state:
    #     st.session_state['logged_in'] = False
    # if 'signup_mode' not in st.session_state:
    #     st.session_state['signup_mode'] = False

    # # Display Signup or Login UI based on user's choice
    # if not st.session_state['logged_in']:
    #     if st.session_state['signup_mode']:
    #         signup_success = signup_ui()
    #         if signup_success:
    #             st.session_state['signup_mode'] = False
    #             st.success("Account created successfully. Please log in.")
    #     else:
    #         login_success = login_ui()
    #         if login_success:
    #             st.session_state['logged_in'] = True

    # # Display LLM Interaction UI if user is logged in
    # if st.session_state['logged_in']:
    
    #%%%%%%%% Login Logic End %%%%%%%%
    
    llm_input_ui()

if __name__ == "__main__":
    main()
