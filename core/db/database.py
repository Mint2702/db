import psycopg2

from .settings import settings
from .utils import sql_command


@sql_command
def get_table(cursor, table: str) -> dict:
    """ Достает все данные из указанной таблицы """

    command = f"SELECT * FROM {table}"
    cursor.execute(command)
    records = cursor.fetchall()
    print(records)
    return records
