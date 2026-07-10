import dlt

#Customer Expectations
customer_rules= {
    "rule_1" : "customer_id is not NULL",
    "rule_2" : "customer_name is not NULL"
}

#Inesting customers
@dlt.table(
    name="customers_stg"
)
@dlt.expect_all_or_drop(customer_rules)
def customers_stg():
    df=spark.readStream.table("dltgautam.source.customers")
    return df