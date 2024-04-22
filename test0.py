import dash
from dash import html
from dash import dcc
from dash import Dash, dash_table, html, Input, Output, Patch, callback
import plotly.graph_objs as go
from datetime import datetime

# Data
x_data = ["2021-12-21T19:58:00.542000", "2021-12-21T19:58:01.542000", "2021-12-21T19:58:02.542000"]
x_data = [datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f') for date in x_data]  # Convert strings to datetime objects
y_data = [13500.0, 13503.33591, 13506.67183]
z_data = [
    [599.8054, 581.1404, 570.4771],
    [678.9323, 644.2858, 610.9979],
    [576.6772, 568.9164, 565.6251]
]

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    dcc.Graph(
        id='heatmap1',
        figure={
            'data': [go.Heatmap(
                x=x_data,
                y=y_data,
                z=z_data,
                type='heatmap',
                colorscale='Viridis'
            )],
            'layout': go.Layout(
                title='Heatmap',
                xaxis=dict(title='Time'),
                yaxis=dict(title='Y Value')
            )
        }
    ),
    html.Button("Delete first row", id="delete-button-1")
])

# Deleting row at index 0 in the data when the delete button is clicked
@callback(
    Output("heatmap1", "figure"),
    Input("delete-button-1", "n_clicks")
)
def delete_records(n_clicks):
    patched_table = Patch()
    if n_clicks:
        patched_table.delHeat(0, 3)
    return patched_table

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
