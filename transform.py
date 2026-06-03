import pandas as pd

# Load data
df = pd.read_csv(
    r"C:\Users\kuche\OneDrive\Desktop\CUSTOMER CHURN\customer_churn_messy.csv")

# Remove extra spaces
df["customer_id"] = df["customer_id"].astype(str).str.strip()

# Standardize subscription plan values
df["subscription_plan"] = (
    df["subscription_plan"]
    .astype(str)
    .str.strip()
    .str.title()
)

# Fill missing subscription plans
df["subscription_plan"] = df["subscription_plan"].replace("Nan", "Unknown")

# Fill missing regions
df["region"] = df["region"].fillna("Unknown")

# Fill missing customer names
df["customer_name"] = df["customer_name"].fillna("Unknown")

# Fill missing feedback
df["feedback_text"] = df["feedback_text"].fillna("No Feedback")

# Remove negative spend values
df = df[df["monthly_spend"] >= 0]

# Convert dates
df["signup_date"] = pd.to_datetime(df["signup_date"], dayfirst=True)
df["last_login_date"] = pd.to_datetime(df["last_login_date"], dayfirst=True)

# Save cleaned file
df.to_csv(
    r"C:\Users\kuche\OneDrive\Desktop\CUSTOMER CHURN\customer churn_cleaned.csv",
    index=False
)

print("Cleaning Completed")
print("Final Shape:", df.shape)