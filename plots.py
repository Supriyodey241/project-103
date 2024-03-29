import pandas as pd
import plotly.express as px
import csv
df = pd.read_csv("data.csv")

fig = px.line(df, x = "date", y = "cases", color = "country")
fig.show()