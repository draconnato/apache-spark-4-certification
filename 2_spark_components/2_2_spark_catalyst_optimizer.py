# Databricks notebook source
from pyspark.sql import functions as f
from pyspark.sql.types import *

# COMMAND ----------

"""
Add transformations in the new DF, but without action.
Creates the optimized plan.
"""
data = [
    (1, "lisa", "lisa@random.com"),
    (2, "john", "john@random.com"),
    (3, "mary", "mary@random.com"),
    (4, "peter", "peter@random.com"),
    (5, "jane", "jane@random.com"),
    (6, "jim", "jim@random.com"),
    (7, "sara", "sara@random.com"),
    (8, "bob", "bob@random.com"),
    (9, "alex", "alex@random.com"),
]

columns = ["id", "name", "email"]

df_new = spark.createDataFrame(data = data, schema = columns)

# Transformation - 1
df_new = df_new.select("id","email")

# Transformation - 2
df_new = df_new.filter(
    f.col("id") > 5
)

# No output.

# COMMAND ----------

"""
Call an action - display is only available in Databricks.
"""
display(df_new)

# id	email
# 6     jim@random.com
# 7     sara@random.com
# 8     bob@random.com
# 9     alex@random.com

# COMMAND ----------

"""
Returns the phisical plan that will be send to workers.

It needs to be read from botton to top direction.

In the previous cel we selected columns first and then filter the id.

But the catalyst optimizer moves the filter before, since it will be a better performance prune the data first
"""
df_new.explain()

# == Physical Plan ==
# *(1) Project [id#6L, email#8]
# +- *(1) Filter (isnotnull(id#6L) AND (id#6L > 5))
#    +- *(1) Scan ExistingRDD[id#6L,name#7,email#8]