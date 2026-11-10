
import os
import sys

from pyspark.sql import SparkSession

# Configure Python interpreter for PySpark
os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

# Create Spark session
spark = (
    SparkSession.builder
    .appName("RetailSalesCSVIngestion")
    .master("local[*]")
    .getOrCreate()
)

# Read retail sales CSV file
sales_df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("data/raw/retail_sales.csv")
)

# Display data
print("RETAIL SALES DATA")
sales_df.show(20, truncate=False)

# Display schema
print("DATA SCHEMA")
sales_df.printSchema()

# Display record count
print("Total Records:", sales_df.count())

# Display column names
print("Column Names:", sales_df.columns)

# Stop Spark session
spark.stop()
