from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="銀行業務戰情室｜總處＞各區中心＞分行權責平台",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 隱藏 Streamlit 預設上方空白與邊界，讓戰情室完整滿版呈現
st.markdown(
    """
    <style>
      #MainMenu {visibility: hidden;}
      header {visibility: hidden;}
      footer {visibility: hidden;}
      .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        max-width: 100% !important;
      }
      iframe {
        width: 100% !important;
        border: none !important;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).parent / "BusinessWarRoom.html"

if html_path.exists():
    html_content = html_path.read_text(encoding="utf-8")
    components.html(html_content, height=1350, scrolling=True)
else:
    st.error("找不到 BusinessWarRoom.html，請先執行 `python build_warroom_html.py` 產生戰情室檔案。")
