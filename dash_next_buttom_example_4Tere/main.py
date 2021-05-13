import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

layout_screen1=html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),    dbc.Button("Next", id='next_id'),dbc.Button("Back", id='back_id', style = dict(display='none'))
])

layout_screen2=html.Div(children=[
    html.H1(children='Hello Dash 2'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),    dbc.Button("Back", id='back_id'),dbc.Button( id='next_id', style = dict(display='none'))
])

# CALLBACK

@app.callback(
    dash.dependencies.Output('layout', 'children'),
    [dash.dependencies.Input('next_id', 'n_clicks'),dash.dependencies.Input('back_id', 'n_clicks')]
)
def next_layout(n_clicks,n2):
    ctx = dash.callback_context

    if not ctx.triggered:
        return layout_screen1
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        print(button_id)
        if button_id=='next_id':
            return layout_screen2
        elif button_id=='back_id':
            return layout_screen1
        else:
            return layout_screen1

app.layout = html.Div(children=[layout_screen1],id='layout')

if __name__ == '__main__':
    app.run_server(debug=True)
