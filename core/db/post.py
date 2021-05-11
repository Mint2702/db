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
def get_table_student_count(
        cursor,
) -> int:
    """Достает кол во строк в таблице"""

    command = "SELECT count(*) FROM student"
    cursor.execute(command)
    result = cursor.fetchall()

    return result[0]



@sql_command
def post_student(cursor, name, surname, date_if_birth, passport_num, passport_date, passport_given, passport_inn, platoon) -> None:
    """ Добавление студентов в таблицу"""
    count = get_table_student_count()
    print(count)

    """
    INSERT
    INTO
    works
    VALUES(1101, 'Mumu', 'novel');
    """





'''
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

'''