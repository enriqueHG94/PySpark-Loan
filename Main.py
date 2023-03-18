from pyspark.sql import SparkSession

# Crea una sesión de Spark
spark = SparkSession.builder.appName('reading CSV').getOrCreate()

# Lee el archivo CSV desde la carpeta
df = spark.read.format('csv')\
    .option('header', 'true')\
    .load("Resources\Loan-Data.csv")

# Muestra el dataframe
df.show()
