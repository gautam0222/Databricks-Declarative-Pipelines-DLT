import dlt
from pyspark.sql.functions import *

#Creating Materialized View
@dlt.table(
    name="business_sales"
)
def business_sales():
    df_fact=spark.read.table("fact_sales")
    df_dimCust=spark.read.table("dim_customers")
    df_dimProd=spark.read.table("dim_products")

    df_join=df_fact.join(df_dimCust,df_fact.customer_id==df_dimCust.customer_id,"inner")
    df_join=df_join.join(df_dimProd,df_join.product_id==df_dimProd.product_id,"inner")
    df_join=df_join.select("region","category","total_amount")
    return df_join.groupBy("region","category").agg((sum("total_amount")).alias("total_sales"))
    
