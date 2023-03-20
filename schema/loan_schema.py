from pyspark.sql.types import StructType, StructField, StringType, IntegerType, LongType

class loan:
    def __init__(self):
        self.schema = StructType([
            StructField("checking_status", StringType(), True),
            StructField("duration", IntegerType(), True),
            StructField("credit_history", StringType(), True),
            StructField("purpose", StringType(), True),
            StructField("credit_amount", LongType(), True),
            StructField("savings_status", StringType(), True),
            StructField("employment", StringType(), True),
            StructField("installment_commitment", IntegerType(), True),
            StructField("personal_status", StringType(), True),
            StructField("other_parties", StringType(), True),
            StructField("residence_since", IntegerType(), True),
            StructField("property_magnitude", StringType(), True),
            StructField("age", IntegerType(), True),
            StructField("other_payment_plans", StringType(), True),
            StructField("housing", StringType(), True),
            StructField("existing_credits", IntegerType(), True),
            StructField("job", StringType(), True),
            StructField("num_dependents", IntegerType(), True),
            StructField("own_telephone", StringType(), True),
            StructField("foreign_worker", StringType(), True),
            StructField("class", StringType(), True)
        ])

LoanEntity = loan()