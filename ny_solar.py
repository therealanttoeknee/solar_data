import pandas as pd

import streamlit as st

import matplotlib.pyplot as plt

import plotly.express as px

data = pd.read_csv("ny_solar.csv", low_memory = False)

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

# Count the occurrences of each unique value in the column
value_counts = data['Zip'].value_counts()

# Find the value that repeats the most number of times
most_common_value = value_counts.idxmax()

# Remove commas from values and convert to numeric type
data['Estimated Annual PV Energy Production (kWh)'] = pd.to_numeric(data['Estimated Annual PV Energy Production (kWh)'].str.replace(',', ''), errors='coerce')

# Calculate the sum of the values
total_sum = data['Estimated Annual PV Energy Production (kWh)'].sum()

conversion = total_sum / 10 ** 6

st.markdown('Metrics')
col1, col2, col3 = st.columns(3)
col1.metric("The number of projects", data['Project ID'].count())
col2.metric("Zip code with the most number of installations", int(most_common_value))
col3.metric("Estimated annual production (GWh)", round(conversion))

# Display the bar chart
st.bar_chart(data['Interconnection Date'])




















