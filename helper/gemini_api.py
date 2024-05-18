import os
import pathlib
import textwrap
import google.generativeai as genai
import time

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Configure API key
os.environ['GOOGLE_API_KEY'] = " "

genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

def text_completion(prompt):
    '''
    Call Gemini API for text completion

    Parameters:
        - prompt: user query (str)

    Returns:
        - dict with status and response
    '''
    try:
        print("Calling Gemini API...")
        models = [m for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        if not models:
            raise Exception("No models support the 'generateContent' method")
        model = genai.GenerativeModel('gemini-pro')
        business_details = input("Enter your Business or Shop details: ")
        response = model.generate_content("Here is Business Information"+ business_details + ",Now answer this Query based on the information provided make sure you answer based on this information and not your own " + prompt + "Be confident while answering not clueless")
        print("API call successful.")
        # Extracting the text content from the response
        text = response.candidates[0].content.parts[0].text

        return {
            'status': 1,
            'response': text
        }
    except Exception as e:
        print("API call failed with error:", e)
        return {
            'status': 0,
            'response': str(e)
        }