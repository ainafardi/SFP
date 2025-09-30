import streamlit as st
import pandas as pd
import google.generativeai as genai

user_emoji = "👤" # Change this to any emojis you like
robot_img = "robot.jpg" # Find a picture online(jpg/png), download it and drag to
											# your files under the Chatbot folder

# Configure Gemini API
GOOGLE_API_KEY = "AIzaSyBRNHjIqWDnXi5mJGAF4hleAYXd2ADq_4o"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')

def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []


def get_gemini_response(prompt, persona_instructions):
            full_prompt = f"{persona_instructions}\n\nUser: {prompt}\nAssistant:"
            response = model.generate_content(full_prompt)
            return response.text

def main():
    st.title("Gemini AI Chatbot")
    
    initialize_session_state()

    # Display chat messages
            # Replace the section in the code that says "Display chat messages" with this code
    for message in st.session_state.messages:
        if message["role"] == "assistant":
            with st.chat_message("assistant", avatar=robot_img):
                st.write(f"{message['content']}")
        else:
            with st.chat_message("user", avatar=user_emoji):
                st.write(f"{message['content']}")

    # Chat input
    if prompt := st.chat_input("Chat with Gemini"):
        # Display user message
        with st.chat_message("user"):
            st.write(prompt)
        
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Get Gemini response
        
            # Display assistant response
        with st.chat_message("assistant"):
            st.write(response)
        
            # Add assistant response to history
            st.session_state.messages.append({"role": "assistant", "content": response})

        if prompt := st.chat_input("Chat with Gemini"):
    # Display user message
             with st.chat_message("user"):
                st.write(prompt)

    st.session_state.messages.append({"role": "user", "content": prompt})
    # Get Gemini response with persona
    response = get_gemini_response(prompt, persona_instructions)

    
    # Display assistant response
    with st.chat_message("assistant"):
        st.write(response)

    st.session_state.messages.append({"role": "assistant", "content": response})


with st.sidebar:
    st.title("Sidebar") 
    st.radio("Radio-button select", ["Friendly", "Formal", "Funny"], index=0)
    st.multiselect("Multi-select", ["Movies", "Travel", "Food", "Sports"], default=["Food"])
    st.selectbox("Dropdown select", ["Data", "Code", "Travel", "Food", "Sports"], index=0)
    st.slider("Slider", min_value=1, max_value=200, value=60)
    st.select_slider("Option Slider", options=["Very Sad", "Sad", "Okay", "Happy", "Very Happy"], value="Okay")

    persona_instructions = """
    You are a hilarious roast bot.
    Be playful and witty.
    Your roasts should be light-hearted, never offensive.
    Use funny emojis and sarcasm in your replies.
    """


if __name__ == "__main__":
    main()