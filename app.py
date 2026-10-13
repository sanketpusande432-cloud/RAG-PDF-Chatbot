import streamlit as st
from response import generate_response

st.title('!!! RAG Chatbot !!!')

if 'messages' not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg['role']):
        st.write(msg['message'])

question = st.chat_input('Enter Question')

if question:
    with st.chat_message('user'):
        st.write(question)

    st.session_state.messages.append({
        'role': 'user',
        'message': question
    })

    result, sources = generate_response(
        question,
        previous_history=st.session_state.messages[-4:]
    )

    if result:
        with st.chat_message('assistant'):
            st.write(result)

            with st.expander('Source'):
                st.write(sources)

        st.session_state.messages.append({
            'role': 'assistant',
            'message': result
        })