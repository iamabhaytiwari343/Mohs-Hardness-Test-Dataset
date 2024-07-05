import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load your data from CSV
data = pd.read_csv("Dataset/train.csv")  # Replace with your filename 

# Streamlit app configuration (optional)
st.set_page_config(
    page_title="Mohs Hardness Data Dashboard",
    page_icon=":hammer:",
)

# Display title
st.title("Mohs Hardness Test Data")

# Select columns for exploration (optional)
selected_columns = st.multiselect(
    "Select features to explore:", data.columns[:-1], default=["allelectrons_Average", "density_Average"]  # Exclude target variable
)

# Correlation heatmap
fig, ax = plt.subplots()
correlation = data[selected_columns].corr()
ax.imshow(correlation, cmap="coolwarm")
ax.set_title("Correlation Heatmap")
ax.set_xticks(range(len(correlation.columns)))
ax.set_yticks(range(len(correlation.columns)))
ax.set_xticklabels(correlation.columns, rotation=45, ha="right")
ax.set_yticklabels(correlation.columns)
st.pyplot(fig)

# Scatter plots (consider using st.altair for more advanced charts)
st.subheader("Scatter Plots")
for col in selected_columns:
    fig, ax = plt.subplots()
    ax.scatter(data["Hardness"], data[col])
    ax.set_title(f"Hardness vs {col}")
    ax.set_xlabel("Hardness")
    ax.set_ylabel(col)
    st.pyplot(fig)

# Additional analysis based on your interests
# - Explore relationships between Mohs hardness and other features
# - Filter data by hardness range
# - Use color-coding to highlight trends

