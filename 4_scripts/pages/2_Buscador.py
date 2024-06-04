
import sqlalchemy as sqa 
import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Cripto Currencies",
    page_icon="💸",
    layout="wide")


#Criar a interface com o banco
conn = st.connection("mydb", type="sql")

# Definir uma função para carregar dados do banco de dados
@st.cache_data
def load_data():
    query = "SELECT * FROM 'cotacao_yahoo.db'"
    yahoo = conn.query(query)
    return 

yahoo = load_data()

st.dataframe(yahoo)


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
