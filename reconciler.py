import pandas as pd

def main():
    # Load the data silos
    stock = pd.read_csv('warehouse_stock.csv')
    sales = pd.read_csv('sales_records.csv')

    # Merge data on the unique SKU
    df = pd.merge(stock, sales, on='sku', how='left')

    # Calculate the discrepancy
    df['remaining'] = df['inventory_count'] - df['units_sold']

    print("--- LOGISTICS RECONCILIATION REPORT ---")
    print(df)

    # Check for "Oversold" errors
    oversold = df[df['remaining'] < 0]
    if not oversold.empty:
        print("\n--- ATTENTION: OVERSOLD ITEMS DETECTED ---")
        print(oversold)

        # Export the errors to a CSV for the operations team
        oversold.to_csv('discrepancies_to_fix.csv', index=False)
        print("\n[SUCCESS] Discrepancy report saved to 'discrepancies_to_fix.csv'")

if __name__ == "__main__":
    main()
