import pandas as pd
import os
file_path = r'C:\Users\Arunav Pathak\Desktop\stock_project\project_folder\static\archive(2)\CIPLA.csv'

if os.path.exists(file_path):
    print(f"File found at: {file_path}")
else:
    print(f"File not found at: {file_path}")

try:
    df = pd.read_csv(file_path)
    print("CSV loaded successfully")
    print(df.head())
except Exception as e:
    print(f"Error occurred: {e}")
