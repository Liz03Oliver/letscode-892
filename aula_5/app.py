import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import streamlit as st


# função que carrega o dataset


def carrega_dataset(nome_do_dataset):
    return sns.load_dataset(nome_do_dataset)


# CORPO
## CORPO - Título da Aplicação
st.markdown("""
            ### Ferramenta de analise de dados
            ---
            """)


## CORPO - Carregando o dataset
nome_do_dataset= st.text_input('Qual é o dataset?', value='penguins')

if nome_do_dataset:
    df = carrega_dataset(nome_do_dataset)
 
       
# SIDEBAR
## SIDEBAR - Filtro dos campos
with st.sidebar:
    st.title('Filtros')
    cols_select=\
        st.multiselect("Filtre os campos que deseja analisar:",
                   options=list(df.columns),
                   default=list(df.columns) ) 

# filtra os campos selecionados
df_select= df[cols_select]
    
    
## CORPO - Info do dataset
with st.expander("Dados do Dataseet"):
    st.header('Dados do Dataset')
    st.subheader("Primeiros registros")
    st.write(df_select.head())

    st.subheader("Colunas")
    for cols in df_select.columns:
        st.markdown("- {cols}")
    
    st.subheader('Dados Faltantes')
    st.write(df_select.isna().sum()[df_select.isna().sum() > 0]) 
    
    st.write(df_select.describe())

## CORPO - Análise Univariada

st.header("Análise Univariada")
univar_campo=\
    st.selectbox("Selecione um campo numerico para avaliar sua distribuição:",
             options=list(df_select.select_dtypes(include=np.number).columns))

st.plotly_chart(px.histogram(data_frame=df_select, x=univar_campo))    
st.plotly_chart(px.box(data_frame=df_select, y=univar_campo))  

## CORPO - Análise Bivariada


### CORPO - Análise Bivariada - gráfico de dispersão

        
### CORPO - Análise Bivariada - gráfico de boxplot


### CORPO - Análise Bivariada - gráfico de pairplot

    


# ATIVIDADES
# Refatore o código, aplicando as modificações:

# 1 - Modularize o código passando a função "carrega_dataset" para um módulo

# 2 - Crie um slider no sidebar que permita filtrar uma amostra do dataset.
#     Para realizar amostragem, utilize o método sample do dataframe pandas.

# 3 - Adicione a informação do tamanho do dataset na seção 
#     de 'Dados do Dataset'

# 4 - Adicione uma seção de análise multivariada:
#   4.1 - Adicione a possibilidade de segmentação no gráfico de dispersao
#   4.2 - Adicione checkbox que permita incluir linha de tendência 
#         no gráfico de dispersão
#   4.3 - Adicione a possibilidade de segmentação no gráfico de boxplot
#   4.4 - Adicione a possibilidade de segmentação no gráfico de pairplot

