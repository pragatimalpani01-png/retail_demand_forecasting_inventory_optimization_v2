import argparse, sqlite3
from pathlib import Path
import pandas as pd
import numpy as np
ROOT=Path(__file__).resolve().parent
def main():
 p=argparse.ArgumentParser(); p.add_argument('--source',choices=['demo','raw'],default='demo'); a=p.parse_args()
 if a.source=='raw': raise SystemExit('M5 requires preprocessing. Follow DATA_GUIDE.md; the ready-to-run pipeline uses demo data.')
 sales=pd.read_csv(ROOT/'data/demo/daily_sales_demo.csv',parse_dates=['date'])
 inv=pd.read_csv(ROOT/'data/demo/inventory_snapshot_demo.csv')
 daily=sales.groupby(['date','store_id','sku'],as_index=False).agg(units_sold=('units_sold','sum'))
 cutoff=daily.date.max()-pd.Timedelta(days=60); train=daily[daily.date<=cutoff]; test=daily[daily.date>cutoff]
 rows=[]
 for (store,sku),g in train.groupby(['store_id','sku']):
  actual=test[(test.store_id==store)&(test.sku==sku)]
  if len(actual): rows.append([store,sku,np.mean(abs(actual.units_sold-g.tail(7).units_sold.mean())),np.mean(abs(actual.units_sold-g.tail(28).units_sold.mean()))])
 pd.DataFrame(rows,columns=['store_id','sku','mae_7d_mean','mae_28d_mean']).to_csv(ROOT/'outputs/holdout_metrics.csv',index=False)
 recent=daily[daily.date>=daily.date.max()-pd.Timedelta(days=55)].groupby('sku').units_sold.agg(['mean','std']).reset_index()
 x=inv.merge(recent,on='sku',how='left'); x['daily_demand']=x['mean'].fillna(0); x['demand_std_daily']=x['std'].fillna(0)
 period=x.supplier_lead_time_days+x.review_period_days
 x['target_stock']=np.ceil(x.daily_demand*(period+x.safety_stock_days)+1.65*x.demand_std_daily*np.sqrt(period))
 x['reorder_qty']=np.maximum(0,x.target_stock-x.current_on_hand); x['days_of_cover']=x.current_on_hand/x.daily_demand.replace(0,np.nan)
 x['stock_status']=np.where(x.days_of_cover<x.supplier_lead_time_days,'Review now',np.where(x.days_of_cover<period,'Watch','Covered'))
 x.to_csv(ROOT/'outputs/reorder_recommendations.csv',index=False)
 with sqlite3.connect(ROOT/'outputs/retail_demo.sqlite') as con:
  sales.to_sql('daily_sales',con,if_exists='replace',index=False); x.to_sql('reorder_recommendations',con,if_exists='replace',index=False)
 print('Outputs rebuilt. Open outputs/dashboard.html.')
if __name__=='__main__': main()
