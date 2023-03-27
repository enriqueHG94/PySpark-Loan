from pyspark.sql import SparkSession
from schema.loan_schema import loan_entity

spark = SparkSession.builder.appName('working CSV').getOrCreate()

df = spark.read.format('csv')\
    .option('header', 'true')\
    .schema(loan_entity.schema)\
    .load("resources\loan_data.csv")


df.show()