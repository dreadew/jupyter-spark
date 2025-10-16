from pyspark.sql import DataFrame, SparkSession


def save_delta_table(df: DataFrame, path: str, mode: str = "overwrite") -> None:
    """
    Save a DataFrame to a Delta table at the specified path.

    :param df: The DataFrame to save.
    :param path: The path where the Delta table will be saved.
    :param mode: The save mode (default is 'overwrite').
    """
    df.write.format("delta").mode(mode).save(path)


def read_delta_table(spark: SparkSession, path: str) -> DataFrame:
    """
    Read a Delta table from the specified path.

    :param spark: The Spark session to use for reading the Delta table.
    :param path: The path where the Delta table is located.
    :return: A DataFrame containing the data from the Delta table.
    """
    return spark.read.format("delta").load(path)
