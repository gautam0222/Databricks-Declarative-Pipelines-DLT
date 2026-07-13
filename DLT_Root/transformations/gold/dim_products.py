import dlt

# Creating Empty Streaming Table
dlt.create_streaming_table(
  name="dim_products",
)

#Auto CDC Flow
dlt.create_auto_cdc_flow(
  target = "dim_products",
  source = "products_enr_view",
  keys = ["product_id"],
  sequence_by = "last_updated",
  apply_as_deletes = None,
  apply_as_truncates = None,
  except_column_list = None,
  stored_as_scd_type = 2,
  track_history_column_list= None,
  track_history_except_column_list=None   
)