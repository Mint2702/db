from .utils import sql_command


@sql_command
def search_equipment(cursor, subject: str) -> list:
    """Достает данные для оборудования в удобном виде"""

    command = f"SELECT eq.denomination, sb.name FROM equipment as eq, subject as sb, equipment_for_subject as eq_sb WHERE eq_sb.id_equipment = eq.id AND eq_sb.id_subject = sb.id AND sb.name like '%{subject}%'"
    cursor.execute(command)
    records = cursor.fetchall()
    result = [[record[0], record[1]] for record in records]

    return result


@sql_command
def search_student(cursor, last_name: str) -> list:
    """Достает студента"""

    command = f"SELECT first_name, last_name, date_of_birth, passport_num, passport_date, passport_given, inn, direction, sc.address, sc.phone_number FROM student, platoon, student_contacts as sc WHERE student.platoon_id = platoon.id AND student.last_name like '%{last_name}%' AND sc.id_student = student.id"
    cursor.execute(command)
    records = cursor.fetchall()
    result = [
        [
            record[0],
            record[1],
            record[2],
            record[3],
            record[4],
            record[5],
            record[6],
            record[7],
            record[8],
            record[9],
        ]
        for record in records
    ]

    return result


@sql_command
def search_subject(cursor, name: str) -> list:
    """Достает данные о предметах"""

    command = f"SELECT sb.name, sb.year_of_study, sb.semester_of_study, pl.direction FROM platoon as pl, subject as sb, subject_of_platoon as sb_pl WHERE sb_pl.id_platoon = pl.id AND sb_pl.id_subject = sb.id AND sb.name like '%{name}%'"
    cursor.execute(command)
    records = cursor.fetchall()
    result = [
        [record[0], int(record[1].days / 365.25) + 2, int(record[2]), record[3]]
        for record in records
    ]

    return result


@sql_command
def search_teacher(cursor, last_name: str) -> list:
    """Достает данные о преподавателях"""

    command = f"SELECT t.first_name, t.last_name, t.date_of_birth, t.teaching_begin, t.passport_num, t.passport_date, t.passport_given, t.inn, r.title, s.name, tc.address, tc.phone_number FROM teacher as t, rank as r, teacher_subject_area as ts, subject as s, teacher_contacts as tc WHERE ts.id_subject = s.id AND ts.id_teacher = t.id AND r.id = t.rank AND t.last_name like '%{last_name}%' AND tc.id_teacher = t.id"
    cursor.execute(command)
    records = cursor.fetchall()
    result = [
        [
            record[0],
            record[1],
            record[2],
            record[3],
            record[4],
            record[5],
            record[6],
            record[7],
            record[8],
            record[9],
            record[10],
            record[11],
        ]
        for record in records
    ]

    return result
