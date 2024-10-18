import streamlit as st

history = st.Page("finance/history.py", title="History", icon=":material/dashboard:", default=True)
indic = st.Page("finance/indic.py", title="Ticker", icon=":material/dashboard:")


pg = st.navigation(
    {"Finance": [history, indic]}
)

pg.run()