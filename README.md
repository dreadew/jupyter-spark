# Jupyter PySpark Notebook with S3 Support

Lightweight Docker image for Jupyter Notebook with PySpark, Python 3.11, and built-in S3/Delta Lake integration.

## Features

- Python 3.11
- Jupyter Notebook
- PySpark (connects to external Spark cluster)
- Poetry for dependency management
- S3/Delta Lake support

## Quick Start

1.1. Build the image:

```bash
docker build -t jupyter-pyspark .
```

1.2. Or pull the image from Docker Hub:

```bash
docker pull dreadew/jupyter-pyspark:latest
```

2. Run interactively or via `docker-compose.yml`:

```bash
docker run -it -p 8888:8888 \
    -e SPARK_URL=spark://spark-master:7077 \
    -e JUPYTER_TOKEN=your_token \
    jupyter-pyspark
```

3. Access Jupyter Notebook at `http://localhost:8888`.

## Environment Variables

- `SPARK_URL` – Spark Master URL
- `JUPYTER_TOKEN` – Notebook access token
- `DB_CONNECTION_STRING` – Database connection string
- `S3_ENDPOINT`, `S3_ACCESS_KEY`, `S3_SECRET_KEY` – S3 credentials
- `S3_DELTA_BUCKET`, `S3_RAW_BUCKET` – S3 buckets for Delta Lake and raw datasets

```

```
