import dlt
from pyspark.sql.functions import *
from pyspark.sql.types import *

#Transforming Products data
@dlt.view(
    name="products_enr_view"
)
def products_stg_trns():
    df=spark.readStream.table("products_stg")
    df=df.withColumn("price",col("price").cast(IntegerType()))
    return df

#Creating Destination Silver Table
dlt.create_streaming_table(
    name="products_enr"
)

dlt.create_auto_cdc_flow(
  target = "products_enr",
  source = "products_enr_view",
  keys = ["product_id"],
  sequence_by = col("last_updated"),
  apply_as_deletes = None,
  apply_as_truncates = None,
  except_column_list = None,
  stored_as_scd_type = 1
)