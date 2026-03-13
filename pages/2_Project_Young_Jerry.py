import streamlit as st
import requests

# Page‑specific chat history key
CHAT_KEY = "junior_jerry_messages"

# ==== CONFIG ====

# Define your servers (index 0 and index 1)
SERVER_URLS = [
    "http://192.168.8.91:1234",  # server 0 (Pi)
    "http://192.168.8.87:1234",  # server 1 (Smart Jerry / Colab)
]

SERVER_NAMES = [
    "Server 0 - Raspberry Pi 5",
    "Server 1 - Mac mini M4"
]

# When opening this page, clear any other chat page's history
for key in ("smart_jerry_messages",):
    if key in st.session_state:
        del st.session_state[key]

# User selects which server to use
selected_server_idx = st.selectbox(
    "Select server",
    options=list(range(len(SERVER_NAMES))),  # 0, 1, ...
    format_func=lambda i: SERVER_NAMES[i],   # show friendly label instead of number
    index=0,                                 # default: server 0
)

# Map selected option (0 or 1) to the actual base URL
API_BASE = SERVER_URLS[selected_server_idx]
API_URL = f"{API_BASE}/v1/chat/completions"
MODELS_API_URL = f"{API_BASE}/v1/models"


def fetch_models():
    """Fetch chat-capable models from the API (excludes embedding models)."""
    try:
        response = requests.get(MODELS_API_URL, timeout=5)
        response.raise_for_status()
        data = response.json()
        raw = data.get("data", data) if isinstance(data, dict) else data
        if not isinstance(raw, list):
            return []
        all_models = [
            m.get("id", m) if isinstance(m, dict) else str(m)
            for m in raw
        ]
        # Exclude embedding models - they don't support chat completions
        return [m for m in all_models if "embed" not in m.lower()]
    except Exception as e:
        st.warning(f"Could not fetch models: {e}")
        return []


# ==== UI ====
st.title("Junior Jerry LLM Chat")

# Initialize chat history for this page
if CHAT_KEY not in st.session_state:
    st.session_state[CHAT_KEY] = []

# Model selector
models = fetch_models()
if models:
    default_idx = 0
    if "selected_model" in st.session_state and st.session_state.selected_model in models:
        default_idx = models.index(st.session_state.selected_model)
    selected_model = st.selectbox(
        "Select model",
        options=models,
        index=default_idx,
        key="model_selector",
    )
    st.session_state.selected_model = selected_model
else:
    selected_model = st.text_input("Model (API unavailable)", value="liquid/lfm2.5-1.2b")
    st.session_state.selected_model = selected_model

# Display chat history
for msg in st.session_state[CHAT_KEY]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
prompt = st.chat_input("Type your message...")

if prompt:
    # Show user message
    st.session_state[CHAT_KEY].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Call API
    payload = {
        "model": st.session_state.selected_model,
        "messages": st.session_state[CHAT_KEY],
        "temperature": 0.7
    }

    try:
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()
        data = response.json()

        assistant_reply = data["choices"][0]["message"]["content"]

    except Exception as e:
        assistant_reply = f"Error: {e}"

    # Show assistant reply
    st.session_state[CHAT_KEY].append({"role": "assistant", "content": assistant_reply})
    with st.chat_message("assistant"):
        st.markdown(assistant_reply)
