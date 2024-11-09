"""
Main CLI or app entry point
"""

from lib.lib import (
    extract,
    load_data,
    describe,
    query,
    example_transform,
    start_spark,
    end_spark,
)


def main():
    # extract data
    extract()
    # start spark session
    spark = start_spark("WRRankings")
    # load data into dataframe
    df = load_data(spark)
    # example metrics
    describe(df)
    # query
    query(
        spark,
        df,
        "SELECT Week, COUNT(*) AS player_count FROM WRRankings GROUP BY Week ORDER BY Week",
        "WRRankings",
    )
    # example transform
    example_transform(df)
    # end spark session
    end_spark(spark)


if __name__ == "__main__":
    main()
