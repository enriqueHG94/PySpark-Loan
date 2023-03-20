from pyspark.sql import SparkSession
from schema.loan_schema import LoanEntity

spark = SparkSession.builder.appName('reading CSV').getOrCreate()

df = spark.read.format('csv')\
    .option('header', 'true')\
    .schema(LoanEntity.schema)\
    .load("resources\loan_data.csv")

df.show()