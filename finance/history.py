import streamlit as st
from yFinance import hist

st.title("JFinance - Dados Históricos")

col1, col2, col3 = st.columns(3)

with col1:
    ticker = st.text_input("Ex.: MGLU3, PETR4, ABEV3.")
with col2:
    ""
with col3:
    ""

if ticker:
    st.dataframe(hist(ticker))
else:
    "Digite um ticker para exibir dados históricos."