import dlt

# Creating Empty Streaming Table
dlt.create_streaming_table(
  name="fact_sales",
)

#Auto CDC Flow
dlt.create_auto_cdc_flow(
  target = "fact_sales",
  source = "sales_enr_view",
  keys = ["sales_id"],
  sequence_by = "sale_timestamp",
  apply_as_deletes = None,
  apply_as_truncates = None,
  except_column_list = None,
  stored_as_scd_type = 1,
  track_history_column_list= None,
  track_history_except_column_list=None   
)