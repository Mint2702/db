from .utils import sql_command


def get_student_id(cursor, name, surname, passport_num, passport_inn) -> int:
    """ Возвращаетс id студента """
    command = f"SELECT id FROM student WHERE first_name='{name}' AND last_name='{surname}' AND passport_num='{passport_num}' AND inn='{passport_inn}'"
    cursor.execute(command)
    records = cursor.fetchall()
    result = [int(record[0]) for record in records]
    return result[0]


@sql_command
def post_student(
    cursor,
    name,
    surname,
    date_if_birth,
    passport_num,
    passport_date,
    passport_given,
    passport_inn,
    platoon,
    address,
    phone,
) -> None:
    """ Добавление студентов в таблицу """
    cursor.execute(
        "INSERT INTO student (first_name, last_name, date_of_birth, passport_num,  passport_date,  passport_given, inn, platoon_id) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",
        (
            name,
            surname,
            date_if_birth,
            passport_num,
            passport_date,
            passport_given,
            passport_inn,
            platoon,
        ),
    )
    student_id = get_student_id(cursor, name, surname, passport_num, passport_inn)
    cursor.execute(
        "INSERT INTO student_contacts (id_student, address, phone_number) VALUES(%s, %s, %s)",
        (student_id, address, phone),
    )


def get_rod_id(cursor, rod) -> int:
    command = f"SELECT id FROM platoon WHERE direction='{rod}'"
    cursor.execute(command)
    records = cursor.fetchall()
    result = [int(record[0]) for record in records]
    return result[0]


def get_subject_id(cursor, name) -> int:
    command = f"SELECT id FROM subject WHERE name='{name}'"
    cursor.execute(command)
    records = cursor.fetchall()
    result = [int(record[0]) for record in records]
    return result[0]


@sql_command
def post_subject(cursor, name, year, semestr, rod) -> None:
    """ Добавление предметов """
    rod_id = get_rod_id(cursor, rod)
    cursor.execute(
        "INSERT INTO subject (name, year_of_study, semester_of_study) VALUES(%s, %s, %s)",
        (name, year, semestr),
    )

    subject_id = get_subject_id(cursor, name)
    cursor.execute(
        "INSERT INTO subject_of_platoon (id_platoon, id_subject) VALUES(%s, %s)",
        (rod_id, subject_id),
    )


def get_equipment_id(cursor, name) -> int:
    command = f"SELECT id FROM equipment WHERE denomination='{name}'"
    cursor.execute(command)
    records = cursor.fetchall()
    result = [int(record[0]) for record in records]
    return result[0]


@sql_command
def post_equipment(cursor, name, subject) -> None:
    """Добавление оборудования"""
    subject_id = get_subject_id(cursor, subject)
    cursor.execute(f"INSERT INTO equipment (denomination) VALUES('{name}')")
    equipment_id = get_equipment_id(cursor, name)
    cursor.execute(
        "INSERT INTO equipment_for_subject (id_equipment, id_subject) VALUES(%s, %s)",
        (equipment_id, subject_id),
    )


def get_rank_id(cursor, rank_name) -> int:
    command = f"SELECT id FROM rank WHERE title='{rank_name}'"
    cursor.execute(command)
    records = cursor.fetchall()
    result = [int(record[0]) for record in records]
    return result[0]


def get_teacher_id(cursor, name, surname, passport_num, passport_inn) -> int:
    command = f"SELECT id FROM teacher WHERE first_name='{name}' AND last_name='{surname}' AND passport_num='{passport_num}' AND inn='{passport_inn}'"
    cursor.execute(command)
    records = cursor.fetchall()
    result = [int(record[0]) for record in records]
    return result[0]


@sql_command
def post_teacher(
    cursor,
    name,
    surname,
    birth,
    begin,
    passport_num,
    passport_date,
    passport_given,
    passport_inn,
    rank,
    specialisation,
    address,
    phone,
) -> None:
    rank_id = get_rank_id(cursor, rank)
    subject_id = get_subject_id(cursor, specialisation)
    cursor.execute(
        "INSERT INTO teacher (first_name, last_name, date_of_birth, teaching_begin, passport_num, passport_date, passport_given, inn, rank) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (
            name,
            surname,
            birth,
            begin,
            passport_num,
            passport_date,
            passport_given,
            passport_inn,
            rank_id,
        ),
    )
    teacher_id = get_teacher_id(cursor, name, surname, passport_num, passport_inn)

    cursor.execute(
        "INSERT INTO teacher_subject_area (id_subject, id_teacher) VALUES(%s, %s)",
        (subject_id, teacher_id),
    )

    cursor.execute(
        "INSERT INTO teacher_contacts (id_teacher, address, phone_number) VALUES(%s, %s, %s)",
        (teacher_id, address, phone),
    )
