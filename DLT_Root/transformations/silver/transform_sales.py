import dlt
from pyspark.sql.functions import *

#Transforming Sales data
@dlt.view(
    name="sales_enr_view"
)
def sales_stg_trns():
    df=spark.readStream.table("sales_stg")
    df=df.withColumn("total_amount",col("quantity")*col("amount"))
    return df

#Creating Destination Silver Table
dlt.create_streaming_table(
    name="sales_enr"
)

dlt.create_auto_cdc_flow(
  target = "sales_enr",
  source = "sales_enr_view",
  keys = ["sales_id"],
  sequence_by = col("sale_timestamp"),
  apply_as_deletes = None,
  apply_as_truncates = None,
  except_column_list = None,
  stored_as_scd_type = 1
)