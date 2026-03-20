import pandas as pd
import plotly.express as px

df = pd.read_csv("data/raw/sanidad_espana.csv")

df["Eficiencia"] = (df["Esperanza_Vida"] / df["Gasto_Habitante"]) * 1000
df["Eficiencia"] = df["Eficiencia"].round(2)

fig = px.scatter(
    df,
    x="Gasto_Habitante",
    y="Esperanza_Vida",
    size="Eficiencia",
    color="CCAA",
    hover_name="CCAA",
    title="SISTEMA SANITARIO ESPAÑOL: ANÁLISIS DE EFICIENCIA E INVERSIÓN",
    labels={
        "Gasto_Habitante": "Inversión por Habitante (€)",
        "Esperanza_Vida": "Expectativa de Vida (Años)",
        "Eficiencia": "Ratio de Eficiencia",
    },
    text="CCAA",
    template="plotly_dark",
)

fig.update_traces(
    textposition="top center", marker=dict(line=dict(width=1, color="white"))
)

fig.update_layout(
    font_family="Arial",
    title_font_size=22,
    xaxis=dict(showgrid=False, zeroline=False),
    yaxis=dict(showgrid=True, gridcolor="gray"),
)

fig.write_html("index.html")

print("Visualización interactiva desplegada en index.html")
