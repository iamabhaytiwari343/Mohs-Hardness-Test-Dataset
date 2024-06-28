import streamlit as st
import pandas as pd
import plotly.express as px

train=pd.read_csv('Dataset/train.csv')
test=pd.read_csv('Dataset/test.csv')

st.title('Mohs Hardness Test')
st.write('Explore the relationships between various material properties.')
col1 , col2 = st.columns(2)

# Example dropdown for feature selection
selected_feature = st.selectbox("Select a Feature:", train.columns[:-1])

# Example radio buttons for chart selection
chart_type = st.radio("Choose Chart Type:", ("Scatter Plot", "Histogram"))

# Filter data based on selected feature
filtered_data = data[["id", selected_feature, "Hardness"]]

# Example chart creation using Plotly Express
if chart_type == "Scatter Plot":
    fig = px.scatter(filtered_data, x=selected_feature, y="Hardness")
elif chart_type == "Histogram":
    fig = px.histogram(filtered_data, x=selected_feature)

st.plotly_chart(fig)
