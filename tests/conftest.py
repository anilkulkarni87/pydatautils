"""Conf for spark unitest."""
import pytest
from pyspark.sql import SparkSession


@pytest.fixture(scope="session")
def spark() -> SparkSession:
    """_summary_.

    Returns:
        SparkSession: _description_
    """
    spark = (
        SparkSession.builder.master("local[1]")
        .config("spark.port.maxRetries", "1000")
        .config("spark.sql.shuffle.partitions", "1")
        .getOrCreate()
    )
    return spark
