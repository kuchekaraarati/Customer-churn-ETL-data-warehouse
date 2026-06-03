# Customer-churn-ETL-data-warehouse
End-to-end ETL and data warehousing project using Python, Pandas, SQL Server, and pyodbc for customer churn analytics.
# Customer Churn ETL & Data Warehousing Project

## Project Overview

This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline built using Python, Pandas, SQL Server, and pyodbc. The objective was to process messy customer churn data, perform data quality validation and transformation, load cleansed data into SQL Server, and create a dimensional data warehouse for analytics.

## Project Highlights

• Processed 500 customer records
• Cleaned and validated data using Python and Pandas
• Loaded 488 records into SQL Server
• Built staging, dimension, and fact tables
• Developed end-to-end ETL pipeline using Python and pyodbc
• Achieved 52.46% churn analysis reporting through SQL queries

## Business Problem

Organizations often receive customer data from multiple sources containing missing values, inconsistent formats, invalid records, and duplicate information. Poor data quality can negatively impact analytics and business decision-making.

This project focuses on:

* Data profiling and quality assessment
* Data cleaning and transformation
* SQL Server data loading
* Data warehouse design
* Customer churn analytics

## Technologies Used

### Programming

* Python
* SQL

### Libraries

* Pandas
* pyodbc

### Database

* Microsoft SQL Server

### Concepts

* ETL Development
* Data Warehousing
* Data Modeling
* Data Quality Validation
* Analytics Reporting

## Dataset

The project uses a synthetic customer churn dataset containing:

* Customer Information
* Subscription Plans
* Monthly Spending
* Support Tickets
* Customer Feedback
* Churn Status

### Initial Dataset

* Records: 500

### Final Dataset

* Records Loaded: 488

## ETL Pipeline Architecture

Raw CSV Data
↓
Data Profiling
↓
Data Cleaning & Validation
↓
Data Transformation
↓
Clean Dataset
↓
SQL Server Staging Table
↓
Dimension Tables
↓
Fact Table
↓
Analytics Queries

## Data Quality Checks Performed

* Missing Value Identification
* Missing Value Handling
* Invalid Email Detection
* Negative Spending Detection
* Data Standardization
* Data Type Validation
* Duplicate Analysis

## Data Warehouse Design

### Staging Table

Stg_Customer_Churn

### Dimension Table

DimCustomer

Columns:

* CustomerID
* CustomerName
* Region
* SubscriptionPlan

### Fact Table

FactCustomerActivity

Columns:

* CustomerID
* MonthlySpend
* SupportTickets
* Churned

## Key Analytics Results

### Overall Churn Analysis

* Total Customers: 488
* Churned Customers: 256
* Churn Rate: 52.46%

### Churn by Subscription Plan

| Subscription Plan | Customers | Churned Customers | Churn Rate |
| ----------------- | --------- | ----------------- | ---------- |
| Basic             | 131       | 72                | 54.96%     |
| Enterprise        | 83        | 47                | 56.63%     |
| Premium           | 138       | 73                | 52.90%     |
| Unknown           | 136       | 64                | 47.06%     |

### Average Monthly Spend by Region

| Region  | Average Spend |
| ------- | ------------- |
| Central | 279.62        |
| East    | 242.40        |
| North   | 271.95        |
| South   | 256.30        |
| Unknown | 251.94        |
| West    | 254.88        |

## Project Structure

Customer-Churn-ETL-DataWarehouse

├── data

│ ├── customer_churn_messy_500.csv

│ └── customer_churn_clean.csv

├── scripts

│ ├── extract.py

│ ├── transform.py

│ └── customer_churn_load.py

├── sql

│ ├── create_tables.sql

│ ├── load_dimension_tables.sql

│ └── analytics_queries.sql

└── README.md

## Business Insights

### Customer Churn Overview

The dataset contained 488 valid customer records after data quality validation and cleaning. Analysis showed that 256 customers had churned, resulting in an overall churn rate of 52.46%. This indicates that more than half of the customer base discontinued the service.

### Subscription Plan Analysis

Enterprise customers exhibited the highest churn rate (56.63%), followed by Basic plan customers (54.96%). Premium plan customers showed a slightly lower churn rate (52.90%), suggesting marginally better customer retention compared to other plans.

The Unknown subscription category recorded the lowest churn rate (47.06%), indicating either stronger retention within this segment or potential data quality issues that may require further investigation.

### Regional Spending Analysis

Customers from the Central region generated the highest average monthly spend (279.62), while customers from the East region recorded the lowest average spend (242.40).

The difference in spending patterns across regions suggests that customer value may vary geographically, which could help guide targeted retention and marketing strategies.

### Data Quality Findings

During the ETL process, multiple data quality issues were identified, including missing values, inconsistent records, and invalid data entries. After applying validation and cleaning rules, 488 high-quality records were successfully loaded into the SQL Server data warehouse for analytics.

## Recommendations

* Investigate factors contributing to high churn among Enterprise and Basic subscription plan customers.
* Conduct deeper customer behavior analysis to identify potential churn indicators.
* Develop targeted customer retention strategies for high-risk customer segments.
* Improve source data quality processes to reduce missing or unknown customer attributes.
* Implement regular churn monitoring and reporting to support proactive business decision-making.
* Enhance the data warehouse by incorporating additional customer interaction and transaction data for richer analytics.

## Key Learnings

* Building end-to-end ETL pipelines using Python and SQL Server
* Data cleaning and transformation techniques
* Data quality validation processes
* SQL Server integration using pyodbc
* Data warehouse design using fact and dimension tables
* Business analytics using SQL queries
