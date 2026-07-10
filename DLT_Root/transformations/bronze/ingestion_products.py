import dlt

#Product Expectations
product_rules= {
    "rule_1" : "product_id is not NULL",
    "rule_2" : "price >= 0"
}

#Inesting products
@dlt.table(
    name="products_stg"
)
@dlt.expect_all_or_drop(product_rules)
def products_stg():
    df=spark.readStream.table("dltgautam.source.products")
    return df