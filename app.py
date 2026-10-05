import streamlit as st

from tallyhold import __version__

st.set_page_config(page_title="Tallyhold", layout="wide")

st.title("Tallyhold")
st.caption(f"Offline data management, validation and profiling tool · v{__version__}")