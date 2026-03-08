import pandas as pd
import glob

# Read all CSV files in the data folder
files = glob.glob("data/*.csv")

df_list = []

for file in files:
    df = pd.read_csv(file)
    df_list.append(df)

# Combine all CSV files
data = pd.concat(df_list)

# Keep only Pink Morsels
data = data[data["product"] == "pink morsel"]

# Remove $ sign from price and convert to float
data["price"] = data["price"].replace('[\$,]', '', regex=True).astype(float)

# Calculate sales
data["sales"] = data["quantity"] * data["price"]

# Select required columns
final_data = data[["sales", "date", "region"]]

# Save the processed file
final_data.to_csv("formatted_sales.csv", index=False)

print("Data processing completed!")