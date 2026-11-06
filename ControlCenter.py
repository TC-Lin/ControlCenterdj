from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="銀行業務戰情室｜總處＞各區中心＞分行權責平台",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 讓 Streamlit 的 iframe 固定貼齊瀏覽器視窗 (100vw x 100vh)，
# 確保內部放大視窗 (Modal) 與固定側邊欄永遠 100% 置中於螢幕正中央，且不會產生雙層捲軸
st.markdown(
    """
    <style>
      #MainMenu, header, footer, [data-testid="stHeader"], [data-testid="stToolbar"] {
        display: none !important;
        visibility: hidden !important;
      }
      html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"], .main, .block-container {
        margin: 0 !important;
        padding: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        max-width: 100vw !important;
        overflow: hidden !important;
      }
      iframe {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        border: none !important;
        margin: 0 !important;
        padding: 0 !important;
        z-index: 9999 !important;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).parent / "BusinessWarRoom.html"

if html_path.exists():
    html_content = html_path.read_text(encoding="utf-8")
    components.html(html_content, height=900, scrolling=True)
else:
    st.error("找不到 BusinessWarRoom.html，請先執行 `python build_warroom_html.py` 產生戰情室檔案。")
