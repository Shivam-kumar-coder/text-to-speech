import streamlit as st
from gtts import gTTS as gt

st.title("Text to Speech Converter")

with st.form(key='text_to_speech_form'):
    text_input = st.text_input("Enter text")
    file_uploader = st.file_uploader("Choose a file", type=["txt"])
    submit_button = st.form_submit_button(label='Convert')

if submit_button:
    file_content = None
    if file_uploader is not None:
        file_content = file_uploader.read().decode("utf-8")

    if text_input:
        c = gt(text=text_input, lang="en")
    elif file_content:
        c = gt(text=file_content, lang="en")
    else:
        st.error("Please provide text or upload a file.")
    
    c.save("web.mp3")
    st.success("Converted successfully")
    audio_file = open("web.mp3", "rb")
    audio = audio_file.read()
    st.audio(audio, format='audio/ogg')


hide_menu = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)
