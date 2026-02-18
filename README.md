# Logistics Data Reconciliation Engine

This project implements a multi-source data reconciliation pipeline that compares warehouse inventory records against digital sales data to identify operational discrepancies such as oversold SKUs and inventory mismatches.

The system is designed to simulate real-world logistics auditing workflows by programmatically detecting inconsistencies and generating structured discrepancy reports for operational review.

---

## Overview

Operational systems often maintain fragmented data across multiple sources (e.g., warehouse systems and sales platforms). When these systems fall out of sync, businesses may experience:

- Ghost inventory
- Oversold items
- Fulfillment failures
- Reporting inaccuracies

This reconciliation engine demonstrates how integrated data auditing can be performed programmatically using Pandas.

The pipeline performs:

1. Multi-source data ingestion  
2. Key-based dataset merging  
3. Inventory variance computation  
4. Discrepancy detection  
5. Automated report generation  

The result is a structured reconciliation report highlighting high-risk operational errors.

---

## Features

### Multi-Source Data Integration

- Loads inventory data from `warehouse_stock.csv`
- Loads sales data from `sales_records.csv`
- Performs key-based joins on `sku`

---

### Inventory Variance Computation

Calculates:

```
remaining_inventory = inventory_count - units_sold
```

This allows the system to identify negative inventory conditions.

---

### Discrepancy Detection

Flags:
- Oversold SKUs (negative remaining inventory)
- Items requiring operational review

High-priority discrepancies are exported automatically.

---

## Output Artifacts

Discrepancy reports are saved to:

```
discrepancies_to_fix.csv
```

This simulates structured reporting workflows used by operations teams.

---

## Project Structure

```
reconciler.py
warehouse_stock.csv
sales_records.csv
discrepancies_to_fix.csv  # generated after execution
README.md
```

---

## How to Run

### 1. Activate virtual environment

```bash
source venv/bin/activate
```

### 2. Run the reconciliation engine

```bash
python reconciler.py
```

### 3. Review outputs

- Full reconciliation report printed in terminal
- High-priority discrepancies exported to `discrepancies_to_fix.csv`

---

## Technologies Used

- Python 3.x  
- Pandas (data manipulation & joins)  
- CSV-based data integration  

---

## Future Improvements

- Full outer join reconciliation with missing SKU detection  
- Duplicate SKU aggregation logic  
- Missing value handling (treat null `units_sold` as 0)  
- Summary audit metrics (total inventory, total discrepancies)  
- Database-backed ingestion (PostgreSQL)  
- Streaming ingestion via Kafka  

---

