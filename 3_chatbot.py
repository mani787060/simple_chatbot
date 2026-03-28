"""import streamlit as st
import os  
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
 
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

while True:
    user_input = input("You:")
    chat_history.append(user_input)
 
    #small safety fix so that if you type "EXIT" or "Exit", it still knows to close.
    if user_input.lower() == 'exit':      
        break
    
    result = model.invoke(chat_history)
    chat_history.append(result.content)
    
    print("AI: ", result.content)

"""


import os  
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import time # Added for wait time

load_dotenv()

# We use the stable model for your environment
# model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")
model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite-preview")

# we have to add also 'chat_history' so that it can easily remember our previous work 

chat_history=[]

print("--- Chatbot Started ---")

while True:
    user_input = input("\nYou: ")
    chat_history.append(user_input)

    if user_input.lower() == 'exit': break
    
    # Try the request up to 3 times if we hit a rate limit
    for attempt in range(3):
        try:
            print("AI: ", end="", flush=True)
            # Using stream to make it feel fast
            for chunk in model.stream(user_input):
                # Clean up the Gemini 3 list format
                if isinstance(chunk.content, list):
                    content = "".join([part['text'] for part in chunk.content if 'text' in part])
                else:
                    content = chunk.content
                print(content, end="", flush=True)
            
            print() # New line when finished
            break # Success! Exit the retry loop
            
        except Exception as e:
            if "429" in str(e):
                print(f"\n[Busy] Google is throttling the free tier. Retrying in 10s...")
                time.sleep(10)
                continue # Try the loop again
            else:
                print(f"\nAI Error: {e}")
                break