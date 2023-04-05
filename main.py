from pyspark.sql import SparkSession
from schema.loan_schema import loan_entity
from services.transformations import transform_dataframe

spark = SparkSession.builder.appName('working CSV').getOrCreate()

df = spark.read.format('csv') \
    .option('header', 'true') \
    .schema(loan_entity.schema) \
    .load("resources\loan_data.csv")

transformed_df = transform_dataframe(df)
transformed_df.show()
