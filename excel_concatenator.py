import pandas as pd
import os

# Define the folder path where the files are located
folder_path = r"C:\Users\USER-NAME\Desktop"

# Define the filenames
file1 = "EXAMPLE1.csv"
file2 = "EXAMPLE2_Vehicle.csv"

# Combine full file paths
file1_path = os.path.join(folder_path, file1)
file2_path = os.path.join(folder_path, file2)

# Read the CSV files into Pandas DataFrames
try:
    df1 = pd.read_csv(file1_path)
    print(f"Successfully read {file1}")
except FileNotFoundError:
    print(f"Error: {file1} not found in {folder_path}")

try:
    df2 = pd.read_csv(file2_path)
    print(f"Successfully read {file2}")
except FileNotFoundError:
    print(f"Error: {file2} not found in {folder_path}")

# Example: Concatenate the two datasets vertically (rows combined)
try:
    combined_df = pd.concat([df1, df2], ignore_index=True)
    print("Datasets combined successfully!")
except Exception as e:
    print(f"Error combining datasets: {e}")

# Save the combined dataset to a new CSV file
output_file = os.path.join(folder_path, "Combined_Dataset.csv")
try:
    combined_df.to_csv(output_file, index=False)
    print(f"Combined dataset saved to {output_file}")
except Exception as e:
    print(f"Error saving combined dataset: {e}")
