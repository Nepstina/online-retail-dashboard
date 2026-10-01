import os
import pandas as pd
import streamlit as st
import plotly.express as px
st.set_page_config(page_title="Retail Revenue Dashboard", layout="wide")
st.title(r"?? Online Retail Revenue Dashboard")
st.markdown(r"Automated e-commerce insights powered by Python")
data_path = "cleaned_retail_data.csv"
if os.path.exists(data_path):
    df = pd.read_csv(data_path)
    total_revenue = df['TotalSales'].sum()
    total_orders = df['InvoiceNo'].nunique()
    avg_order_value = total_revenue / total_orders if total_orders > 0 else 0
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Total Revenue", value=f"${total_revenue:,.2f}")
    col2.metric(label="Total Orders", value=f"{total_orders}")
    col3.metric(label="Avg Order Value", value=f"${avg_order_value:,.2f}")
    st.markdown("---")
    left_col, right_col = st.columns(2)
    with left_col:
        st.subheader("Sales by Product")
        fig_prod = px.bar(df, x='Description', y='TotalSales', title="Product Revenue", color='TotalSales', color_continuous_scale='Blues')
        st.plotly_chart(fig_prod, width='stretch')
    with right_col:
        st.subheader("Sales by Country")
        fig_geo = px.pie(df, values='TotalSales', names='Country', title="Revenue Share", hole=0.4)
        st.plotly_chart(fig_geo, width='stretch')
else:
    st.error(r"? Cleaned data file not found. Run clean_data.py first!")
