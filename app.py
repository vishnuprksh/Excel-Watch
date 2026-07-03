import base64
from pathlib import Path

import streamlit as st

from excel_watch import completed, outstanding


st.set_page_config(page_title="Invoice Watch", layout="centered")


def load_theme():
    css_path = Path(__file__).with_name("style.css")
    st.markdown(f"<style>{css_path.read_text()}</style>", unsafe_allow_html=True)


def render_header():
    logo_path = Path(__file__).with_name("assets") / "logo.png"

    if not logo_path.exists():
        st.title("Invoice Watch")
        return

    encoded_logo = base64.b64encode(logo_path.read_bytes()).decode("utf-8")
    st.markdown(
        f"""
        <div class="app-logo-wrap">
            <img class="app-logo" src="data:image/png;base64,{encoded_logo}" alt="Invoice Watch logo">
        </div>
        """,
        unsafe_allow_html=True,
    )


load_theme()

render_header()

selected_option = st.selectbox(
    "Options",
    ["Outstanding", "Completed"],
    key="selected_option",
)

if selected_option == "Outstanding":
    outstanding.render()
else:
    completed.render()
