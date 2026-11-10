
import os
import sys
from pyspark.sql import SparkSession

# Use the same Python interpreter for Spark driver and workers
os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

# Create Spark Session
spark = (
    SparkSession.builder
    .appName("RetailSalesDataFrame")
    .master("local[*]")
    .getOrCreate()
)

# Create sample retail sales data
sales_data = [
    (1, "Laptop", 2, 150000),
    (2, "Mouse", 5, 2500),
    (3, "Keyboard", 3, 4500)
]

columns = ["SaleID", "Product", "Quantity", "Price"]

# Create DataFrame
sales_df = spark.createDataFrame(sales_data, columns)

# Display DataFrame
sales_df.show()

# Display schema
sales_df.printSchema()

# Count rows
print("Total Sales Records:", sales_df.count())

# Stop Spark
spark.stop()
