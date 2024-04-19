## Dashboard for weather API data  

#  

# import libraries
import pandas as pd 
import dash
from dash import Dash, dcc, html, callback
from dash.dependencies import Input, Output, State
import plotly.express as px
from dash import dash_table
import dash_bootstrap_components as dbc

# import data
data = pd.read_csv('./data/prep_data.csv')
#data.tail()

##------------------ Creating graphs ----------------------

# graph 1 - plot temperature
fig1 = px.line(data,
              x='date',
              y='avg_temp_c',
              color='city',
               labels = {
                   'date': 'Date',
                   'avg_temp_c': 'avg. temperature in °C',
                   'city': 'Cities'
               }
             )
    
fig1.show()

graph1 = dcc.Graph(figure=fig1)


# graph 2 - plot temperature
filtered_data = data[(data['date'] >= '2023-08-11') & (data['date'] <= '2023-08-24')]

fig2 = px.line(filtered_data,
              x='date',
              y='uv',
              color='city',
              labels = {
                   'date': 'Date',
                   'uv': 'UV',
                   'city': 'Cities'
               }
             )

fig2.show()

graph2 = dcc.Graph(figure=fig2)


# graph 3 - plot total_precip_mm
fig3 = px.line(filtered_data,
              x='date',
              y = 'total_precip_mm',
              color='city',
              labels = {
                   'date': 'Date',
                   'total_precip_mm': 'total rainfall in mm',
                   'city': 'Cities'
               }
             )
    
fig3.show()

graph3 = dcc.Graph(figure=fig3)

#----------------------Dashboard------------------------ 

# initializing app
app =dash.Dash(external_stylesheets=[dbc.themes.DARKLY])

# define the server
server = app.server

app.layout = html.Div([html.H1('Vacay Locater', style={'textAlign': 'center', 'color': '#636EFA'}), 
                       html.Div(html.P("Which location is best for hiking? Zermatt, Salzburg or Trondheim?"), 
                                 style={'textAlign': 'center', 'margin': '0 auto', 'width': '900px'}),
                       html.Div([html.Div('Average Temperature', 
                                 style={'textAlign': 'center', 'margin': '0 auto', 'width': '900px'}),
                                 graph1]),
                       html.Div([html.Div("August seems stable. Let's investigate further.", 
                                 style={'textAlign': 'center', 'margin': '0 auto', 'width': '900px'}),
                       html.Div("What about UV Radiation?", 
                                 style={'textAlign': 'center', 'margin': '0 auto', 'width': '900px'}),
                                 graph2
                                ]),
                       html.Div([html.Div("What about rainfall?", 
                                 style={'textAlign': 'center', 'margin': '0 auto', 'width': '900px'}),
                                 graph3,
                       html.H2("Zermatt seems to be the best option!", 
                                 style={'textAlign': 'center', 'margin': '0 auto', 'width': '900px'}),                                
                                ])
])

if __name__ == '__main__':
     app.run_server()