import pandas as pd
import pyodbc

# Read cleaned CSV
df = pd.read_csv(
    r"C:\Users\kuche\OneDrive\Desktop\CUSTOMER CHURN\customer churn_cleaned.csv"
)

# Replace all NaN values
df = df.fillna("")


print(df.isnull().sum())

# Connect to SQL Server
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=LAPTOP-27URIM5D\\SQLEXPRESS;"
    "DATABASE=CustomerChurnDW;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

loaded_count = 0

for i, row in df.iterrows():

    try:

        cursor.execute("""
        INSERT INTO Stg_Customer_Churn
        (
            customer_id,
            customer_name,
            email,
            signup_date,
            last_login_date,
            region,
            subscription_plan,
            monthly_spend,
            support_tickets,
            feedback_text,
            churned
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,

        str(row["customer_id"]),
        str(row["customer_name"]),
        str(row["email"]),
        str(row["signup_date"]),
        str(row["last_login_date"]),
        str(row["region"]),
        str(row["subscription_plan"]),
        float(row["monthly_spend"]),
        int(row["support_tickets"]),
        str(row["feedback_text"]),
        int(row["churned"])

        )

        loaded_count += 1

    except Exception as e:

        print(f"\nError on row {i}")
        print(row)
        print(e)

conn.commit()

print(f"\n{loaded_count} records loaded successfully!")

cursor.close()
conn.close()