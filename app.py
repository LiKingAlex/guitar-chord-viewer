import streamlit as st
import streamlit.components.v1 as components

# Read your HTML file
with open("guitar_chords.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Display it
st.title("🎸 Guitar Chords Visualizer")
components.html(html_content, height=900, scrolling=True)
