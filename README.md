
Jipange Youth SACCO Loan Portfolio Analysis Dashboard

Overview
A comprehensive Streamlit dashboard for analyzing loan portfolio performance and borrower reliability for Jipange Youth SACCO in Makueni County. The dashboard provides insights into repayment trends, default risks, and borrower behavior patterns.

#Features

#Dashboard Metrics
- Total Loans**: Count of all loans in the portfolio
- Default Rate**: Percentage of loans in default status
- On-time Repayment**: Percentage of loans repaid on schedule
- Late Payments**: Percentage of loans with delayed payments
- Portfolio Value**: Total value of all active loans

# Interactive Filters
- Borrower Age**: Slider (18-35 years)
- Loan Amount**: Slider (KSh 5,000 - 50,000)
- Business Type**: Multi-select filter
- *epayment Status**: Multi-select filter
- Loan Year**: Multi-select filter

#Visual Analytics
- **Repayment Status Distribution**: Pie/Bar/Donut charts
- **Default Rate by Loan Size**: Small, Medium, Large loans
- **Age Risk Patterns**: Default rates across different ages
- **Business Type Analysis**: Performance by business category
- **Yearly Trends**: Default rate trends over time

#  Risk Insights
- Identification of highest and lowest risk categories
- Age-based risk patterns
- Business type performance analysis
- Loan size risk assessment

# Installation

# Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

# Required Packages
Install the required packages using:

```bash
pip install streamlit pandas plotly numpy openpyxl
'''

Running the Application

1. Clone or download the project files
   · dashboard.py
   · jipange_dataset_cleaned.xlsx
   · requirements.txt
2. Navigate to the project directory
   bash
   cd JIPANGE_SACCO_PROJECT
   
3. Run the Streamlit application
   bash
   streamlit run dashboard.py
   
4. Access the dashboard
   · Local URL: http://localhost:8501
   · Network URL: Provided in the terminal output

Data Structure

The application uses an Excel file (jipange_dataset_cleaned.xlsx) with the following columns:

· Borrower_ID: Unique identifier for each borrower
· Name: Borrower's name
· Age: Borrower's age (18-35)
· Loan_Amount: Loan amount in Kenyan Shillings
· Business_Type: Type of business (Salon, Farming, Retail, Boda Boda, Other)
· Income_Level: Income category (High, Medium, Low)
· Repayment_Status: Loan status (On-time, Late, Default)
· Repayment_Score: Numerical score (0-1) indicating repayment reliability
· Loan_Year: Year the loan was disbursed

Usage Guide

1. Apply Filters

Use the sidebar filters to narrow down the loan portfolio data based on:

· Age range of borrowers
· Loan amount brackets
· Business types
· Repayment statuses
· Loan years

2. Analyze Metrics

View the key performance indicators in the top metrics section to get an overview of portfolio health.

3. Explore Charts

· Use chart type selectors to switch between different visualization formats
· Analyze repayment patterns across different dimensions
· Identify risk trends and performance insights

4. Review Detailed Data

Scroll to the bottom to view the filtered dataset with all borrower details.

Technical Details

Built With

· Streamlit: Web application framework
· Pandas: Data manipulation and analysis
· Plotly: Interactive visualizations
· NumPy: Numerical computations

File Structure


JIPANGE_SACCO_PROJECT/
├── dashboard.py          # Main application file
├── jipange_dataset_cleaned.xlsx  # Dataset
├── requirements.txt      # Python dependencies
└── README.md            # This file
``

Support

For technical issues or questions about the dashboard:

1. Ensure all required packages are installed
2. Verify the Excel file is in the correct location
3. Check that the Excel file format matches the expected structure

License

This project is developed for academic project purposes as part of Zetech University requirements.

Author

Lizpencer Adhiambo Okello
DDA-01-0047/2024
Department of ICT and Engineering
Zetech University
