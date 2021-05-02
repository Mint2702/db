import psycopg2
from loguru import logger

from .settings import settings


def db_connect():
    try:
        conn = psycopg2.connect(
            host=settings.host,
            port=settings.port,
            user=settings.user,
            password=settings.password,
            database=settings.db_name,
        )
        cursor = conn.cursor()
        logger.info("Connection succsessful")
    except Exception as err:
        logger.warning("Connection failed")
        logger.info(err)
