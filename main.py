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
    # extract data path
    data_path = extract()
    # start spark session
    spark = start_spark("WRRankings")
    # load data into dataframe
    df = load_data(spark, data=data_path)
    # example metrics
    describe(df)
    # query
    query(
        spark,
        df,
        """
        SELECT TEAM, AVG(PROJ_FPTS) AS avg_proj_points 
        FROM WRRankings 
        GROUP BY TEAM 
        ORDER BY avg_proj_points DESC
        """,
        "WRRankings",
    )
    # example transform
    example_transform(df)
    # end spark session
    end_spark(spark)

if __name__ == "__main__":
    main()
