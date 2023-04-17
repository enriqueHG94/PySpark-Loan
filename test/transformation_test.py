from services.transformations import transform_dataframe
from pyspark.sql import SparkSession
from pyspark.sql.functions import lit

spark = SparkSession.builder.appName('CSV Reader').getOrCreate()

print('tranformation should be applied')

sample_df = spark.read.csv('resources/samples/sample.csv', header=True)

transformed_df = transform_dataframe(sample_df)

expected_df = spark.read.csv('resources/expected/expected.csv', header=True)\
    .withColumn('categorized_age', lit('adulto'))\
    .withColumn('is_employed', lit(True))


print('transformed_df:\n')
transformed_df.show()

print('expected_df:\n')
expected_df.show()

actual = transformed_df.select(sorted(transformed_df.columns)).collect()
expected = expected_df.select(sorted(expected_df.columns)).collect()
assert actual == expected