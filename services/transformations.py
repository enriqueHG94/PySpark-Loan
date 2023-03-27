from pyspark.sql.functions import when

def transform_dataframe(df):
    categorized_age = when(df.age < 25, 'joven') \
        .when((df.age >= 25) & (df.age < 60), 'adulto') \
        .otherwise('anciano')
    transformed_df = df.select('duration', 'credit_history', 'purpose', 'credit_amount', 'personal_status',
                               'age', categorized_age.alias('categorized_age'), 'housing', 'existing_credits',
                               'num_dependents', (df.employment.isNotNull()).alias('is_employed'))
    return transformed_df
