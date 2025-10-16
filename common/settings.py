import os
from dotenv import load_dotenv
from typing import List

load_dotenv()

SPARK_URL: str = os.getenv("SPARK_URL", "local[*]")
DB_CONNECTION_STRING: str = os.getenv("DB_CONNECTION_STRING", "")
S3_ENDPOINT: str = os.getenv("S3_ENDPOINT", "")
S3_ACCESS_KEY: str = os.getenv("S3_ACCESS_KEY", "")
S3_SECRET_KEY: str = os.getenv("S3_SECRET_KEY", "")
S3_BUCKETS: List[str] = os.getenv("S3_BUCKETS", "").split(",")
