# Logistics Data Reconciliation Engine

## Overview
This project is an automated auditing tool designed to synchronize fragmented logistics data. It identifies discrepancies between physical warehouse inventory and digital sales records to prevent "ghost inventory" and fulfillment failures.

## Features
- **Automated Data Merging**: Uses Pandas to perform left-joins on disparate CSV data sources.
- **Discrepancy Detection**: Programmatically calculates inventory variances.
- **Automated Reporting**: Generates a 'high-priority' CSV report for items requiring immediate operational attention (oversold stock).

## Tech Stack
- **Language**: Python 3.13
- **Libraries**: Pandas (Data Manipulation)
- **Environment**: Isolated Virtual Environments (venv) for project reproducibility.

## How to Run
1. Activate the environment: `source venv/bin/activate`
2. Run the reconciler: `python3 reconciler.py`
3. View results in the terminal or check `discrepancies_to_fix.csv`.