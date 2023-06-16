import pandas as pd

import streamlit as st

data = pd.read_csv("ny_solar.csv")

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

st.markdown('Metrics')
col1, col2, col3 = st.columns(3)
col1.metric("The number of projects", data['Project ID'].count())
col2.metric("Most popular area", data['Zip'].value_counts.idmax())
