from pyspark.sql import SparkSession

# Crea una sesión de Spark
spark = SparkSession.builder.appName('reading CSV').getOrCreate()

# Lee el archivo CSV desde la carpeta
df = spark.read.format('csv')\
    .option('header', 'true')\
    .load("resources\loan_data.csv")

# Muestra el dataframe
df.show()
