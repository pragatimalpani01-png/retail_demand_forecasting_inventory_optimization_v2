# Data guide

## Included files
- `data/demo/daily_sales_demo.csv`: daily units by store and SKU, category, unit price, promotion flag and a synthetic stockout proxy.
- `data/demo/inventory_snapshot_demo.csv`: example on-hand quantities, supplier lead times, review periods and safety-stock assumptions.

All included data is synthetic.

## M5 dataset
Official page: https://www.kaggle.com/competitions/m5-forecasting-accuracy/data

The data is free to access with a Kaggle account, subject to the competition's current terms. The full files are large and are not included here. The M5 sales file is wide: each row is an item/store series and each day has its own column. To adapt it, reshape the day columns to long form (`date`, `store_id`, `sku`, `units_sold`), map day IDs to dates using the calendar file, and join prices at the item/store/week level. Check the competition terms before redistributing source files.
