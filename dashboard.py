
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(layout="wide")

def load_data():
    df = pd.read_excel(r"C:\Users\Liz\Jipange _project\data\jipange_dataset_cleaned.xlsx")
    return df

df = load_data()

st.sidebar.header("Loan Portfolio Filters")

age_filter = st.sidebar.slider('Borrower Age', 18, 35, (18, 35))
loan_filter = st.sidebar.slider('Loan Amount (KSh)', 5000, 50000, (5000, 50000), 1000)
business_filter = st.sidebar.multiselect('Business Type', df['Business_Type'].unique(), df['Business_Type'].unique())
status_filter = st.sidebar.multiselect('Repayment Status', df['Repayment_Status'].unique(), df['Repayment_Status'].unique())
year_filter = st.sidebar.multiselect('Loan Year', sorted(df['Loan_Year'].unique()), sorted(df['Loan_Year'].unique()))

filtered_df = df[
    (df['Age'] >= age_filter[0]) & (df['Age'] <= age_filter[1]) &
    (df['Loan_Amount'] >= loan_filter[0]) & (df['Loan_Amount'] <= loan_filter[1]) &
    (df['Business_Type'].isin(business_filter)) &
    (df['Repayment_Status'].isin(status_filter)) &
    (df['Loan_Year'].isin(year_filter))
]

total_loans = len(filtered_df)
default_count = (filtered_df['Repayment_Status'] == 'Default').sum()
default_rate = (default_count / total_loans) * 100 if total_loans > 0 else 0
on_time_count = (filtered_df['Repayment_Status'] == 'On-time').sum()
on_time_rate = (on_time_count / total_loans) * 100 if total_loans > 0 else 0
late_count = (filtered_df['Repayment_Status'] == 'Late').sum()
late_rate = (late_count / total_loans) * 100 if total_loans > 0 else 0
avg_loan = filtered_df['Loan_Amount'].mean()
total_value = filtered_df['Loan_Amount'].sum()

loan_size_analysis = filtered_df.groupby(
    pd.cut(filtered_df['Loan_Amount'], [5000, 15000, 30000, 50000], 
           labels=['Small (5K-15K)', 'Medium (15K-30K)', 'Large (30K-50K)']),
    observed=False
).agg({
    'Repayment_Status': lambda x: (x == 'Default').mean() * 100,
    'Borrower_ID': 'count'
}).round(1).rename(columns={'Borrower_ID': 'Count'})

if not loan_size_analysis.empty:
    worst_loan_size = loan_size_analysis['Repayment_Status'].idxmax()
    worst_loan_rate = loan_size_analysis['Repayment_Status'].max()
    best_loan_size = loan_size_analysis['Repayment_Status'].idxmin()
    best_loan_rate = loan_size_analysis['Repayment_Status'].min()
else:
    worst_loan_size = "N/A"
    worst_loan_rate = 0
    best_loan_size = "N/A"
    best_loan_rate = 0

age_analysis_individual = filtered_df.groupby('Age', observed=False).agg({
    'Repayment_Status': lambda x: (x == 'Default').mean() * 100,
    'Loan_Amount': 'mean',
    'Borrower_ID': 'count'
}).round(1).rename(columns={'Borrower_ID': 'Count', 'Loan_Amount': 'Avg_Loan'})

if not age_analysis_individual.empty:
    valid_ages = age_analysis_individual[age_analysis_individual['Count'] > 0]
    if not valid_ages.empty:
        worst_age = valid_ages['Repayment_Status'].idxmax()
        worst_age_rate = valid_ages['Repayment_Status'].max()
        best_age = valid_ages['Repayment_Status'].idxmin()
        best_age_rate = valid_ages['Repayment_Status'].min()
    else:
        worst_age = "N/A"
        worst_age_rate = 0
        best_age = "N/A"
        best_age_rate = 0
else:
    worst_age = "N/A"
    worst_age_rate = 0
    best_age = "N/A"
    best_age_rate = 0

year_analysis = filtered_df.groupby('Loan_Year', observed=False).agg({
    'Repayment_Status': lambda x: (x == 'Default').mean() * 100,
    'Loan_Amount': 'mean',
    'Borrower_ID': 'count'
}).round(1).rename(columns={'Borrower_ID': 'Count', 'Loan_Amount': 'Avg_Loan'})

business_analysis = filtered_df.groupby('Business_Type', observed=False).agg({
    'Repayment_Status': lambda x: (x == 'Default').mean() * 100,
    'Loan_Amount': 'mean',
    'Borrower_ID': 'count'
}).round(1).rename(columns={'Borrower_ID': 'Count', 'Loan_Amount': 'Avg_Loan'})

if not business_analysis.empty:
    worst_business = business_analysis['Repayment_Status'].idxmax()
    worst_business_rate = business_analysis['Repayment_Status'].max()
    best_business = business_analysis['Repayment_Status'].idxmin()
    best_business_rate = business_analysis['Repayment_Status'].min()
else:
    worst_business = "N/A"
    worst_business_rate = 0
    best_business = "N/A"
    best_business_rate = 0

st.title("Jipange Youth SACCO Loan Portfolio Analysis")
st.write(f"Analyzing {len(filtered_df)} youth loans from {df['Loan_Year'].min()} to {df['Loan_Year'].max()}")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Total Loans", f"{total_loans:,}")

with col2:
    st.metric("Default Rate", f"{default_rate:.1f}%")

