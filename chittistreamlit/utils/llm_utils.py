# from langchain_core.messages import AIMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langchain_anthropic.chat_models import ChatAnthropic
from langchain_mistralai import ChatMistralAI
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

# Sample function to get response from LLM
def get_response_from_llm(user_query, language_choice='English', model_choice = 'gpt-4o-mini'):
    load_dotenv()

    template = """
    System: {prompt}
    User question: {user_query}
    """
    
    prompts = {
        'default': "This is a default system prompt to start the conversation.",
        'conversational': "You are an assistant helping a user with LLM queries."
    }
    
    causal_prompt = prompts['conversational']
    prompt = ChatPromptTemplate.from_template(template)

    # Select the model based on user choice
    if model_choice == "gpt-4o-mini":
        llm = ChatOpenAI(model='gpt-4o-mini')
    elif model_choice == "Anthropic":
        llm = ChatAnthropic(model="claude-3-5-sonnet-20240620")
    elif model_choice == "LLaMA - with Groq":
        llm = ChatGroq(model="llama3-8b-8192")
    elif model_choice == "Mistral":
        llm = ChatMistralAI(model="mistral-medium")

    chain = prompt | llm | StrOutputParser()

    # Get response from LLM
    return chain.invoke({
        "prompt": causal_prompt,
        "user_query": user_query,
    })
