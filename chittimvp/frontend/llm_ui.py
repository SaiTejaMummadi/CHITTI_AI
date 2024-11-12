import streamlit as st
from backend.processor import get_response

def llm_input_ui():
    # st.header("LLM Interaction")

    # User selects a model
    language_choice = st.selectbox("Choose your language", ["English", "Hindi", "Telugu"])
    model_choice = 'gpt-4o-mini'

    # Text input for LLM query
    user_query = st.text_area("Enter your question:")

    if st.button("Get Response"):
        # Call backend to get LLM response
        if user_query.strip() != "":
            response = get_response(user_query, language_choice,model_choice)
            st.write("LLM Response:")
            st.write(response)
        else:
            st.warning("Please enter a valid query.")
