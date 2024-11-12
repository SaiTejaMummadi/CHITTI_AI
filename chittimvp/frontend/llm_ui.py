import streamlit as st
from backend.processor import get_response

def llm_input_ui():
    st.header("LLM Interaction")

    # User selects a model
    model_choice = st.selectbox("Choose a model", ["gpt-4o-mini", "Anthropic", "LLaMA - with Groq", "Mistral"])

    # Text input for LLM query
    user_query = st.text_area("Enter your question:")

    if st.button("Get Response"):
        # Call backend to get LLM response
        if user_query.strip() != "":
            response = get_response(user_query, model_choice)
            st.write("LLM Response:")
            st.write(response)
        else:
            st.warning("Please enter a valid query.")
