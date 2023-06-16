import pandas as pd

import streamlit as st

import plotly as pt

data = pd.read_csv("/Users/anthony/Desktop/NY_SOLAR.csv")

st.set_page_config(layout='wide', initial_sidebar_state='expanded')
