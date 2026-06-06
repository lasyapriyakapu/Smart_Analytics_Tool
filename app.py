import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Smart Analytics Tool",
    layout="wide"
)
st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #FFF8E1,
        #FFE0B2,
        #FFD180
    );
}


h1 {
    text-align: center;
    color: #6A0DAD;
}

[data-testid="stMetric"] {
    background-color: white;
    padding: 15px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
}

[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #FF9800,
        #FFC107
    );
}
[data-testid="stSidebar"] * {
    color: white !important;
}
@keyframes pulse {
    0% {transform: scale(1);}
    50% {transform: scale(1.05);}
    100% {transform: scale(1);}
}

</style>
""", unsafe_allow_html=True)






st.sidebar.title("📊 Analytics Menu")
st.markdown("""
<h1 style='text-align:center;
color:#FF6F00;
animation: pulse 2s infinite;'>
Smart Analytics Tool
</h1>
""", unsafe_allow_html=True)
st.markdown("""
<div style="
padding:20px;
border-radius:20px;
background:linear-gradient(90deg,#FF9800,#FFC107);
color:black;
text-align:center;
font-size:24px;
font-weight:bold;">
🚀 Upload Any CSV and Get Instant Insights
</div>
""", unsafe_allow_html=True)

st.sidebar.info(
    """
    Upload any CSV file and instantly:
    
    ✅ Preview Dataset
    
    ✅ Analyze Missing Values
    
    ✅ View Statistics
    
    ✅ Generate Interactive Charts
    """
)


st.write("Upload a CSV file and analyze your data instantly.")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")

    st.dataframe(df.head())

    st.subheader("Dataset Shape")

    col1, col2 = st.columns(2)

    col1.metric("Rows", df.shape[0])

    col2.metric("Columns", df.shape[1])
    st.subheader("Missing Value Analysis")

    missing_values = df.isnull().sum()

    st.dataframe(
    missing_values[missing_values > 0])
    st.subheader("Statistical Summary")

    st.dataframe(df.describe())
    numeric_cols = df.select_dtypes(
    include="number"
    ).columns
    st.subheader("Histogram")

    selected_col = st.selectbox(
        "Select Numeric Column",
        numeric_cols
    )

    fig = px.histogram(
    df,
    x=selected_col,
    color_discrete_sequence=["#6C63FF"]
    )

    fig.update_layout(
    title=f"Distribution of {selected_col}",
    template="plotly_white"
    )

    st.plotly_chart(fig)
    st.subheader("Box Plot")

    selected_box = st.selectbox(
        "Select Column for Box Plot",
        numeric_cols,
        key="box"
    )

    fig2 = px.box(
        df,
        y=selected_box,
        color_discrete_sequence=["#FF4DA6"]
    )

    fig2.update_layout(
        title=f"Box Plot of {selected_box}",
        template="plotly_white"
    )

    st.plotly_chart(fig2)
    st.subheader("Scatter Plot")

    x_col = st.selectbox(
        "Select X-Axis",
        numeric_cols,
        key="x"
    )

    y_col = st.selectbox(
        "Select Y-Axis",
        numeric_cols,
        key="y"
    )

    fig3 = px.scatter(
        df,
        x=x_col,
        y=y_col,
        color_discrete_sequence=["#00C853"]
    )

    fig3.update_layout(
        title=f"{x_col} vs {y_col}",
        template="plotly_white"
    )

    st.plotly_chart(fig3)