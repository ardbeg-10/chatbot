import pandas as pd
import openai
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

# Load the CSV file
df = pd.read_csv('topics.csv')

# Initialize the OpenAI model
llm = OpenAI()

SYSTEM_MSG = """        
Please tag the text with the topic it is disscussing. 
Choose only one topic. If it does not match with any of the topics, return empty. 
"""


def summarize_topic(text):
    """
    Conclude the text in a phrase.
    """
    try:
        response = openai.ChatCompletion.create(
            
            api_key = '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',
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": SYSTEM_MSG}, 
            {"role": "user", "content": text}]
        )
        return response.choices[0].message["content"] 
    except Exception as e:
        return f"Error in summarization: {e}"

def summarize(text):
    """
    Conclude the text in a phrase.
    """
    try:
        response = openai.ChatCompletion.create(
            api_key = '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',
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "summarize the text."},
                      {"role": "user", "content": text}]
        )
        return response.choices[0].message["content"] 
    except Exception as e:
        return f"Error in summarization: {e}"

# Apply summarization to the 'Text' column
df['Summary'] = df['Text'].apply(summarize)

# Save the results back to CSV
df.to_csv('topics1.csv', index=False)

