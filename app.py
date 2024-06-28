import streamlit as st
import pandas as pd
import plotly.express as px

train=pd.read_csv('Dataset/train.csv')
test=pd.read_csv('Dataset/test.csv')

st.title('Mohs Hardness Test')
st.write('Explore the relationships between various material properties.')
col1 , col2 = st.columns(2)

# Example dropdown for feature selection
selected_feature = st.selectbox("Select a Feature:", data.columns[:-1])

# Example radio buttons for chart selection
chart_type = st.radio("Choose Chart Type:", ("Scatter Plot", "Histogram"))