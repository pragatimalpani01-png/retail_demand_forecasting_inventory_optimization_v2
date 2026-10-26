# Retail Demand Forecasting & Inventory Optimization

This project tackles a practical retail question: what should we expect to sell next, and which products need attention before they run out?

Instead of stopping at a sales dashboard, it connects demand patterns to a forecast check and a reorder worksheet. The dashboard walks through four steps: read demand, test a forecast, make a stock call, and stress-test the assumptions.

## Run it

1. Install Python 3.10 or newer.
2. Install requirements: `python -m pip install -r requirements.txt`
3. Rebuild the demo outputs: `python run_project.py --source demo`
4. Open `outputs/dashboard.html` in a browser.
5. Read `reports/retail_demand_inventory_review.pdf`.

The included data is synthetic and labelled as demo data. Do not describe its numbers as real retailer findings.

## What makes it worth exploring

- Time-based holdout comparison of simple forecast baselines.
- Reorder recommendations tied to demand, lead time and safety stock.
- An interactive dashboard with a guided story and adjustable assumptions.
- A view of stockout-censored demand: low sales can reflect lack of availability, not lack of customer demand.
- SQL examples, static visualizations, a SQLite database, and tests.

## Data source

The Walmart M5 Forecasting Accuracy data is available through Kaggle:
https://www.kaggle.com/competitions/m5-forecasting-accuracy/data

Access is free with a Kaggle account, subject to competition terms. The full dataset is not bundled here. See `DATA_GUIDE.md` for its structure and preparation notes. The current demo pipeline runs immediately; M5 requires preprocessing because daily sales are stored in wide format and calendar/prices are separate files.

## Limitations to keep in mind

The reorder formula is a planning approximation, not an automated purchasing system. A production version should account for open purchase orders, case-pack sizes, supplier minimums, expiry, inventory accuracy and service-level targets. Forecasts should be compared with seasonal-naive baselines using rolling-origin backtests. Sales during stockouts may understate true demand.
