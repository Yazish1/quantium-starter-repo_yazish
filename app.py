from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()
df = pd.read_csv(r"quantium-starter-repo_yazish\data\pink_morsel_sales.csv")

df["date"] = pd.to_datetime(df["date"], errors="coerce")
df = df[(df["date"] >= "2021-01-01") &
        (df["date"] < "2021-02-01")]

daily_sales = (
    df.groupby("date", as_index=False)["total"]
      .sum()
      .sort_values("date")
)

fig = px.line(daily_sales, x="date", y="total")


app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='Pink-Morsel-Sales-Graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
