from .utils import sql_command


def get_student_id(cursor, name, surname, passport_num, passport_inn) -> int:
    """Возвращаетс id студента"""
    command = f"SELECT id FROM student WHERE first_name='{name}' AND last_name='{surname}' AND passport_num='{passport_num}' AND inn='{passport_inn}'"
    cursor.execute(command)
    records = cursor.fetchall()
    result = [int(record[0]) for record in records]
    return result[0]


def get_platoon_id(cursor, title) -> int:
    """Возвращаетс id студента"""
    command = f"SELECT id FROM platoon WHERE direction='{title}'"
    cursor.execute(command)
    records = cursor.fetchall()
    result = [int(record[0]) for record in records]
    return result[0]


@sql_command
def update_student(cursor, values, old) -> None:
    """Обновление студентов"""
    student_id = get_student_id(cursor, old[0], old[1], old[3], old[6])
    platoon_id = get_platoon_id(cursor, values["platoon"])
    command = f"UPDATE student SET first_name='{values['name']}', last_name='{values['last_name']}', date_of_birth='{values['born']}', passport_num='{values['pas_num']}', passport_date='{values['pas_date']}', passport_given='{values['pas_given']}', inn='{values['inn']}', platoon_id='{platoon_id}' WHERE id='{student_id}'"
    cursor.execute(command)
    command1 = f"UPDATE student_contacts SET address='{values['address']}', phone_number='{values['number']}' WHERE id_student='{student_id}'"
    cursor.execute(command1)


def get_subject_id(cursor, name) -> int:
    command = f"SELECT id FROM subject WHERE name='{name}'"
    cursor.execute(command)
    records = cursor.fetchall()
    result = [int(record[0]) for record in records]
    return result[0]


def get_rod_id(cursor, rod) -> int:
    command = f"SELECT id FROM platoon WHERE direction='{rod}'"
    cursor.execute(command)
    records = cursor.fetchall()
    result = [int(record[0]) for record in records]
    return result[0]


@sql_command
def update_subject(cursor, values, old) -> None:
    """Обновление предметов"""
    subject_id = get_subject_id(cursor, old[0])
    rod_id = get_rod_id(cursor, values["platoon"])
    command = f"UPDATE subject SET name='{values['subject']}', year_of_study='{values['year']}', semester_of_study='{values['semestr']}' WHERE id='{subject_id}'"
    cursor.execute(command)
    command1 = f"UPDATE subject_of_platoon SET id_platoon='{rod_id}' WHERE id_subject='{subject_id}'"
    cursor.execute(command1)


def ger_equipment_id(cursor, name) -> int:
    command = f"SELECT id FROM equipment WHERE denomination='{name}'"
    cursor.execute(command)
    records = cursor.fetchall()
    result = [int(record[0]) for record in records]
    return result[0]


@sql_command
def update_equipment(cursor, values, old) -> None:
    equipment_id = ger_equipment_id(cursor, old[0])
    subject_id = get_subject_id(cursor, values["subject"])
    command = f"UPDATE equipment SET denomination='{values['name']}' WHERE id='{equipment_id}'"
    cursor.execute(command)

    command1 = f"UPDATE equipment_for_subject SET id_subject='{subject_id}' WHERE id_equipment='{equipment_id}'"
    cursor.execute(command1)


def get_teacher_id(cursor, num) -> int:
    command = f"SELECT id FROM teacher WHERE passport_num='{num}'"
    cursor.execute(command)
    records = cursor.fetchall()
    result = [int(record[0]) for record in records]
    return result[0]


def get_rank_id(cursor, name) -> int:
    command = f"SELECT id FROM rank WHERE title='{name}'"
    cursor.execute(command)
    records = cursor.fetchall()
    result = [int(record[0]) for record in records]
    return result[0]


@sql_command
def update_teacher(cursor, values, old) -> None:
    teacher_id = get_teacher_id(cursor, old[4])
    rank_id = get_rank_id(cursor, values["rank"])
    command = f"UPDATE teacher SET first_name='{values['name']}', last_name='{values['last_name']}', date_of_birth='{values['born']}', passport_num='{values['pas_num']}', passport_date='{values['pas_date']}', passport_given='{values['pas_given']}', inn='{values['inn']}', rank='{rank_id}' WHERE id='{teacher_id}'"
    cursor.execute(command)

    command1 = f"UPDATE teacher_contacts SET address='{values['address']}', phone_number='{values['number']}' WHERE id_teacher='{teacher_id}'"
    cursor.execute(command1)
