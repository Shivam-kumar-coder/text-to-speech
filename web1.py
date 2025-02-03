from gtts import gTTS as gt
import streamlit as st

try:
    st.title("text to speech  convertor by coder-shivam ")

    a=st.text_input("enter input")

    c=gt(text=a,lang="en")
    c.save("web.mp3")

    if a:
        if c:
            st.success("converted succesfully")
            audio_file=open("web.mp3","rb")
            audio=audio_file.read()
            st.audio(audio,format='audio/ogg')

        else:
            st.error("please text another")
except Exception as e:
    print(e)
