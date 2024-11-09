"""
Tests for functions in lib.py
"""

import os
import pytest
from my_lib.lib import (
    extract,
    load_data,
    describe,
    query,
    example_transform,
    start_spark,
    end_spark,
)


@pytest.fixture(scope="module")
def spark():
    spark = start_spark("TestApp")
    yield spark
    end_spark(spark)


@pytest.fixture(scope="module")
def df(spark):
    file_path = extract()
    df = load_data(spark, data=file_path)
    return df


def test_extract():
    file_path = extract()
    assert os.path.exists(file_path) is True


def test_load_data(df):
    assert df is not None
    assert df.count() > 0  # Ensure the dataframe has records
    assert "PROJ_FPTS" in df.columns  # Ensure renamed column exists


def test_describe(df):
    # Describe should return a summary and log output
    result = describe(df)
    assert result is None  # As describe function calls .show() which returns None


def test_query(spark, df):
    result = query(
        spark,
        df,
        "SELECT TEAM, AVG(PROJ_FPTS) AS avg_proj_points FROM WRRankings GROUP BY TEAM ORDER BY avg_proj_points DESC",
        "WRRankings",
    )
    assert result is None  # query function calls .show() which returns None


def test_example_transform(df):
    result = example_transform(df)
    assert result is None  # example_transform function calls .show() which returns None


if __name__ == "__main__":
    pytest.main()
