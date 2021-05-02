import psycopg2
from loguru import logger

from .settings import settings


def db_connect(host: str, port: str, user: str, password: str, database: str) -> bool:
    try:
        conn = psycopg2.connect(
            host=host,
            port=int(port),
            user=user,
            password=password,
            database=database,
        )
        cursor = conn.cursor()
        logger.info("Connection succsessful")

        return True

    except Exception as err:
        logger.warning("Connection failed")
        logger.info(err)

        return False
