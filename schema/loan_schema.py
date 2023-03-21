from pyspark.sql.types import StructType, StructField, StringType, IntegerType, LongType

class LoanSchema:
    CHECKING_STATUS_FIELD = "checking_status"
    DURATION_FIELD = "duration"
    CREDIT_HISTORY_FIELD = "credit_history"
    PURPOSE_FIELD = "purpose"
    CREDIT_AMOUNT_FIELD = "credit_amount"
    SAVINGS_STATUS_FIELD = "savings_status"
    EMPLOYMENT_FIELD = "employment"
    INSTALLMENT_COMMITMENT_FIELD = "installment_commitment"
    PERSONAL_STATUS_FIELD = "personal_status"
    OTHER_PARTIES_FIELD = "other_parties"
    RESIDENCE_SINCE_FIELD = "residence_since"
    PROPERTY_MAGNITUDE_FIELD = "property_magnitude"
    AGE_FIELD = "age"
    OTHER_PAYMENT_PLANS_FIELD = "other_payment_plans"
    HOUSING_FIELD = "housing"
    EXISTING_CREDITS_FIELD = "existing_credits"
    JOB_FIELD = "job"
    NUM_DEPENDENTS_FIELD = "num_dependents"
    OWN_TELEPHONE_FIELD = "own_telephone"
    FOREIGN_WORKER_FIELD = "foreign_worker"
    CLASS_FIELD = "class"

    def __init__(self):
        self.schema = StructType([
            StructField(self.CHECKING_STATUS_FIELD, StringType(), True),
            StructField(self.DURATION_FIELD, IntegerType(), True),
            StructField(self.CREDIT_HISTORY_FIELD, StringType(), True),
            StructField(self.PURPOSE_FIELD, StringType(), True),
            StructField(self.CREDIT_AMOUNT_FIELD, LongType(), True),
            StructField(self.SAVINGS_STATUS_FIELD, StringType(), True),
            StructField(self.EMPLOYMENT_FIELD, StringType(), True),
            StructField(self.INSTALLMENT_COMMITMENT_FIELD, IntegerType(), True),
            StructField(self.PERSONAL_STATUS_FIELD, StringType(), True),
            StructField(self.OTHER_PARTIES_FIELD, StringType(), True),
            StructField(self.RESIDENCE_SINCE_FIELD, IntegerType(), True),
            StructField(self.PROPERTY_MAGNITUDE_FIELD, StringType(), True),
            StructField(self.AGE_FIELD, IntegerType(), True),
            StructField(self.OTHER_PAYMENT_PLANS_FIELD, StringType(), True),
            StructField(self.HOUSING_FIELD, StringType(), True),
            StructField(self.EXISTING_CREDITS_FIELD, IntegerType(), True),
            StructField(self.JOB_FIELD, StringType(), True),
            StructField(self.NUM_DEPENDENTS_FIELD, IntegerType(), True),
            StructField(self.OWN_TELEPHONE_FIELD, StringType(), True),
            StructField(self.FOREIGN_WORKER_FIELD, StringType(), True),
            StructField(self.CLASS_FIELD, StringType(), True)
            ])

loan_entity = LoanSchema()