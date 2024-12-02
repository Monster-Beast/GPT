import streamlit as st
import requests

st.set_page_config(page_title="ChatGPT 聊天机器人")

st.sidebar.title("会话历史")

if 'history' not in st.session_state:
    st.session_state.history = []

for i, msg in enumerate(st.session_state.history):
    st.sidebar.write(f"{i+1}: {msg['content'][:20]}")

user_input = st.text_input("请输入您的消息：")

if st.button("发送") and user_input:
    st.session_state.history.append({"role": "user", "content": user_input})
    response = requests.post("http://localhost:8000/chat", json={"messages": st.session_state.history})
    assistant_reply = response.json()['choices'][0]['message']['content']
    st.session_state.history.append({"role": "assistant", "content": assistant_reply})

    for msg in st.session_state.history[-2:]:
        if msg['role'] == 'user':
            st.write(f"**你**：{msg['content']}")
        else:
            st.write(f"**聊天机器人**：{msg['content']}")