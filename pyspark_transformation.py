from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("SalesPipeline").getOrCreate()

# Read raw data (Bronze Layer)
df = spark.read.option("header", "true").csv("/mnt/datalake/bronze/sales_sample.csv")

# Data cleaning
df_clean = df.filter(col("price").isNotNull())

# Create total revenue column
df_transformed = df_clean.withColumn(
    "total_revenue",
    col("quantity") * col("price")
)

# Write to Silver Layer
df_transformed.write.mode("overwrite").parquet("/mnt/datalake/silver/sales_data")

print("Transformation completed successfully")
