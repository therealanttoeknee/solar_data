import pandas as pd

import streamlit as st

data = pd.read_csv("ny_solar.csv")

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

# Count the occurrences of each unique value in the column
value_counts = data['Zip'].value_counts()

# Find the value that repeats the most number of times
most_common_value = value_counts.idxmax()

# Count of the most common value
count_most_common_value = value_counts.loc[most_common_value]

st.markdown('Metrics')
col1, col2, col3 = st.columns(3)
col1.metric("The number of projects", data['Project ID'].count())
col2.metric("Most popular area", count_most_common_value)
