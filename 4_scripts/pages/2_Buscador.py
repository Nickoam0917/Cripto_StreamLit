import streamlit as st
import pandas as pd
import json

st.set_page_config(
    page_title="Cripto Currencies",
    page_icon="💸",
    layout="wide")


yahoo = pd.read_json('./lista.json')

#Tratar as linhas e transformar (astype)
#yahoo['price'] = yahoo['price'].str.replace(',','').str.replace('.','').astype(float)
yahoo['change'] = yahoo['change'].str.replace(',', '').str.replace('.', '').str.replace('+', '').str.replace('-', '').astype(float)
yahoo['per_market'] = yahoo['per_market'].str.replace('+','').str.replace('%','').str.replace(',','.').astype(float)
yahoo['market'] = yahoo['market'].str.replace('.','').str.replace('T','').str.replace('B','').astype(float)

yahoo = st.session_state["data"] = yahoo

moeda = yahoo["name"].value_counts().index
name = st.sidebar.selectbox('Criptomoeda', moeda)

cripto_stats =  yahoo[yahoo["name"] == name].iloc[0]
st.title(f"{cripto_stats['name']}")

st.divider()
st.subheader(f"Preço USD {cripto_stats['price']}")


col1, col2, col3 = st.columns(3)
change_value = cripto_stats['change']
perMarket_value = cripto_stats['per_market']
market_value = cripto_stats['market']
col1.metric(label="Alteração", value=f"{change_value}")
#col2.metric(label="Percentual de Alteração", value= f"Percentual: {perMarket_value}%")
#col3.metric(label="Valor de Mercado", value=f"{market_value}")

col2.metric(label="Percentual de Alteração", value=f"{market_value}",
            delta=f"{perMarket_value}%")