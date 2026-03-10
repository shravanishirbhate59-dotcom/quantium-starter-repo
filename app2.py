import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output

# Load data
df = pd.read_csv("formatted_sales.csv")

# Prepare data
df["date"] = pd.to_datetime(df["date"])
df["region"] = df["region"].str.lower()
df = df.sort_values("date")

# Create app
app = Dash(__name__)

# Layout
app.layout = html.Div(

    style={
        "backgroundColor": "#ffe6f0",
        "fontFamily": "Arial",
        "padding": "30px"
    },

    children=[

        # HEADER
        html.H1(
            "🍬 Soul Foods Pink Morsel Sales Dashboard",
            style={
                "textAlign": "center",
                "color": "#ff4d94"
            }
        ),

        html.P(
            "Explore sales trends before and after the Pink Morsel price increase on January 15, 2021.",
            style={
                "textAlign": "center",
                "color": "#5a2a3b",
                "fontSize": "18px",
                "marginBottom": "30px"
            }
        ),

        # FILTER SECTION
        html.Div([

            html.H3("Filter by Region", style={"color": "#ff4d94"}),

            dcc.RadioItems(
                id="region-filter",
                options=[
                    {"label": "North", "value": "north"},
                    {"label": "East", "value": "east"},
                    {"label": "South", "value": "south"},
                    {"label": "West", "value": "west"},
                    {"label": "All Regions", "value": "all"}
                ],
                value="all",
                inline=True
            ),

            html.Br(),

            html.H3("Select Date Range", style={"color": "#ff4d94"}),

            dcc.DatePickerRange(
                id="date-range",
                start_date=df["date"].min(),
                end_date=df["date"].max(),
                display_format="YYYY-MM-DD"
            )

        ],

        style={
            "backgroundColor": "white",
            "padding": "25px",
            "borderRadius": "12px",
            "boxShadow": "0px 5px 15px rgba(0,0,0,0.1)",
            "width": "70%",
            "margin": "0 auto 30px auto",
            "textAlign": "center"
        }),

        # GRAPH
        html.Div([

            dcc.Graph(id="sales-chart")

        ],

        style={
            "backgroundColor": "white",
            "padding": "20px",
            "borderRadius": "12px",
            "boxShadow": "0px 5px 15px rgba(0,0,0,0.1)"
        })
    ]
)


# CALLBACK
@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value"),
    Input("date-range", "start_date"),
    Input("date-range", "end_date")
)

def update_chart(region, start_date, end_date):

    filtered_df = df.copy()

    # Region filter
    if region != "all":
        filtered_df = filtered_df[filtered_df["region"] == region]

    # Date filter
    filtered_df = filtered_df[
        (filtered_df["date"] >= start_date) &
        (filtered_df["date"] <= end_date)
    ]

    # Chart
    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        markers=True,
        title=f"Sales Trend - {region.capitalize()}",
        template="plotly_white"
    )

    fig.update_traces(line_color="#ff4d94")

    # Highlight price increase date
    fig.add_vline(
        x="2021-01-15",
        line_width=3,
        line_dash="dash",
        line_color="red"
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Sales ($)",
        title_x=0.5,
        hovermode="x unified"
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)