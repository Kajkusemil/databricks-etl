from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
df = spark.read.csv("/databricks-datasets/samples/population-vs-price/data_geo.csv", header=True)
df.show()
