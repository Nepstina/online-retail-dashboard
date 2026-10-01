import os
import pandas as pd

def run_cleaning_pipeline():
    home = os.path.expanduser("~")
    possible_paths = [
        os.path.join(home, "Desktop"),
        os.path.join(home, "OneDrive", "Desktop"),
        os.path.join(home, "OneDrive - Personal", "Desktop")
    ]
    
    desktop_path = None
    for p in possible_paths:
        if os.path.exists(p):
            desktop_path = p
            break
            
    if not desktop_path:
        desktop_path = os.getcwd()

    
    project_dir =project_dir = r"C:\Users\Nepstina\OneDrive\Desktop\Online Retail Revenue Dashboard"

    data_folder = os.path.join(project_dir, "data")
    
    os.makedirs(data_folder, exist_ok=True)
    
    input_file = os.path.join(data_folder, "online_retail.csv")
    output_file = os.path.join(data_folder, "cleaned_retail_data.csv")
    print(f"Auto-building project inside: {project_dir}")
    
   
    print(" Generating fresh test data file...")
    dummy_data = {
        'InvoiceNo': ['536365', '536365', '536366', '536367', 'C536368', '536369'],
        'StockCode': ['85123A', '71053', '22752', '84029G', '71053', '21730'],
        'Description': ['White Heart Holder', 'White Lantern', 'Nesting Boxes', 'Hot Water Bottle', 'White Lantern', 'Glass Star Holder'],
        'Quantity': [6, 6, 2, 12, -1, 4],
        'InvoiceDate': ['2026-01-01 08:26', '2026-01-01 08:26', '2026-01-01 09:34', '2026-01-02 11:15', '2026-01-02 12:45', '2026-01-03 15:20'],
        'UnitPrice': [2.55, 3.39, 8.50, 3.75, 3.39, 4.25],
        'CustomerID': ['17850', '17850', '13047', '12346', '12346', None],
        'Country': ['United Kingdom', 'United Kingdom', 'France', 'Germany', 'Germany', 'United Kingdom']
    }
    pd.DataFrame(dummy_data).to_csv(input_file, index=False)
    
 
    print("Step 1: Loading raw data...")
    df = pd.read_csv(input_file)
    print(f" Original dataset size: {df.shape[0]} rows")

    print(" Step 2: Cleaning anomalies...")
    df = df.dropna(subset=['Description'])
    df['CustomerID'] = df['CustomerID'].fillna('Guest')
    df_clean = df[df['Quantity'] > 0].copy()

    print(" Step 3: Calculating metrics...")
    df_clean['TotalSales'] = df_clean['Quantity'] * df_clean['UnitPrice']

    print(" Step 4: Saving cleaned data...")
    df_clean.to_csv(output_file, index=False)
    
    print(f"\nSUCCESS! Cleaned dataset saved with {df_clean.shape[0]} rows.")
    print(f" Perfect data file ready at: {output_file}")

if __name__ == "__main__":
    run_cleaning_pipeline()
