# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    line_chart.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yel-hadd <yel-hadd@mail.com>               +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/04 19:28:06 by yel-hadd          #+#    #+#              #
#    Updated: 2023/05/04 19:28:06 by yel-hadd         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import streamlit as st
import plotly.graph_objs as go
import pandas as pd

# Load world population data from CSV file
df = pd.read_csv('dataset1.csv')

# Create a dropdown menu for the user to select a country
country_list = df['Country Name'].unique()
country_dropdown = st.selectbox('Select a country', country_list)

# Get the population data for the selected country
df_country = df.loc[df['Country Name'] == country_dropdown]

# Melt the data so that the years are stored in a single column
df_country = df_country.melt(id_vars=['Country Name', 'Country Code'], var_name='Year', value_name='Population')

# Create a Plotly figure object
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df_country['Year'],
    y=df_country['Population'],
    name=country_dropdown,
    mode='lines',
    line=dict(color='green', width=2)
))

fig.update_layout(
    title=f'{country_dropdown} Population Over Time',
    xaxis_title='Year',
    yaxis_title='Population'
)

# Show the chart
st.plotly_chart(fig)
