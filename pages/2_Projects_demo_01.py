import streamlit as st
import requests

# ==== CONFIG ====
API_BASE = "http://192.168.8.91:1234"
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
st.title("Raspberry Pi 5 LLM Chat")

if "messages" not in st.session_state:
    st.session_state.messages = []

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
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
prompt = st.chat_input("Type your message...")

if prompt:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Call API
    payload = {
        "model": st.session_state.selected_model,
        "messages": st.session_state.messages,
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
    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
    with st.chat_message("assistant"):
        st.markdown(assistant_reply)
