"""
library functions
"""

import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import when, col
from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType,
    StringType,
    FloatType,
)

LOG_FILE = "pyspark_output.md"


def log_output(operation, output, query=None):
    """adds to a markdown file"""
    with open(LOG_FILE, "a") as file:
        file.write(f"The operation is {operation}\n\n")
        if query:
            file.write(f"The query is {query}\n\n")
        file.write("The truncated output is: \n\n")
        file.write(output)
        file.write("\n\n")


def start_spark(appName):
    spark = SparkSession.builder.appName(appName).getOrCreate()
    return spark


def end_spark(spark):
    spark.stop()
    return "stopped spark session"


def extract(
    file_path="/data/WRRankingsWeek5.csv",
):
    """Verifies the existence of the data file"""
    if not os.path.exists(file_path):
        raise FileNotFoundError("Data file not found.")
    return file_path


def load_data(spark, data="/data/WRRankingsWeek5.csv", name="WRRankings"):
    """Load data with defined schema"""
    schema = StructType(
        [
            StructField("Player", StringType(), True),
            StructField("Team", StringType(), True),
            StructField("Pos", StringType(), True),
            StructField("Points", FloatType(), True),
            StructField("Week", IntegerType(), True),
        ]
    )

    df = spark.read.option("header", "true").schema(schema).csv(data)
    log_output("load data", df.limit(10).toPandas().to_markdown())
    return df


def query(spark, df, query, name):
    """Query using Spark SQL"""
    df = df.createOrReplaceTempView(name)
    log_output("query data", spark.sql(query).toPandas().to_markdown(), query)
    return spark.sql(query).show()


def describe(df):
    summary_stats_str = df.describe().toPandas().to_markdown()
    log_output("describe data", summary_stats_str)
    return df.describe().show()


def example_transform(df):
    """Example transformation on WR Rankings dataset"""
    conditions = [(col("Pos") == "WR") | (col("Pos") == "RB"), (col("Pos") == "TE")]

    categories = ["Wide Receiver/Running Back", "Tight End"]

    df = df.withColumn(
        "Position_Category",
        when(conditions[0], categories[0])
        .when(conditions[1], categories[1])
        .otherwise("Other"),
    )

    log_output("transform data", df.limit(10).toPandas().to_markdown())
    return df.show()
