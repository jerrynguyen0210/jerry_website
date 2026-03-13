import streamlit as st
import requests

# Use a page‑specific chat history key so it
# doesn't conflict with other pages.
CHAT_KEY = "smart_jerry_messages"

# Static fallback list of models
FALLBACK_MODEL_OPTIONS = [
    "qwen3-vl:30b",
    "gpt-oss:20b",
    "llama3:8b",
]

# 🔥 CHANGE THIS TO YOUR NGROK URL
OLLAMA_URL = "https://decadently-untunnelled-edwin.ngrok-free.dev/"
COLAB_URL = "https://www.kaggle.com/code/jerrynguyen0210/ollama-demo/edit/"


def fetch_models():
    """
    Fetch available models from the Ollama API.
    Falls back to a static list if the request fails.
    """
    try:
        resp = requests.get(f"{OLLAMA_URL}/api/tags", timeout=5)
        resp.raise_for_status()
        data = resp.json()
        # Typical Ollama /api/tags response: {"models": [{"name": "model:tag"}, ...]}
        models = [
            m.get("name")
            for m in data.get("models", [])
            if isinstance(m, dict) and m.get("name")
        ]
        if not models:
            raise ValueError("No models found in /api/tags response")
        return models
    except Exception as e:
        st.warning(f"Could not fetch models from API, using defaults. Error: {e}")
        return FALLBACK_MODEL_OPTIONS


st.title("Smart Jerry Chatbot!")

# When opening this page, clear any other chat page's history
# so that chats are reset after switching pages.
for key in ("junior_jerry_messages",):
    if key in st.session_state:
        del st.session_state[key]

# Button linking to the Colab/ngrok endpoint
st.link_button("Open Colab backend", COLAB_URL)

# Model selector (persists per-session), populated from API when possible
model_options = fetch_models()
default_idx = 0
if (
    "smart_jerry_model" in st.session_state
    and st.session_state.smart_jerry_model in model_options
):
    default_idx = model_options.index(st.session_state.smart_jerry_model)

selected_model = st.selectbox(
    "Select model",
    options=model_options,
    index=default_idx,
    key="smart_jerry_model",
)

# Initialize chat history for this page
if CHAT_KEY not in st.session_state:
    st.session_state[CHAT_KEY] = []

# Display chat history
for message in st.session_state[CHAT_KEY]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Type your message..."):

    # Add user message
    st.session_state[CHAT_KEY].append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # Send request to Ollama
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            try:
                response = requests.post(
                    f"{OLLAMA_URL}/api/generate",
                    json={
                        "model": selected_model,
                        "prompt": prompt,
                        "stream": False,
                    },
                    headers={
                        "Content-Type": "application/json",
                        "ngrok-skip-browser-warning": "true",
                    },
                    timeout=300,
                )

                if response.status_code == 200:
                    reply = response.json()["response"]
                else:
                    reply = f"Error: {response.status_code}\n{response.text}"

            except Exception as e:
                reply = f"Connection error:\n{str(e)}"

        st.markdown(reply)

    st.session_state[CHAT_KEY].append({"role": "assistant", "content": reply})
