import streamlit as st
from PIL import Image
import google.generativeai as genai
from collections import deque

GOOGLE_API_KEY = "AIzaSyDk0_7GU4FojcOW2Ko_Y2hh9OIK_XbE7-Y"
genai.configure(api_key=GOOGLE_API_KEY)

# Custom CSS for chat messages
def load_custom_css():
    """
    Loads custom CSS styles for the chat messages.
    Returns:
        None
    """
    
    custom_css = """
    <style>
    /* Add your custom CSS here */
    .chat-message {
        padding: 10px;
        border-radius: 25px;
    }
    .user-message {
        background-color: #0099ff;
        text-align: left;
    }
    .bot-message {
        background-color: #0099ff;
        color: white;
        text-align: left;
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

load_custom_css()

user_image = Image.open("./images/user.png")
bot_image = Image.open("./images/bot.png")

# Initialize the chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = deque()



# Function to call the Gemini API
def call_gemini_api(user_input):
    """
    Calls the Gemini API to generate content based on the user input.
    @param:
        user_input (str): The input provided by the user.
    Returns:
        str: The generated content from the Gemini API.
    """

    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(user_input)
    return response.text



# Streamlit app layout
st.title("Chat with Gemini API")

# Input area
col1, col2 = st.columns([1, 5])
with col1:
    st.image(user_image, width=50, caption='User')
with col2:
    user_input = st.text_input("You:", key="input")


if st.button("Send"):
    if user_input:
        # Append user input to chat history
        st.session_state.chat_history.appendleft({"sender": "user", "message": user_input})
        
        # Get response from Gemini API
        response = call_gemini_api(user_input)
        
        # Append Gemini API response to chat history
        st.session_state.chat_history.appendleft({"sender": "Gemini", "message": response})

# Clear chat history button
if st.button("Clear Chat"):
    st.session_state.chat_history = deque()

# Display chat history
for chat in st.session_state.chat_history:
    if chat["sender"] == "user":
        col1, col2 = st.columns([1, 5])
        with col1:
            st.image(user_image, width=50, caption='User')
        with col2:
            st.markdown(f"<div class='chat-message user-message'>{chat['message']}</div>", unsafe_allow_html=True)
    else:
        col1, col2 = st.columns([1, 5])
        with col1:
            st.image(bot_image, width=50, caption='Gemini')
        with col2:
            st.markdown(chat['message'])

