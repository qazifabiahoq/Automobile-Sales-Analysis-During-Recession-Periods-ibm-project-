#!/usr/bin/env python
# coding: utf-8

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

# Load the data using pandas
data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv')

# Initialize the Dash app
app = dash.Dash(__name__)

# ---------------------------------------------------------------------------------
# Create the dropdown menu options
dropdown_options = [
    {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
    {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
]
# List of years
year_list = [i for i in range(1980, 2024, 1)]
# ---------------------------------------------------------------------------------------

# Create the layout of the app
app.layout = html.Div([
    # TASK 2.1: Add title to the dashboard
    html.H1(
        "Automobile Sales Statistics Dashboard", 
        style={'textAlign': 'center', 'color': '#503D36', 'font-size': '24px'}
    ),
    
    # TASK 2.2: Add two dropdown menus
    html.Div([
        # Dropdown for selecting report type
        html.Label("Select Report Type:", style={'font-size': '18px', 'color': '#503D36'}),
        dcc.Dropdown(
            id='dropdown-statistics', 
            options=dropdown_options,
            value='Select Statistics',
            placeholder='Select a report type',
            style={'width': '80%', 'padding': '3px', 'font-size': '20px', 'text-align-last': 'center'}
        )
    ]),
    
    html.Div([
        # Dropdown for selecting year
        html.Label("Select Year:", style={'font-size': '18px', 'color': '#503D36'}),
        dcc.Dropdown(
            id='select-year',
            options=[{'label': str(i), 'value': i} for i in year_list],
            value='Select Year',
            placeholder='Select Year',
            style={'width': '80%', 'padding': '3px', 'font-size': '20px', 'text-align-last': 'center'}
        )
    ]),
    
    # TASK 2.3: Add a division for output display
    html.Div([
        html.Div(
            id='output-container', 
            className='chart-grid', 
            style={'display': 'flex', 'height': '200px', 'border': '2px solid #503D36', 'padding': '10px'},
            children=[html.H3("Output will be displayed here", style={'textAlign': 'center'})]
        )
    ])
])
# 2.4  Callback
@app.callback(
    Output(component_id='output-container', component_property='children'),
    [Input(component_id='dropdown-statistics', component_property='value'), 
     Input(component_id='select-year', component_property='value')]
)
def update_output_container(selected_statistics, selected_year):
    if selected_statistics == 'Recession Period Statistics':
        # Recession Period Statistics code remains unchanged
        recession_data = data[data['Recession'] == 1]
        total_sales = recession_data['Automobile_Sales'].sum()

        # Plot 1: Automobile sales fluctuate over Recession Period (year wise) using line chart
        yearly_rec = recession_data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        R_chart1 = dcc.Graph(
            figure=px.line(yearly_rec, 
                x='Year', 
                y='Automobile_Sales',
                title="Automobile Sales Over Recession Period"
            )
        )

        # Plot 2: Average number of vehicles sold by vehicle type (Bar chart)
        average_sales = recession_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        R_chart2 = dcc.Graph(
            figure=px.bar(average_sales,
                x='Vehicle_Type',
                y='Automobile_Sales',
                title="Average Vehicle Sales by Vehicle Type"
            )
        )

        # Plot 3: Pie chart for total expenditure share by vehicle type during recessions
        exp_rec = recession_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        R_chart3 = dcc.Graph(
            figure=px.pie(exp_rec,
                values='Advertising_Expenditure',
                names='Vehicle_Type',
                title="Expenditure Share by Vehicle Type During Recession"
            )
        )

        # Plot 4: Bar chart for the effect of unemployment rate on vehicle type and sales
        unemp_data = recession_data.groupby(['unemployment_rate', 'Vehicle_Type'])['Automobile_Sales'].mean().reset_index()
        R_chart4 = dcc.Graph(
            figure=px.bar(unemp_data,
                x='unemployment_rate',  # Ensure this matches the column name exactly
                y='Automobile_Sales',
                color='Vehicle_Type',
                labels={'unemployment_rate': 'Unemployment Rate', 'Automobile_Sales': 'Average Automobile Sales'},
                title="Effect of Unemployment Rate on Vehicle Type and Sales"
            )
        )

        return [
            html.Div(className='chart-item', children=[
                html.Div(children=R_chart1, style={'flex': '50%', 'padding': '10px'}),
                html.Div(children=R_chart2, style={'flex': '50%', 'padding': '10px'})
            ], style={'display': 'flex', 'flexWrap': 'wrap'}),
            html.Div(className='chart-item', children=[
                html.Div(children=R_chart3, style={'flex': '50%', 'padding': '10px'}),
                html.Div(children=R_chart4, style={'flex': '50%', 'padding': '10px'})
            ], style={'display': 'flex', 'flexWrap': 'wrap'})
        ]

    elif selected_statistics == 'Yearly Statistics' and selected_year != 'Select Year':
        # Yearly Statistics code for the selected year
        yearly_data = data[data['Year'] == selected_year]

        # Plot 1: Yearly Automobile sales using line chart for the whole period.
        yas = data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        Y_chart1 = dcc.Graph(
            figure=px.line(yas, 
                x='Year', 
                y='Automobile_Sales',
                title="Yearly Automobile Sales"
            )
        )

        # Plot 2: Total Monthly Automobile sales using line chart.
        mas = data.groupby('Month')['Automobile_Sales'].sum().reset_index()
        Y_chart2 = dcc.Graph(
            figure=px.line(mas,
                x='Month',
                y='Automobile_Sales',
                title='Total Monthly Automobile Sales'
            )
        )

        # Plot 3: Average number of vehicles sold during the selected year by vehicle type
        avr_vdata = yearly_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        Y_chart3 = dcc.Graph(
            figure=px.bar(avr_vdata,
                x='Vehicle_Type',
                y='Automobile_Sales',
                title=f'Average Vehicles Sold by Vehicle Type in the Year {selected_year}'
            )
        )

        # Plot 4: Total Advertisement Expenditure for each vehicle using pie chart
        exp_data = yearly_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        Y_chart4 = dcc.Graph(
            figure=px.pie(exp_data, 
                values='Advertising_Expenditure',
                names='Vehicle_Type',
                title='Total Advertisement Expenditure for Each Vehicle'
            )
        )

        return [
            html.Div(className='chart-item', children=[
                html.Div(children=Y_chart1, style={'flex': '50%', 'padding': '10px'}),
                html.Div(children=Y_chart2, style={'flex': '50%', 'padding': '10px'})
            ], style={'display': 'flex', 'flexWrap': 'wrap'}),
            html.Div(className='chart-item', children=[
                html.Div(children=Y_chart3, style={'flex': '50%', 'padding': '10px'}),
                html.Div(children=Y_chart4, style={'flex': '50%', 'padding': '10px'})
            ], style={'display': 'flex', 'flexWrap': 'wrap'})
        ]

    else:
        return html.Div([html.H3("Please select valid inputs", style={'textAlign': 'center'})])


# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
