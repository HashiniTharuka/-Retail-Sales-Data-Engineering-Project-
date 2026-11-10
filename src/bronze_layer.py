
import os
import sys

from pyspark.sql import SparkSession

# --------------------------------------------------
# 1. Configure Python interpreter
# --------------------------------------------------
os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

# --------------------------------------------------
# 2. Create Spark session
# --------------------------------------------------
spark = (
    SparkSession.builder
    .appName("RetailSalesBronzeLayer")
    .master("local[*]")
    .config("spark.hadoop.fs.permissions.umask-mode", "000")
    .getOrCreate()
)

# Set Hadoop configuration
spark.sparkContext._jsc.hadoopConfiguration().set(
    "fs.permissions.umask-mode", "000"
)

try:
    # --------------------------------------------------
    # 3. Read raw CSV data
    # --------------------------------------------------
    input_path = "data/raw/retail_sales.csv"
    bronze_path = "data/bronze/retail_sales"

    sales_df = (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv(input_path)
    )

    print("\n========== RAW SALES DATA ==========")
    sales_df.show(20, truncate=False)

    print("Raw CSV Record Count:", sales_df.count())

    # --------------------------------------------------
    # 4. Write data to Bronze layer as Parquet
    # --------------------------------------------------
    sales_df.write \
        .mode("overwrite") \
        .parquet(bronze_path)

    print("\nBronze Layer Created Successfully!")

    # --------------------------------------------------
    # 5. Read data back from Bronze layer
    # --------------------------------------------------
    bronze_df = spark.read.parquet(bronze_path)

    print("\n========== BRONZE LAYER DATA ==========")
    bronze_df.show(20, truncate=False)

    print("Bronze Record Count:", bronze_df.count())

    print("\nBronze Schema:")
    bronze_df.printSchema()

finally:
    # --------------------------------------------------
    # 6. Stop Spark session
    # --------------------------------------------------
    spark.stop()
