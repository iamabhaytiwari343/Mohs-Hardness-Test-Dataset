import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('Dataset/train.csv')

# Set Streamlit page configuration
st.set_page_config(page_title="Mohs Hardness Test Dashboard", layout="wide")

# Summary Statistics
st.title("Mohs Hardness Test Dashboard")

st.header("Summary Statistics")
st.write("Total Number of Entries: ", df.shape[0])
st.write("Average Hardness: ", df['Hardness'].mean())
st.write("Hardness Range: ", df['Hardness'].min(), " - ", df['Hardness'].max())
st.write("Average Density (Total): ", df['density_Total'].mean())
st.write("Average Atomic Weight: ", df['atomicweight_Average'].mean())

# Data Visualizations
st.header("Data Visualizations")

# Bar Chart of Hardness Values
st.subheader("Bar Chart of Hardness Values")
fig, ax = plt.subplots()
df.sort_values(by='Hardness', inplace=True)
ax.bar(df['id'], df['Hardness'])
ax.set_xlabel('ID')
ax.set_ylabel('Hardness')
ax.set_title('Hardness Values by ID')
st.pyplot(fig)

# Scatter Plot of Hardness vs. Density Total
st.subheader("Scatter Plot of Hardness vs. Density (Total)")
fig, ax = plt.subplots()
ax.scatter(df['density_Total'], df['Hardness'])
ax.set_xlabel('Density (Total)')
ax.set_ylabel('Hardness')
ax.set_title('Hardness vs. Density (Total)')
st.pyplot(fig)

# Correlation Heatmap
st.subheader("Correlation Heatmap")
fig, ax = plt.subplots()
corr = df.corr()
sns.heatmap(corr, annot=True, ax=ax, cmap='coolwarm')
ax.set_title('Correlation Heatmap')
st.pyplot(fig)

# Interactive Filters
st.header("Interactive Filters")

# Hardness Range Slider
hardness_range = st.slider('Select Hardness Range', float(df['Hardness'].min()), float(df['Hardness'].max()), (float(df['Hardness'].min()), float(df['Hardness'].max())))
filtered_df = df[(df['Hardness'] >= hardness_range[0]) & (df['Hardness'] <= hardness_range[1])]

st.write(f"Filtered Data (Hardness Range: {hardness_range[0]} - {hardness_range[1]})")
st.write(filtered_df)

# Entry Details
st.header("Entry Details")

# Select Entry by ID
selected_id = st.selectbox('Select Entry by ID', df['id'].unique())
entry_details = df[df['id'] == selected_id]

st.write(f"Details of Entry ID: {selected_id}")
st.write(entry_details)
