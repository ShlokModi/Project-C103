import pandas as pd
import plotly_express as pe
df = pd.read_csv("xyz.csv")
fig = pe.scatter(df, x="date", y="cases", color="country")
fig.show()