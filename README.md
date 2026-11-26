# Vendor Performance & Inventory Risk Analysis

## Project Overview
This project analyzes vendor purchasing, sales performance, profitability, stock turnover, and inventory risk across brands and products. Raw datasets stored in `dataset/` are ingested into SQLite (`inventory.db`), processed and aggregated into summary outputs in `analysed_data/`, analyzed in Python, and presented in a multi-page Power BI report alongside PDF summaries.

## Business Objectives
* Evaluate vendor sales vs. purchasing performance and freight cost impact
* Measure vendor concentration and purchase contribution across top suppliers
* Assess product-level sales, gross profit, and profit margins
* Identify low-turnover vendors and potential capital lock-up
* Segment inventory risk across excess stock, shortage risk, and dead stock

## Tools & Technologies
* **Python:** `pandas`, `numpy`, `matplotlib`, `seaborn`, `scipy`, `sqlalchemy`, `sqlite3`, `logging`
* **SQL (SQLite):** Joins, aggregations, summary table generation, and database querying (`inventory.db`)
* **Power BI:** Multi-page interactive dashboard, DAX measures, and visual reporting (`vendor_performance.pbix`)
* **Jupyter Notebook & Python Scripts:** Modular ETL pipeline and statistical exploratory data analysis

## Data Pipeline & Project Structure
```text
vendor-performance-analysis/
├── dataset/                             # Raw source datasets
├── analysed_data/                       # Processed / exported analysis tables & summaries
├── ingestion_db.py                      # Ingests raw datasets into SQLite (inventory.db)
├── get_vendor_summary.py                # Builds and cleans vendor sales summary data
├── inventory.db                         # SQLite database
├── Exploratory_data_analysis.ipynb      # Initial database and table exploration
├── vendor_performance_analysis.ipynb    # Statistical and visual EDA notebook
├── Untitled.ipynb                       # Draft / scratch notebook
├── vendor_performance.pbix              # Interactive Power BI dashboard file
├── vendor_performance_dashboard.pdf     # Exported Power BI dashboard PDF
├── vendor_performance_report.pdf        # Python EDA summary report PDF
├── logs/                                # Execution log files
├── .gitignore                           # Ignored cache, checkpoint, and local files
└── README.md                            # Project documentation
```

## Key Findings
* **High Vendor Purchase Concentration:** The top 5 vendors account for **44.96%** of total purchases, the top 10 account for **65.32%**, and the top 20 account for **83.62%**.
* **Skewed Distributions & Outliers:** Financial and volume metrics—including purchase/sales dollars, quantities, profit margins, and stock turnover—show strong positive skew and notable outliers.
* **Order Size & Unit Price Spread:** Smaller order sizes show wider upward unit-price outliers compared to medium and large bulk orders.
* **Profit Margin Differences Across Vendor Tiers:** Comparing high-volume top vendors against lower-volume vendors highlights distinct differences in average profit margin performance.
* **Inventory Risk Breakdown:** Across inventory tracking, **31.83%** is tied up in excess inventory, **12.60%** faces shortage risk, and **7.91%** is classified as dead stock.

## Dashboards & Reports
* **Interactive Power BI File:** `vendor_performance.pbix` (Executive Overview, Vendor & Product Analysis, and Inventory Analysis).
* **Dashboard Export:** `vendor_performance_dashboard.pdf` — Complete Power BI dashboard exported as PDF.
* **EDA Report Export:** `vendor_performance_report.pdf` — Python exploratory data analysis report with charts and statistical findings.

## How to Run Locally
1. Clone the repository and install the required Python libraries (`pandas`, `numpy`, `matplotlib`, `seaborn`, `scipy`, `sqlalchemy`).
2. Ensure the source data files are in `dataset/` and run `ingestion_db.py` to populate `inventory.db`.
3. Run `get_vendor_summary.py` to generate and clean the summary data (and export outputs to `analysed_data/` as needed).
4. Open `Exploratory_data_analysis.ipynb` and `vendor_performance_analysis.ipynb` in Jupyter to walk through the analysis.
5. Open `vendor_performance.pbix` in Power BI Desktop or view `vendor_performance_dashboard.pdf` and `vendor_performance_report.pdf`.

## Conclusion
Combining SQLite data preparation, Python exploratory and statistical analysis, and Power BI reporting turns raw purchase, sales, and inventory data into practical insights for supplier management, pricing, and inventory control.