"""
=======================================
 Simple Chatbot (Day-14 Project)
---------------------------------------
 Author: AASHISH KUMAR PRAJAPATI 
 Goal  : Beginner-level chatbot project
=======================================

Concepts used:
- Python basics (loops, conditions, functions)
- Reading API key from environment
- Using OpenAI API (Chat Completions)
- Very simple conversation loop 

"""

import os
from openai import OpenAI   # Official OpenAI Python library

# --------------------------------------------------
# Step 1: API Key Setup
# -------------------------------------------------- 

# Make sure to set your API key before running:
# Windows PowerShell (temporary): $env:OPENAI_API_KEY="your-key"
# Windows Persistent (User scope):
#   [System.Environment]::SetEnvironmentVariable("OPENAI_API_KEY","your-key","User")
# After setting, open a NEW terminal.

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("🚫 API key not found. Please set OPENAI_API_KEY as an environment variable.")

# Create OpenAI client
client = OpenAI()

# --------------------------------------------------
# Step 2: Chat Loop
# -------------------------------------------------- 

print("🤖 Chatbot is ready! (type 'bye' to exit)\n")

while True:
    # Takes input from user : 
    user_text = input("You: ")

    # Exit condition :
    if user_text.lower() in ["bye", "exit", "quit"]:
        print("Bot: Okay, bye 👋👋 !! Talk to you later.")
        break

    # Sends user's input to OpenAI : 
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",   # beginner-friendly, fast model
        messages=[
            {"role": "system", "content": "You are a friendly chatbot."},  # simple personality
            {"role": "user", "content": user_text}
        ],
        max_tokens=150,
        temperature=0.7
    )

    # Extract and print bot reply
    bot_reply = response.choices[0].message.content.strip()
    print("Bot:", bot_reply, "\n")
