from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)
df = pd.read_csv(r"quantium-starter-repo_yazish\data\pink_morsel_sales.csv")
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df = df[
    (df["date"] >= "2021-01-01") & (df["date"] <= "2021-02-01")]

app.layout = html.Div(
    className="container",
    children=[
        html.H1("Pink Morsel sales - January 2021",
            className="title"),
        dcc.RadioItems(
            id="region",
            className="radio",
            options= [
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "West", "value": "west"},
                {"label": "South", "value": "south"},
                {"label": "East", "value": "east"},
            ],
            value="all",
            inline=True
        ),
        html.Div(
            dcc.Graph(id="Pink-Morsel-Sales",
                className="graph")
        )
    ]
)

@app.callback(
    Output("Pink-Morsel-Sales", "figure"),
    Input("region", "value")
)

def update(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]
    
    daily_sales = (
        filtered_df
        .groupby("date", as_index=False)["total"]
        .sum()
        .sort_values("date")
    )
    
    fig = px.line(
        daily_sales, x="date", y="total",
        labels={
            "date": "Date",
            "total": "Sales amount ($)"
        },
        title=f"Pink Morsel Sales for {selected_region.upper()} (January 2021)"
    )
    return fig

if __name__ == '__main__':
    app.run(debug=True)
