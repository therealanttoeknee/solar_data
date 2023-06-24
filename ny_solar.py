import pandas as pd

import streamlit as st

import matplotlib.pyplot as plt

import plotly.express as px

import numpy as np

data = pd.read_csv("ny_solar.csv", low_memory = False)

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

unique_counties = pd.DataFrame(data['County'].unique(), columns = ['unique_county'])

#Reorganizes the column in alphabetical order
unique_counties = unique_counties.sort_values(by='unique_county', ascending=True)


#sidebar
st.sidebar.header("Welcome! :-) ")

with st.sidebar:
  selected_county = st.selectbox('Please select a county in New York State',
                  unique_counties)

# Count the occurrences of each unique value in the column for that specific county
value_counts = data[data['County'] == selected_county]['County'].value_counts()

filter = data[data['Estimated Annual PV Energy Production (kWh)'] == selected_county]['Estimated Annual PV Energy Production (kWh)'].value_counts()

# Remove commas from values and convert to numeric type
#data['Estimated Annual PV Energy Production (kWh)'] = pd.to_numeric(data['Estimated Annual PV Energy Production (kWh)'].str.replace(',', ''), errors='coerce')                                                                    

# Calculate the sum of the values
#total_sum = data['Estimated Annual PV Energy Production (kWh)'].sum()

#conversion = total_sum / 10 ** 6

st.markdown('Metrics')
col1, col2, col3 = st.columns(3)
col1.metric("The number of projects", value_counts)
col2.metric("Estimated Annual Production", filter)





















