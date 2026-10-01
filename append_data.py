import os
import pandas as pd

def append_new_transactions():
  
    project_dir = r"C:\Users\Nepstina\OneDrive\Desktop\Online Retail Revenue Dashboard"
    raw_file = os.path.join(project_dir, "data", "online_retail.csv")
    
    print("🔄 Preparing to add new data...")

   
    new_data = {
        'InvoiceNo': ['536371', '536372', '536373'],
        'StockCode': ['22752', '21730', '85123A'],
        'Description': ['Set 7 Babushka Nesting Boxes', 'Glass Star Holder', 'White Heart Holder'],
        'Quantity':[10, 5, 2],
        'InvoiceDate': ['2026-10-01 10:15', '2026-10-01 11:30', '2026-10-01 14:00'],
        'UnitPrice': [8.50, 4.25, 2.55],
        'CustomerID': ['15000', '16500', 'Guest'],
        'Country': ['France', 'United Kingdom', 'United Kingdom']
    }

    df_new = pd.DataFrame(new_data)

    
    if os.path.exists(raw_file):
        print(" Found existing online_retail.csv file. Appending rows...")
        
        df_existing = pd.read_csv(raw_file)
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
        df_combined.to_csv(raw_file, index=False)
    else:
        print(" File not found. Creating a brand new online_retail.csv file instead...")
        df_new.to_csv(raw_file, index=False)
        
    print(f" SUCCESS! Added {len(df_new)} new sales rows to your raw dataset.")
    print(" NEXT STEP: Run your 'clean_data.py' script to update the dashboard metrics!")

if __name__ == "__main__":
    append_new_transactions()
