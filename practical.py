# import streamlit as st
# # st.write("Worldwide Analysis of Quality of Life and Economic Factors")

# # Set page to use full width
# st.set_page_config(layout="wide")

# # Headline
# st.header("Worldwide Analysis of Quality of Life and Economic Factors")

# # Subtitle
# st.subheader(
#     "This app enables you to explore the relationships between poverty, "
#     "life expectancy, and GDP across various countries and years. "
#     "Use the panels to select options and interact with the data."
# )

# # Create tabs
# tab1, tab2, tab3 = st.tabs(["Global Overview", "Country Deep Dive", "Data Explorer"])

# with tab1:
#     st.write("### Global Overview Section")
#     st.write("Content for global overview will go here...")

# with tab2:
#     st.write("### Country Deep Dive Section")
#     st.write("Content for country-specific analysis will go here...")

# with tab3:
#     st.write("### Data Explorer Section")
#     st.write("Content for exploring raw data will go here...")

#############################################################
#############################################################
import streamlit as st

# Set page to use full width
st.set_page_config(layout="wide")

# Headline
st.header("Worldwide Analysis of Quality of Life and Economic Factors")

# Subtitle
st.subheader(
    "This app enables you to explore the relationships between poverty, "
    "life expectancy, and GDP across various countries and years. "
    "Use the panels to select options and interact with the data."
)

# Create tabs
tab1, tab2, tab3 = st.tabs(["Global Overview", "Country Deep Dive", "Data Explorer"])

# --- Global Overview ---
with tab1:
    st.write("### 🌍 Global Overview")

    # Year selector
    year = st.slider("Select Year", min_value=1960, max_value=2023, value=2000, step=1)

    # Metric selector
    metric = st.selectbox(
        "Choose a metric to visualize",
        ["GDP per capita", "Life Expectancy", "Poverty Rate"]
    )

    st.write(f"You selected **{metric}** for the year **{year}**.")
    # Placeholder for charts/plots
    st.info("Global overview chart will be displayed here.")


# --- Country Deep Dive ---
with tab2:
    st.write("### 🏳️ Country Deep Dive")

    # Country selector
    country = st.selectbox(
        "Select a country",
        ["United States", "India", "China", "Brazil", "Germany", "Nigeria"]
    )

    # Metric selector
    metric = st.radio(
        "Choose metric to analyze",
        ["GDP per capita", "Life Expectancy", "Poverty Rate"]
    )

    st.write(f"You are exploring **{metric}** for **{country}**.")
    st.info("Country-specific time-series chart will be displayed here.")


# --- Data Explorer ---
with tab3:
    st.write("### 📊 Data Explorer")

    # Columns to display
    columns = st.multiselect(
        "Select columns to display in the data table",
        ["Country", "Year", "GDP per capita", "Life Expectancy", "Poverty Rate"],
        default=["Country", "Year", "GDP per capita"]
    )

    # Number of rows
    n_rows = st.slider("Number of rows to display", min_value=5, max_value=50, value=10)

    st.write(f"Showing first {n_rows} rows with columns {columns}")
    st.info("Interactive data table will be displayed here.")
