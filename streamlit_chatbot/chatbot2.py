import streamlit as st
import google.generativeai as genai

user_emoji = "🦈"  # Change this to any emoji you like
robot_img = "robot.jpg"  # Your robot image file path

# Configure Gemini API
GOOGLE_API_KEY = "AIzaSyBRNHjIqWDnXi5mJGAF4hleAYXd2ADq_4o"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')

def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []

def get_gemini_response(prompt, persona_instructions=""):
    """Generate response from Gemini AI model."""
    full_prompt = f"{persona_instructions}\n\nUser:{prompt}\nAssistant:"
    response = model.generate_content(full_prompt)
    return response.text

def main():
    st.title("music recommendations bot🎧")
    initialize_session_state()

    # Define persona_instructions at the beginning
    persona_instructions = """You are a helpful yet witty bot who suggests songs based on how a user is feeling.
    """

    # Sidebar for persona and settings
    with st.sidebar:
        st.title("Sidebar")
        selected_persona = st.radio("Persona", ["Friendly", "Formal", "Funny"], index=2)
        selected_mood = st.multiselect("Mood", ["Depressed", "Sad","Nostalgic", "Okay", "Angry","Chill", "Happy","Romantic","Energetic"], default="Okay")

        st.info(f"The bot knows you're currently feeling: **{selected_mood}**")

        # Update persona instructions based on selection
        if selected_persona == "Friendly":
            persona_instructions = """You are a friendly and helpful assistant. Keep your tone positive and show care.
            Be sure to recommend a song in each response. Reply longer responses."""
        elif selected_persona == "Formal":
            persona_instructions = """You are a formal assistant. Be professional and concise.
            Be sure to recommend a song in each response.Reply longer responses."""
        else:  # "Funny"
            persona_instructions = """
            You are a witty  roast bot who suggests songs based on how a user is feeling.
            Act unbothered but still be helpful.Be sure to recommend a song in each response.Reply longer responses.
            """

    persona_instructions += f"\n\nUSER's CURRENT MOOD (from slider): {selected_mood}"

    # Display chat messages
    for message in st.session_state.messages:
        if message["role"] == "assistant":
            with st.chat_message("assistant", avatar=robot_img):
                st.write(f"{message['content']}")
        else:
            with st.chat_message("user", avatar=user_emoji):
                st.write(f"{message['content']}")

    # Chat input
    prompt = st.chat_input("Type here")

    if prompt:  # Only process if there's a valid prompt from the user
        # Display user message
        with st.chat_message("user"):
            st.write(prompt)

        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Get Gemini response with persona
        response = get_gemini_response(prompt, persona_instructions)

        # Display assistant response
        with st.chat_message("assistant", avatar=robot_img):
            st.write(response)

        # Add assistant response to history
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()