from .utils import sql_command


@sql_command
def search_student(
    cursor,
) -> list:
    """ Достает данные для оборудования в удобном виде """

    command = "SELECT eq.denomination, sb.name FROM equipment as eq, subject as sb, equipment_for_subject as eq_sb WHERE eq_sb.id_equipment = eq.id AND eq_sb.id_subject = sb.id"
    cursor.execute(command)
    records = cursor.fetchall()
    result = [[record[0], record[1]] for record in records]

    return result
