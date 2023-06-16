import pandas as pd

import streamlit as st

data = pd.read_csv("ny_solar.csv")

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

st.write("Hello")
