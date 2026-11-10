
from pyspark.sql import SparkSession

# Create Spark Session
spark = (
    SparkSession.builder
    .appName("RetailSalesDataPipeline")
    .master("local[*]")
    .getOrCreate()
)

# Display Spark version
print("Spark Version:", spark.version)

# Stop Spark Session
spark.stop()
