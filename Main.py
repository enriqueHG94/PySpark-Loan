from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('reading CSV').getOrCreate()

df = spark.read.format('csv')\
    .option('header', 'true')\
    .load("resources\loan_data.csv")

df.show()