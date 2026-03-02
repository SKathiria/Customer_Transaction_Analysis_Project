1. Introduction
Data plays a central role in modern banking, enabling organisations to understand customer behaviour, manage risk, and support informed decision-making. Financial institutions routinely analyse transaction data to identify spending patterns, monitor trends, and improve services while ensuring ethical and responsible use of customer information.
This project focuses on performing Exploratory Data Analysis (EDA) on a customer transaction dataset using Python. The objective is to clean and analyse transaction data, identify meaningful patterns, and present insights that are relevant to a retail banking context.
The project demonstrates foundational data science skills including data preprocessing, analysis, visualisation, and ethical awareness, all of which are essential for real-world financial analytics roles.

2. Dataset Description
The dataset used in this project is a synthetic customer transaction dataset sourced from an open-access data repository. The data is anonymised and does not contain any real personal or sensitive customer information.

Dataset characteristics
Number of records: 50,000 
Data type: Structured tabular data (CSV format)
Nature: Synthetic / simulated transaction data

Key attributes
customer_id – Unique identifier for each customer
name, surname – Customer name fields (synthetic)
gender – Customer gender (contains missing values)
birthdate – Customer date of birth
transaction_amount – Monetary value of each transaction
date – Date of transaction
merchant_name – Merchant where transaction occurred
category – Transaction category (e.g. Travel, Electronics, Clothing)
The dataset structure closely resembles real-world retail banking transaction logs, making it suitable for analytical practice while remaining ethically safe to use.

3. Tools and Technologies
The analysis was conducted using the following tools:
Python 3.13
Pandas – data manipulation and preprocessing
NumPy – numerical operations
Matplotlib & Seaborn – data visualisation
VS Code – development environment
These tools are widely used in industry for data analysis and financial analytics.

4. Data Preprocessing and Cleaning
Before analysis, the dataset required cleaning and standardisation to ensure data quality.
Key preprocessing steps
Standardised column names by converting them to lowercase and replacing spaces with underscores.
Identified missing values, particularly in the gender column.
Replaced missing gender values with "Unknown" to preserve data volume.
Converted date-related columns (date, birthdate) to datetime format.
Removed records with missing critical values such as transaction date or transaction amount.
Filtered out invalid transactions with negative transaction values.
These steps ensured that the dataset was consistent, reliable, and ready for analysis.

5. Exploratory Data Analysis (EDA)

  5.1 Transaction Amount Distribution
  Analysis of transaction amounts showed that:
  Most ransactions fall within a low to medium value range.
  A small number of high-value transactions act as outliers.
  This distribution reflects typical consumer banking behaviour, where frequent small purchases dominate transaction volume.

  5.2 Category-Based Spending Analysis
  Aggregated analysis by transaction category revealed:
  Certain categories such as Electronics, Travel, and Clothing contribute a larger proportion of total spending.
  Spending behaviour varies significantly across categories, highlighting opportunities for customer segmentation and targeted financial services.
  
  5.3 Merchant-Level Analysis
  Merchant aggregation showed:
  A limited number of merchants account for a significant share of total transaction value.
  This concentration could be useful for merchant risk assessment, partnership evaluation, or fraud monitoring in a banking environment.
  
  5.4 Time-Based Trends
  Monthly aggregation of transaction values demonstrated:
  Clear time-based variations in spending behaviour.
  Potential seasonal trends that could be explored further using predictive modelling or forecasting techniques.
  
  5.5 Demographic-Level Analysis
  Gender-based analysis was conducted at an aggregated level only:
  Small differences were observed in average transaction amounts.
  These results were interpreted cautiously to avoid demographic bias or individual profiling.

6. Ethical Considerations
Ethical responsibility was maintained throughout the project:
The dataset used was synthetic and anonymised, ensuring no real individuals could be identified.
Analysis focused on aggregated trends rather than individual-level behaviour.
Demographic attributes were used carefully and responsibly.
Findings were framed to avoid overgeneralisation or biased conclusions.
Ethical data handling is especially important in financial services, and this project reflects that awareness.

7. Conclusion
This project demonstrates how customer transaction data can be effectively cleaned, explored, and analysed using Python to generate meaningful insights in a banking context. Through structured preprocessing, exploratory analysis, and visualisation, the project highlights patterns in spending behaviour, category trends, merchant concentration, and time-based variation.
Beyond technical implementation, the project emphasises clear communication of insights and responsible data use. Together, these elements reflect a strong foundational skill set in data analysis and demonstrate readiness to apply data science techniques within real-world financial environments.

8. References
McKinney, W. (2018). Python for Data Analysis. O’Reilly Media.
Pandas Documentation: https://pandas.pydata.org/docs/
Matplotlib Documentation: https://matplotlib.org/stable/index.html
Seaborn Documentation: https://seaborn.pydata.org/
Synthetic transaction dataset sourced from an open-access data repository (e.g. Kaggle).
