import dash_leaflet as dl
from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State
import os


app = Dash()  
app.layout = html.Div([
    html.H1(id = 'textout'),
    dl.Map(id = "output-state"),
    dcc.Input(id = 'lat', value = 39.298, type = 'number'),
    dcc.Input(id = 'long', value = -76.590, type = 'number'),
    dcc.Input(id = 'zoom', value = 11, type = 'number'),
    html.Button('Submit', id='submit-button')
])

@app.callback(Output('output-state', 'children'),
              Input('submit-button', 'n_clicks'),
              State('lat', 'value'),
              State('long', 'value'),
              State('zoom', 'value'))
def update_output(n_clicks, lat, long, zoom):
    if n_clicks is not None:
        return dl.Map([dl.TileLayer()], 
                        center = (lat, long), 
                        zoom = zoom,
                        style={'width': '100%', 'height': '75vh', 'margin': "auto", "display": "block"})

@app.callback(Output('textout', 'children'),
              Input('submit-button', 'n_clicks'),
              State('lat', 'value'),
              State('long', 'value'),
              State('zoom', 'value'))
def update_text(n_clicks, lat, long, zoom):    
        return  'Lat {}, Long {},  zoom {}, number of clicks {} times'.format(lat, long, zoom, n_clicks)

if __name__ == '__main__':
    app.run_server(debug = False,  host = 'jupyter.biostat.jhsph.edu', port=os.getuid()+33)