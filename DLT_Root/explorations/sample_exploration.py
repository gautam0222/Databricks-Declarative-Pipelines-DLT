# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
df=spark.read.table("dltgautam.source.orders")
display(df)
