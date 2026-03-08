import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Load processed data
df = pd.read_csv("formatted_sales.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Sort data
df = df.sort_values("date")

# Create line chart
fig = px.line(
    df,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time",
    markers=True
)

fig.update_layout(
    template="plotly_white",
    xaxis_title="Date",
    yaxis_title="Sales ($)",
    title_x=0.5,
    plot_bgcolor="#fff5f8",
    paper_bgcolor="#fff5f8",
    font=dict(color="#5a2a3b")
)

# Create Dash app
app = Dash(__name__)

app.layout = html.Div(

    style={
        "backgroundColor": "#ffe6f0",
        "fontFamily": "Arial",
        "padding": "20px"
    },

    children=[

        # HEADER SECTION
        html.Div(
            style={
                "display": "flex",
                "alignItems": "center",
                "justifyContent": "center",
                "marginBottom": "30px"
            },
            children=[

                # TITLE
                html.H1(
                    "Soul Foods Pink Morsel Sales Dashboard",
                    style={
                        "color": "#ff4d94",
                        "textAlign": "center"
                    }
                )
            ]
        ),

        # DESCRIPTION
        html.P(
            "Visualizing Pink Morsel sales trends before and after the January 15, 2021 price increase.",
            style={
                "textAlign": "center",
                "color": "#5a2a3b",
                "marginBottom": "30px"
            }
        ),

        # CHART CONTAINER
        html.Div(
            style={
                "backgroundColor": "#ffffff",
                "padding": "20px",
                "borderRadius": "12px",
                "boxShadow": "0px 4px 10px rgba(0,0,0,0.15)"
            },

            children=[
                dcc.Graph(
                    id="sales-chart",
                    figure=fig
                )
            ]
        )
    ]
)

if __name__ == "__main__":
    app.run(debug=True) 