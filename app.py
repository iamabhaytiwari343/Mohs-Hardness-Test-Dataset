import streamlit as st

# Define pages
def home():
    st.title("Home")
    st.write("Welcome to the home page of the data dashboard!")

def data_page():
    st.title("Data Page")
    st.write("This is the data page where you can explore various datasets.")

def analysis_page():
    st.title("Analysis Page")
    st.write("This is the analysis page where you can view data analyses.")

# Define a function to display the header
def display_header():
    st.markdown("""
    <div style="background-color:lightblue; padding:10px">
    <h1 style="color:black; text-align:center;">Data Dashboard</h1>
    </div>
    """, unsafe_allow_html=True)
def display_footer():
    st.markdown("""
    <div style="background-color:lightblue; padding:10px; position:fixed; bottom:0; width:100%">
    <p style="color:black; text-align:center;">&copy; 2024 Data Dashboard</p>
    </div>
    """, unsafe_allow_html=True)

# Main app function
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Data Page", "Analysis Page"])

    # Display header
    display_header()

    # Display selected page
    if page == "Home":
        home()
    elif page == "Data Page":
        data_page()
    elif page == "Analysis Page":
        analysis_page()

    # Display footer
    display_footer()

if __name__ == "__main__":
    main()
