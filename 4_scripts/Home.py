import os
import streamlit as st
import pandas as pd
from PIL import Image
import sqlalchemy as sqa 

# Personalizar o título da página
st.set_page_config(
    page_title="Cripto Currencies",
    page_icon="💸",
    layout="wide"
)

#Criar a interface com o banco
engine = sqa.create_engine("sqlite:///cotacao_yahoo.db")
conn = engine.connect()

# Definir uma função para carregar dados do banco de dados
@st.cache_data
def load_data():
    query = "SELECT * FROM 'cotacao_yahoo.db'"
    yahoo = conn.query(query)
    return 

yahoo = load_data()

df_yahoo= pd.read_sql('cotacao_yahoo.db', con=conn)
df_yahoo_cotacao = pd.DataFrame(df_yahoo, columns=['name', 'price', 'change', 'per_market', 'market'])


st.dataframe(yahoo)


image_path = '4_scripts/bitcoin2.png'  # ou 'images/bitcoin2.png' se estiver em um subdiretório

# Verificar se o arquivo de imagem existe
if os.path.exists(image_path):
    logo = Image.open(image_path)
else:
    st.error(f"Arquivo não encontrado: {image_path}")

col1, col2, col3 = st.columns([1, 20, 1])

# Coluna vazia para espaço em branco à esquerda da logo
with col1:
    st.write("")

# Coluna com a logo
with col2:
    if os.path.exists(image_path):
        st.image(logo, width=100)  # Defina a largura desejada para a logo

# Coluna vazia para espaço em branco à direita da logo
with col3:
    st.write("")


st.title('CriptoMoedas Ao Vivo')

st.write("# CRYPTO CURRENCIES💸")

st.write("""
Criptomoedas são moedas digitais ou virtuais que usam criptografia para segurança. 
Elas operam de forma descentralizada na maioria das vezes, utilizando a tecnologia blockchain.
A seguir, apresentamos algumas das principais criptomoedas com suas respectivas mudanças de preço e valor de mercado.
""")

st.header('Tabela de Dados Gerais')
st.dataframe(yahoo, width=1500, height=500, hide_index=True)


