from .utils import sql_command


@sql_command
def get_table_equipment(
    cursor,
) -> list:
    """ Достает все данные из указанной таблицы """

    command = "SELECT * FROM equipment"
    cursor.execute(command)
    records = cursor.fetchall()
    result = [[int(record[0]), record[1]] for record in records]

    return result
