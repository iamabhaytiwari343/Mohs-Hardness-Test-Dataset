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

# Distribution plots using histograms
st.subheader("Distribution Plots")
for col in selected_columns:
    fig, ax = plt.subplots()
    ax.hist(data[col])
    ax.set_title(f"Distribution of {col}")
    ax.set_xlabel(col)
    ax.set_ylabel("Count")
    st.pyplot(fig)

# Line plot (example) - explore other plot types based on your data
st.subheader("Line Plot (Example)")
fig, ax = plt.subplots()
ax.plot(data["Hardness"], data["ionenergy_Average"])  # Replace with relevant columns
ax.set_title("Hardness vs Ionization Energy")
ax.set_xlabel("Hardness")
ax.set_ylabel("Ionization Energy")
st.pyplot(fig)

# Donut chart - explore other chart types for categorical data if applicable
if data["Hardness"].dtype == object:  # Check if Hardness is categorical
    st.subheader("Hardness Distribution")
    fig, ax = plt.subplots()
    ax.pie(data["Hardness"].value_counts(), labels=data["Hardness"].unique(), autopct="%1.1f%%")
    ax.set_title("Hardness Distribution")
    st.pyplot(fig)

# Additional analysis based on your interests
# - Explore relationships between Mohs hardness and other features
# - Filter data by hardness range
# - Use color-coding to highlight trends

# Add a sidebar for filtering by hardness range
with st.sidebar:
    min_hardness = st.number_input("Minimum Hardness", min(data["Hardness"]), max(data["Hardness"]), value=min(data["Hardness"]))
    max_hardness = st.number_input("Maximum Hardness", min(data["Hardness"]), max(data["Hardness"]), value=max(data["Hardness"]))
    filtered_data = data.query("Hardness >= @min_hardness & Hardness <= @max_hardness")  # Filter data using pandas query

# Use the filtered data for plots and analysis after this point
# Feature selection for relationship exploration
selected_feature = st.selectbox(
    "Select a feature to explore with Hardness",
    data.columns[:-1],  # Exclude target variable
)

# Create a dropdown menu for selecting calculation methods
calculation_method = st.selectbox(
    "Select calculation method", ["Average", "Median"]
)

if calculation_method == "Average":
    grouped_data = data.groupby(selected_feature)["Hardness"].mean().reset_index()
elif calculation_method == "Median":
    grouped_data = data.groupby(selected_feature)["Hardness"].median().reset_index()
else:
    st.error("Calculation method not supported")
    # Handle unsupported calculation methods

# Line plot to visualize the relationship
fig, ax = plt.subplots()
ax.plot(grouped_data[selected_feature], grouped_data["Hardness"])
ax.set_title(f"{calculation_method} Hardness by {selected_feature}")
ax.set_xlabel(selected_feature)
ax.set_ylabel("Hardness")
st.pyplot(fig)

# Additional exploration based on the chosen method (e.g., boxplots for medians)
if calculation_method == "Median":
    st.subheader("Hardness Distribution by Feature")
    fig, ax = plt.subplots()
    ax.boxplot(data.groupby(selected_feature)["Hardness"], notch=True)
    ax.set_title(f"Hardness Distribution by {selected_feature}")
    ax.set_xlabel(selected_feature)
    ax.set_ylabel("Hardness")
    st.pyplot(fig)

# Feature selection for relationship exploration with color-coding
selected_feature = st.selectbox(
    "Select a feature to explore with Hardness",
    data.columns[:-1],  # Exclude target variable
)

# Select feature for color-coding (optional)
color_by_feature = st.selectbox(
    "Select feature for color-coding (optional)", data.columns[:-1], key="color_coding"
)  # Unique key to avoid overwriting selection

# Scatter plot with color-coding
fig, ax = plt.subplots()
if color_by_feature:
    for value in data[color_by_feature].unique():
        subset = data.query(f"{color_by_feature} == @value")
        ax.scatter(subset[selected_feature], subset["Hardness"], label=value)
    ax.legend(title=color_by_feature)
else:
    ax.scatter(data[selected_feature], data["Hardness"])
ax.set_title(f"Hardness vs {selected_feature}")
ax.set_xlabel(selected_feature)
ax.set_ylabel("Hardness")
st.pyplot(fig)
