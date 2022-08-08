import os
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Enter your data to see the results"),
    html.Div([
        html.H2('Enter your weight in kilogram'),
        dcc.Input(id = 'weight', value = 95, type = 'number'),
        html.H2('Enter your height in meter'),
        dcc.Input(id = 'height', value = 2.0, type = 'number')
    ]),
    html.Br(),
    html.H1("Your estimated body mass inndex is: "),
    html.H1(id = 'bmi'),

])


@app.callback(
    Output(component_id = 'bmi'   , component_property = 'children'),
    Input(component_id  = 'weight', component_property = 'value'),
    Input(component_id  = 'height', component_property = 'value')
)
def update_output_div(weight, height):
    
    rval = (weight / (height * height))

    return rval

if __name__ == '__main__':
    app.run_server(debug = False,  host = 'jupyter.biostat.jhsph.edu', port=os.getuid()+34)
