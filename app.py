import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Dashboard Analítico - Países")

# 1. Carrega os dados direto do Plotly (sem funções complexas)
df = px.data.gapminder()

# 2. Filtro simples na barra lateral (Zoom & Filter)
continente = st.sidebar.selectbox(
    "Escolha o Continente:", df["continent"].unique()
)
df_f = df[df["continent"] == continente]

# 3. Gráfico 1: Linha temporal
st.subheader(f"Evolução no Continente: {continente}")
fig_linha = px.line(
    df_f, x="year", y="gdpPercap", color="country", template="simple_white"
)
st.plotly_chart(fig_linha, use_container_width=True)

# 4. Gráfico 2: Barras ordenadas (Top países por população)
df_recente = df_f[df_f["year"] == 2007]
fig_barra = px.bar(
    df_recente.sort_values("pop"),
    x="pop",
    y="country",
    orientation="h",
    color="pop",
    color_continuous_scale="Viridis",
    template="simple_white",
)
st.plotly_chart(fig_barra, use_container_width=True)

# 5. Detalhes sob demanda (Tabela simples filtrada)
st.subheader("Dados Detalhados")
st.dataframe(df_recente[["country", "pop", "lifeExp", "gdpPercap"]])