# Databricks notebook source
"""
Import functions
"""
from pyspark.sql import functions as f
from pyspark.sql.types import *

# COMMAND ----------

# MAGIC %md
# MAGIC # Lazy Evaluation

# COMMAND ----------

"""
Create a sample DF and display it.
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

df = spark.createDataFrame(data = data, schema = columns)

display(df) # Action

# id	name	email
# 1     lisa	lisa@random.com
# 2     john	john@random.com
# 3     mary	mary@random.com
# 4     peter	peter@random.com
# 5     jane	jane@random.com
# 6     jim     jim@random.com
# 7     sara	sara@random.com
# 8     bob     bob@random.com
# 9     alex	alex@random.com

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
Call an action - show is a native method from spark.
"""
df_new.show()

# +---+---------------+
# | id|          email|
# +---+---------------+
# |  6| jim@random.com|
# |  7|sara@random.com|
# |  8| bob@random.com|
# |  9|alex@random.com|
# +---+---------------+