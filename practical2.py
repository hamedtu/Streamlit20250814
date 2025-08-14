import streamlit as st
import plotly.express as px
import pandas as pd
from io import BytesIO

# Load sample dataset
df = px.data.gapminder()

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
    year = st.slider("Select Year", min_value=int(df["year"].min()), max_value=int(df["year"].max()), value=2000, step=5)

    # Metric selector
    metric = st.selectbox(
        "Choose a metric to visualize",
        ["GDP per capita", "Life Expectancy", "Population"]
    )

    # Map metric names to dataframe columns
    metric_map = {
        "GDP per capita": "gdpPercap",
        "Life Expectancy": "lifeExp",
        "Population": "pop"
    }

    filtered = df[df["year"] == year]

    fig = px.scatter_geo(
        filtered,
        locations="iso_alpha",
        color=metric_map[metric],
        hover_name="country",
        size=metric_map[metric],
        projection="natural earth",
        title=f"{metric} in {year}"
    )
    st.plotly_chart(fig, use_container_width=True)


# --- Country Deep Dive ---
with tab2:
    st.write("### 🏳️ Country Deep Dive")

    # Country selector
    country = st.selectbox("Select a country", sorted(df["country"].unique()))

    # Metric selector
    metric = st.radio("Choose metric to analyze", ["GDP per capita", "Life Expectancy", "Population"])

    filtered = df[df["country"] == country]

    fig = px.line(
        filtered,
        x="year",
        y=metric_map[metric],
        markers=True,
        title=f"{metric} trend for {country}"
    )
    st.plotly_chart(fig, use_container_width=True)


# --- Data Explorer ---
with tab3:
    st.write("### 📊 Data Explorer")

    # Columns to display
    columns = st.multiselect(
        "Select columns to display in the data table",
        options=list(df.columns),
        default=["country", "year", "gdpPercap", "lifeExp", "pop"]
    )

    # Number of rows
    n_rows = st.slider("Number of rows to display", min_value=5, max_value=50, value=10)

    filtered_df = df[columns].head(n_rows)
    st.dataframe(filtered_df, use_container_width=True)

    # --- Download Buttons ---
    csv = filtered_df.to_csv(index=False).encode("utf-8")

    # For Excel we need a buffer
    excel_buffer = BytesIO()
    with pd.ExcelWriter(excel_buffer, engine="xlsxwriter") as writer:
        filtered_df.to_excel(writer, index=False, sheet_name="Data")
    excel_data = excel_buffer.getvalue()

    st.download_button(
        label="⬇️ Download CSV",
        data=csv,
        file_name="data_explorer.csv",
        mime="text/csv"
    )

    st.download_button(
        label="⬇️ Download Excel",
        data=excel_data,
        file_name="data_explorer.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

###########################################################
##########################################################
# import streamlit as st
# import pandas as pd
# import plotly.express as px
# from io import BytesIO

# # URL of the merged dataset
# data_url = "https://raw.githubusercontent.com/JohannaViktor/streamlit_practical/refs/heads/main/global_development_data.csv"

# # Read dataset
# @st.cache_data
# def load_data():
#     return pd.read_csv(data_url)

# df = load_data()

# # --- Tab 3: Data Explorer ---
# with tab3:
#     st.write("### 📊 Data Explorer (Global Development Data)")

#     # Show the full dataset (first few rows)
#     st.write("#### Preview of the dataset")
#     st.dataframe(df.head(20), use_container_width=True)

#     # Country selector
#     countries = st.multiselect(
#         "Select countries",
#         options=sorted(df["country"].unique()),
#         default=["United States", "India", "China"]
#     )

#     # Year range slider
#     year_min, year_max = int(df["year"].min()), int(df["year"].max())
#     year_range = st.slider(
#         "Select year range",
#         min_value=year_min,
#         max_value=year_max,
#         value=(1990, 2010)
#     )

#     # Apply filters
#     filtered_df = df[
#         (df["country"].isin(countries)) &
#         (df["year"].between(year_range[0], year_range[1]))
#     ]

#     st.write(f"#### Filtered dataset ({len(filtered_df)} rows)")
#     st.dataframe(filtered_df, use_container_width=True)

#     # --- Visualization ---
#     st.write("#### 📈 Visualize Trends")

#     metric = st.selectbox(
#         "Select metric to visualize",
#         ["GDP per capita", "Life Expectancy", "Poverty Rate"]
#     )

#     # Map display names to dataset columns
#     metric_map = {
#         "GDP per capita": "gdp_per_capita",
#         "Life Expectancy": "life_expectancy",
#         "Poverty Rate": "poverty_rate"
#     }

#     if metric_map[metric] in filtered_df.columns:
#         fig = px.line(
#             filtered_df,
#             x="year",
#             y=metric_map[metric],
#             color="country",
#             markers=True,
#             title=f"{metric} over time ({year_range[0]}–{year_range[1]})"
#         )
#         st.plotly_chart(fig, use_container_width=True)
#     else:
#         st.warning(f"⚠️ The dataset does not contain '{metric}' column.")

#     # --- Download Buttons ---
#     csv = filtered_df.to_csv(index=False).encode("utf-8")

#     # Excel buffer
#     excel_buffer = BytesIO()
#     with pd.ExcelWriter(excel_buffer, engine="xlsxwriter") as writer:
#         filtered_df.to_excel(writer, index=False, sheet_name="Filtered Data")
#     excel_data = excel_buffer.getvalue()

#     st.download_button(
#         label="⬇️ Download CSV",
#         data=csv,
#         file_name="filtered_global_development_data.csv",
#         mime="text/csv"
#     )

#     st.download_button(
#         label="⬇️ Download Excel",
#         data=excel_data,
#         file_name="filtered_global_development_data.xlsx",
#         mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#     )
