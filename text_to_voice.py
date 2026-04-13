import streamlit as st
from gtts import gTTS
from io import BytesIO

st.title(" Text to Voice")

text = st.text_area("Enter text", placeholder="Type anything here...")
lang = st.selectbox("Language", ["en", "ur", "hi", "ar"])

if st.button("Convert to Voice"):
    if not text.strip():
        st.warning("Please enter some text.")
    else:
        tts = gTTS(text=text, lang=lang)
        audio_bytes = BytesIO()
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)
        st.audio(audio_bytes, format="audio/mp3", autoplay=True)
        st.success("Done!")