import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Dashboard Analítico - Países")

df = px.data.gapminder()

continente = st.sidebar.selectbox(
    "Escolha o Continente:", df["continent"].unique()
)
df_f = df[df["continent"] == continente]

st.subheader(f"Evolução no Continente: {continente}")
fig_linha = px.line(
    df_f, x="year", y="gdpPercap", color="country", template="simple_white"
)
st.plotly_chart(fig_linha, use_container_width=True)

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

st.subheader("Dados Detalhados")
st.dataframe(df_recente[["country", "pop", "lifeExp", "gdpPercap"]])
