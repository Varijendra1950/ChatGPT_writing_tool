import streamlit as st
import openai


st.title('Chatting with ChatGPT')
st.sidebar.header('Information')
st.sidebar.info('A Streamlit web application that allows you to interact with \
                the OpenAI API\'s implementation of the ChatGPT model.')


engine = 'text-davinci-003'
openai_key = ''



def chatGPT(query):
    completion = openai.Completion.create(engine=engine, prompt=query,
                 max_tokens=1024, n=1, temperature=0.5)
    response = completion.choices[0].text
    return response


ask_chatGPT = st.text_input('Chat with ChatGPT here', value='Who invented Python?')
key = st.sidebar.text_input('Enter your openai_key')
openai.api_key = key
if st.button('Send'):
    response = chatGPT(ask_chatGPT)
    st.write(f'{response}')
