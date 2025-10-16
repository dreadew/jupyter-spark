from common.settings import SPARK_URL
from pyspark.sql import SparkSession


class SparkSessionManager:

    @staticmethod
    def get_spark_session(
        app_name: str = "DefaultApp",
    ) -> SparkSession:
        """
        Get a Spark session with the specified application name.

        :param app_name: Name of the Spark application.
        :return: A SparkSession instance.
        """

        return (
            SparkSession
            .builder
            .appName(app_name)
            .master(SPARK_URL)
            .getOrCreate()
        )
