import pandas as pd
import os

os.makedirs("data/raw", exist_ok=True)

data = {
    "CCAA": [
        "Andalucía",
        "Aragón",
        "Asturias",
        "Baleares",
        "Canarias",
        "Cantabria",
        "Castilla y León",
        "Castilla-La Mancha",
        "Cataluña",
        "C. Valenciana",
        "Extremadura",
        "Galicia",
        "Madrid",
        "Murcia",
        "Navarra",
        "País Vasco",
        "La Rioja",
    ],
    "Gasto_Habitante": [
        1550,
        1820,
        1950,
        1600,
        1580,
        1890,
        1850,
        1750,
        1780,
        1650,
        1720,
        1810,
        1520,
        1680,
        1920,
        2100,
        1840,
    ],
    "Esperanza_Vida": [
        82.1,
        83.5,
        82.8,
        83.2,
        82.5,
        83.4,
        84.1,
        83.0,
        83.8,
        82.9,
        82.4,
        83.6,
        85.1,
        82.7,
        84.5,
        84.2,
        83.9,
    ],
}

df = pd.DataFrame(data)
df.to_csv("data/raw/sanidad_espana.csv", index=False, encoding="utf-8-sig")

print("Dataset raw generado correctamente")
