from common.settings import DB_CONNECTION_STRING
from sqlalchemy import create_engine, text, Engine


def get_db_engine():
    """
    Create and return a SQLAlchemy engine for the database.
    """
    engine = create_engine(DB_CONNECTION_STRING, echo=True)
    return engine


def execute_query(engine: Engine, query: str):
    """
    Execute a SQL query and return the result.

    :param query: SQL query to execute.
    :param engine: SQLAlchemy engine to use for the connection.
    :return: Result of the query execution.
    """
    with engine.connect() as connection:
        result = connection.execute(text(query))
        return result.fetchall()