with col3:
    st.metric("On Time", f"{on_time_rate:.1f}%")

with col4:
    st.metric("Late Payments", f"{late_rate:.1f}%")

with col5:
    st.metric("Portfolio Value", f"KSh {total_value:,.0f}")

st.markdown("---")

left_col, right_col = st.columns([1, 3])

with left_col:
    st.header("Loan Performance Insights")
    
    st.subheader("Portfolio Overview")
    st.write(f"Total loans: {total_loans}")
    st.write(f"Default rate: {default_rate:.1f}%")
    st.write(f"On-time rate: {on_time_rate:.1f}%")
    st.write(f"Average loan size: KSh {avg_loan:,.0f}")
    
    st.subheader("Loan Size Risk Analysis")
    st.write(f"Highest risk: {worst_loan_size} loans")
    st.write(f"Default rate: {worst_loan_rate:.1f}%")
    st.write(f"Lowest risk: {best_loan_size} loans") 
    st.write(f"Default rate: {best_loan_rate:.1f}%")
    
    st.subheader("Age Risk Patterns")
    st.write(f"Highest risk age: {worst_age} years")
    st.write(f"Default rate: {worst_age_rate:.1f}%")
    st.write(f"Lowest risk age: {best_age} years")
    st.write(f"Default rate: {best_age_rate:.1f}%")
    
    st.subheader("Business Type Risk")
    st.write(f"Highest risk: {worst_business}")
    st.write(f"Default rate: {worst_business_rate:.1f}%")
    st.write(f"Lowest risk: {best_business}")
    st.write(f"Default rate: {best_business_rate:.1f}%")

with right_col:
    chart1, chart2 = st.columns(2)
    
    with chart1:
        chart1_type = st.selectbox("Chart Type:", ["Pie Chart", "Bar Chart", "Donut Chart"], key="chart1")
        status_counts = filtered_df['Repayment_Status'].value_counts()
        
        if chart1_type == "Pie Chart":
            fig1 = px.pie(values=status_counts.values, names=status_counts.index, 
                         title="Loan Repayment Status")
        elif chart1_type == "Donut Chart":
            fig1 = px.pie(values=status_counts.values, names=status_counts.index, 
                         title="Loan Repayment Status", hole=0.4)
        else:
            fig1 = px.bar(x=status_counts.index, y=status_counts.values,
                         title="Loan Repayment Status")
        
        st.plotly_chart(fig1, use_container_width=True)
        
        chart3_type = st.selectbox("Chart Type:", ["Bar Chart", "Line Chart", "Donut Chart"], key="chart3")
        
        if chart3_type == "Line Chart":
            fig3 = px.line(x=age_analysis_individual.index, y=age_analysis_individual['Repayment_Status'],
                          title="Default Rate by Borrower Age", markers=True)
        elif chart3_type == "Donut Chart":
            age_counts = filtered_df.groupby(
                pd.cut(filtered_df['Age'], [18, 25, 30, 35], labels=['18-25', '26-30', '31-35'])
            ).size()
            fig3 = px.pie(values=age_counts.values, names=age_counts.index,
                         title="Loan Distribution by Age Group", hole=0.4)
        else:
            fig3 = px.bar(x=age_analysis_individual.index, y=age_analysis_individual['Repayment_Status'],
                         title="Default Rate by Borrower Age")
        
        st.plotly_chart(fig3, use_container_width=True)
        
    with chart2:
        chart2_type = st.selectbox("Chart Type:", ["Bar Chart", "Horizontal Bar", "Donut Chart"], key="chart2")
        
        if chart2_type == "Horizontal Bar":
            fig2 = px.bar(loan_size_analysis, y=loan_size_analysis.index, x=loan_size_analysis['Repayment_Status'], 
                         title="Default Rate by Loan Size", orientation='h')
        elif chart2_type == "Donut Chart":
            loan_counts = filtered_df.groupby(
                pd.cut(filtered_df['Loan_Amount'], [5000, 15000, 30000, 50000], 
                       labels=['Small (5K-15K)', 'Medium (15K-30K)', 'Large (30K-50K)'])
            ).size()
            fig2 = px.pie(values=loan_counts.values, names=loan_counts.index,
                         title="Loan Distribution by Size", hole=0.4)
        else:
            fig2 = px.bar(x=loan_size_analysis.index, y=loan_size_analysis['Repayment_Status'],
                         title="Default Rate by Loan Size")
        
        st.plotly_chart(fig2, use_container_width=True)
        
        chart4_type = st.selectbox("Chart Type:", ["Bar Chart", "Line Chart", "Donut Chart"], key="chart4")
        
        if chart4_type == "Line Chart":
            fig4 = px.line(x=year_analysis.index, y=year_analysis['Repayment_Status'],
                          title="Default Rate Trend by Year", markers=True)
        elif chart4_type == "Donut Chart":
            year_counts = filtered_df['Loan_Year'].value_counts().sort_index()
            fig4 = px.pie(values=year_counts.values, names=year_counts.index,
                         title="Loan Distribution by Year", hole=0.4)
        else:
            fig4 = px.bar(x=year_analysis.index, y=year_analysis['Repayment_Status'],
                         title="Default Rate by Year")
        
        st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")
st.header("Loan Portfolio Details")
st.dataframe(filtered_df[['Borrower_ID', 'Name', 'Age', 'Business_Type', 'Loan_Amount', 
                         'Repayment_Status', 'Repayment_Score', 'Loan_Year']])