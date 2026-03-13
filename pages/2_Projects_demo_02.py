import streamlit as st
import requests

# 🔥 CHANGE THIS TO YOUR NGROK URL
OLLAMA_URL = "https://decadently-untunnelled-edwin.ngrok-free.dev/"

st.title("🤖 Ollama Chatbot (GPU via Colab)")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Type your message..."):

    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # Send request to Ollama
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            try:
                response = requests.post(
                    f"{OLLAMA_URL}/api/generate",
                    json={
                        "model": "qwen3-vl:30b",
                        # "model": "gpt-oss:20b",
                        # "model": "llama3:8b",
                        "prompt": prompt,
                        "stream": False
                    },
                    headers={
                        "Content-Type": "application/json",
                        "ngrok-skip-browser-warning": "true"
                    },
                    timeout=300
                )

                if response.status_code == 200:
                    reply = response.json()["response"]
                else:
                    reply = f"Error: {response.status_code}\n{response.text}"

            except Exception as e:
                reply = f"Connection error:\n{str(e)}"

        st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
