from functools import wraps
import psycopg2
from loguru import logger


def db_connect(host: str, port: str, user: str, password: str, database: str) -> bool:
    """Соединение с БД"""

    global cursor
    global conn

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

        save_db_data([host, port, user, password, database])

        return True

    except Exception as err:
        logger.warning("Connection failed")
        logger.info(err)

        return False


def sql_command(func):
    """Для выполнения запроса производит подключение к бд по данным из db_data.txt файла,
    создает курсор, а после выполнения запроса закрывает курсор и подключение к бд"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        db_data = get_db_data()
        db_connect(db_data[0], db_data[1], db_data[2], db_data[3], db_data[4])

        result = func(cursor, *args, **kwargs)

        conn.commit()
        cursor.close()
        conn.close()

        return result

    return wrapper


def save_db_data(data: list) -> None:
    """Сохраняет данные о бд в текстовом файле для дальнейшего использования"""

    f = open("db_data.txt", "w+")
    for info in data:
        f.write(f"{info}\n")
    f.close()


def get_db_data() -> list:
    """Возвращает данные о бд из файла"""

    f = open("db_data.txt", "r")
    rows = f.readlines()
    data = [row[:-1] for row in rows]
    f.close()

    return data
