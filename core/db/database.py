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


@sql_command
def get_table_equipment_for_subject(
    cursor,
) -> list:
    """ Достает все данные из указанной таблицы """

    command = "SELECT * FROM equipment_for_subject"
    cursor.execute(command)
    records = cursor.fetchall()
    result = [[int(record[0]), int(record[1])] for record in records]

    return result


@sql_command
def get_table_platoon(
    cursor,
) -> list:
    """ Достает все данные из указанной таблицы """

    command = "SELECT * FROM platoon"
    cursor.execute(command)
    records = cursor.fetchall()
    result = [[int(record[0]), record[1]] for record in records]

    return result


@sql_command
def get_table_rank(
    cursor,
) -> list:
    """ Достает все данные из указанной таблицы """

    command = "SELECT * FROM rank"
    cursor.execute(command)
    records = cursor.fetchall()
    result = [[int(record[0]), record[1]] for record in records]

    return result

@sql_command
def get_table_student(
    cursor,
) -> list:
    """ Достает все данные из указанной таблицы """

    command = "SELECT * FROM student"
    cursor.execute(command)
    records = cursor.fetchall()
    result = [[int(record[0]), record[1], record[2], record[3], record[4]] for record in records]

    return result
