import pandas as pd

import streamlit as st

data = pd.read_csv("ny_solar.csv", low_memory = False)

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

# Count the occurrences of each unique value in the column
value_counts = data['Zip'].value_counts()

# Find the value that repeats the most number of times
most_common_value = value_counts.idxmax()

# Sum of the annual PV energy production (GWh)
sum_annual_prod = (data['Estimated Annual PV Energy Production (kWh)'].sum())) / 10**6


st.markdown('Metrics')
col1, col2, col3 = st.columns(3)
col1.metric("The number of projects", data['Project ID'].count())
col2.metric("Most popular area", int(most_common_value))
col3.metric("Total Annual Production (GWH)", sum_annual_prod)

