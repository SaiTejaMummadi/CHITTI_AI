from utils.llm_utils import get_response_from_llm

def get_response(user_query, model_choice):
    # Call the utility function to get the response from the LLM
    return get_response_from_llm(user_query, model_choice)
