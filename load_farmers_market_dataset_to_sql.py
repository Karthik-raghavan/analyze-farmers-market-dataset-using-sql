import sqlalchemy
import pandas as pd

engine = sqlalchemy.create_engine("mysql+pymysql://root:admin@localhost/farmers-market")

booth = pd.read_csv('farmers-market-dataset/booth.csv')
customer_purchases = pd.read_csv('farmers-market-dataset/customer_purchases.csv')
customer = pd.read_csv('farmers-market-dataset/customer.csv')
datetime_demo = pd.read_csv('farmers-market-dataset/datetime_demo.csv')
market_date_info = pd.read_csv('farmers-market-dataset/market_date_info.csv')
product_category = pd.read_csv('farmers-market-dataset/product_category.csv')
product = pd.read_csv('farmers-market-dataset/product.csv')
vendor_booth_assignments = pd.read_csv('farmers-market-dataset/vendor_booth_assignments.csv')
vendor_inventory = pd.read_csv('farmers-market-dataset/vendor_inventory.csv')
vendor = pd.read_csv('farmers-market-dataset/vendor.csv')

booth.to_sql("booth",engine, index=False, if_exists="replace")
customer_purchases.to_sql("customer_purchases",engine, index=False, if_exists="replace")
customer.to_sql("customer",engine, index=False, if_exists="replace")
datetime_demo.to_sql("datetime_demo",engine, index=False, if_exists="replace")
market_date_info.to_sql("market_date_info",engine, index=False, if_exists="replace")
product_category.to_sql("product_category",engine, index=False, if_exists="replace")
product.to_sql("product",engine, index=False, if_exists="replace")
vendor_booth_assignments.to_sql("vendor_booth_assignments",engine, index=False, if_exists="replace")
vendor_inventory.to_sql("vendor_inventory",engine, index=False, if_exists="replace")
vendor.to_sql("vendor",engine, index=False, if_exists="replace")


