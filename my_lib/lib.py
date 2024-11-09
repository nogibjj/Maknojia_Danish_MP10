import os
import requests
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
    url="https://raw.githubusercontent.com/nogibjj/Maknojia_Danish_MP5/refs/heads/main/data/WRRankingsWeek5.csv",
    file_path="data/WRRankingsWeek5.csv",
    directory="data",
):
    """Return file path of the provided dataset"""
    """Extract a url to a file path"""
    if not os.path.exists(directory):
        os.makedirs(directory)
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)

    return file_path


def load_data(spark, data="data/WRRankingsWeek5.csv", name="WRRankings"):
    """Load data with updated schema for WRRankings dataset"""
    # Adjust schema according to dataset structure
    schema = StructType(
        [
            StructField("RK", IntegerType(), True),
            StructField("PLAYER NAME", StringType(), True),
            StructField("TEAM", StringType(), True),
            StructField("OPP", StringType(), True),
            StructField("MATCHUP", StringType(), True),
            StructField("START/SIT", StringType(), True),
            StructField("PROJ. FPTS", FloatType(), True),
        ]
    )

    df = spark.read.option("header", "true").schema(schema).csv(data)

    df = df.withColumnRenamed("PROJ. FPTS", "PROJ_FPTS")

    log_output("load data", df.limit(10).toPandas().to_markdown())

    return df


def query(spark, df, query, name):
    """queries using spark sql"""
    df = df.createOrReplaceTempView(name)

    log_output("query data", spark.sql(query).toPandas().to_markdown(), query)

    return spark.sql(query).show()


def describe(df):
    summary_stats_str = df.describe().toPandas().to_markdown()
    log_output("describe data", summary_stats_str)

    return df.describe().show()


def example_transform(df):
    """Applies transformation on START/SIT column based on its values"""
    conditions = [
        (col("START/SIT") == "A+"),
        (col("START/SIT") == "A"),
        (col("START/SIT") == "B"),
    ]

    recommendations = ["Must Start", "Consider Starting", "Bench"]

    df = df.withColumn(
        "Start_Sit_Recommendation",
        when(conditions[0], recommendations[0])
        .when(conditions[1], recommendations[1])
        .otherwise("Bench"),
    )

    log_output("transform data", df.limit(10).toPandas().to_markdown())

    return df.show()
