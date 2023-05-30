import streamlit as st
import openai

# Streamlit Community Cloud - get OpenAI API key in the Secrets
openai.api_key = st.secrets.OpenAIAPI.openai_api_key

# st.session_state - save the conversation
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": st.secrets.AppSettings.chatbot_setting}
        ]

# Function to communicate with chatbot
def communicate():
    messages = st.session_state["messages"]

    user_message = {"role": "user", "content": st.session_state["user_input"]}
    messages.append(user_message)

    response = openai.ChatCompletion.create(
        model="davinci:ft-personal-2023-05-30-19-10-49",
        messages=messages,
	top_p=1,
	temperature=1
    )  

    bot_message = response["choices"][0]["message"]
    messages.append(bot_message)

    st.session_state["user_input"] = ""  # Remove the existing input

# Building UI
st.title("Shingo's IT Risk and Control Assistant")
st.image("robot.png")
st.write("I am a chatbot based on ChatGPT API, specialised on IT general controls, application controls, SOX regulation, internal control, and internal audit")

user_input = st.text_input("Please enter your message.", key="user_input", on_change=communicate)

if st.session_state["messages"]:
    messages = st.session_state["messages"]

    for message in reversed(messages[1:]):  # Move the latest to the top
        speaker = "🙂"
        if message["role"]=="assistant":
            speaker="🤖"

        st.write(speaker + ": " + message["content"])