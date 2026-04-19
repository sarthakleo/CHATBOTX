import streamlit as st
from bot import stream_chat, new_conversation
from config import (
    APP_TITLE, APP_ICON, APP_CAPTION,
    WELCOME_MESSAGE, QUICK_QUESTIONS,
)

st.set_page_config(
    page_title=APP_TITLE,
    page_icon=":" + APP_ICON + ":",
    layout="centered",
)

if "messages" not in st.session_state:
    st.session_state.messages = new_conversation()
    st.session_state.messages.append({
        "role": "assistant",
        "content": WELCOME_MESSAGE,
    })

st.title(APP_TITLE)
st.caption(APP_CAPTION)

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

with st.sidebar:
    st.subheader("Quick questions")
    for question in QUICK_QUESTIONS:
        if st.button(question, use_container_width=True):
            st.session_state.pending_input = question
    
    st.divider()
    if st.button("Clear conversation", use_container_width=True):
        st.session_state.messages = new_conversation()
        st.session_state.messages.append({
            "role": "assistant",
            "content": WELCOME_MESSAGE,
        })
        st.rerun()
    
    st.caption("Powered by Claude · Codenixia 2026")

def handle_message(user_msg: str) -> None:
    # Show user bubble
    with st.chat_message("user"):
        st.markdown(user_msg)
    
    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_reply = ""
        for chunk in stream_chat(st.session_state.messages, user_msg):
            full_reply += chunk
            placeholder.markdown(full_reply + "▌")
        placeholder.markdown(full_reply)
    
    st.session_state.messages.append({
        "role": "assistant",
        "content": full_reply,
    })


if "pending_input" in st.session_state:
    user_msg = st.session_state.pop("pending_input")
    handle_message(user_msg)

if prompt := st.chat_input("Ask about our courses..."):
    handle_message(prompt)
