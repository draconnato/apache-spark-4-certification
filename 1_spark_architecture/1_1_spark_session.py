# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
# MAGIC %md
# MAGIC # Spark Session

# COMMAND ----------

"""
Databricks creates the SparkSession by default.
"""
print(spark)
# <pyspark.sql.session.SparkSession object at 0x7f1aa82b5f70>

# COMMAND ----------

"""
Spark context requires a SparkSession and in Databricks requires also dedicated access mode isolation.
"""
print(spark.sparkContext)
# <SparkContext master=local[*, 4] appName=Databricks Shell>

# COMMAND ----------

"""
You can create a new spark session If you want to customize session params:
ie. spark.conf.set(....)
"""
spark_new = spark.newSession()
print(spark_new)
# <pyspark.sql.session.SparkSession object at 0x7f1a28ed3830>