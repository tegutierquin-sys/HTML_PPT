from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Empresas españolas con actividad de semiconductores fotónicos",
    layout="wide",
    initial_sidebar_state="collapsed"
)

html_path = Path(__file__).with_name("index.html")
html_content = html_path.read_text(encoding="utf-8", errors="replace")

components.html(
    html_content,
    height=1_000,
    scrolling=True
)
