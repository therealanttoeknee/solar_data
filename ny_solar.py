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

# subset the data frame to select "selected_county" and each kW-DC value 
subsetoooor = data[data['County'] == selected_county][['County', 'Estimated Annual PV Energy Production (kWh)']]

subsetoooor['Estimated Annual PV Energy Production (kWh)'] = subsetoooor['Estimated Annual PV Energy Production (kWh)'].str.replace(',', '').astype(float)

sum_est_ann_pv_prod = subsetoooor['Estimated Annual PV Energy Production (kWh)'].sum()

convert_sum = sum_est_ann_pv_prod / 10 ** 6 

st.markdown('Metrics')
col1, col2, col3 = st.columns(3)
col1.metric("The number of projects", value_counts)
col2.metric("Estimated Annual Production (GWh)", convert_sum)





















