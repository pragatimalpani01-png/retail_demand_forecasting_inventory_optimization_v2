import unittest
from pathlib import Path
import pandas as pd
R=Path(__file__).resolve().parents[1]
class Checks(unittest.TestCase):
 def test_required_columns(self):
  d=pd.read_csv(R/'data/demo/daily_sales_demo.csv')
  self.assertTrue({'date','store_id','sku','units_sold','stockout_flag'}.issubset(d.columns))
 def test_nonnegative_sales(self):
  d=pd.read_csv(R/'data/demo/daily_sales_demo.csv'); self.assertTrue((d.units_sold>=0).all())
 def test_unique_inventory_skus(self):
  d=pd.read_csv(R/'data/demo/inventory_snapshot_demo.csv'); self.assertEqual(d.sku.nunique(),len(d))
if __name__=='__main__': unittest.main()
