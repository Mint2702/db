from .utils import sql_command
import datetime


@sql_command
def get_equipment(
    cursor,
) -> list:
    """ Достает данные для оборудования в удобном виде """

    command = "SELECT eq.denomination, sb.name FROM equipment as eq, subject as sb, equipment_for_subject as eq_sb WHERE eq_sb.id_equipment = eq.id AND eq_sb.id_subject = sb.id"
    cursor.execute(command)
    records = cursor.fetchall()
    result = [[record[0], record[1]] for record in records]
    print(result)

    return result


@sql_command
def get_students(
    cursor,
) -> list:
    """ Достает данные о студентах """

    command = "SELECT full_name, date_of_birth, address, phone_number FROM student"
    cursor.execute(command)
    records = cursor.fetchall()
    result = [[record[0], record[1], record[2], record[3]] for record in records]

    return result


@sql_command
def get_subjects(
    cursor,
) -> list:
    """ Достает данные о предметах """

    command = "SELECT sb.name, sb.year_of_study, sb.semester_of_study, pl.direction FROM platoon as pl, subject as sb, subject_of_platoon as sb_pl WHERE sb_pl.id_platoon = pl.id AND sb_pl.id_subject = sb.id"
    cursor.execute(command)
    records = cursor.fetchall()
    result = [
        [record[0], int(record[1].days / 365.25) + 2, int(record[2]), record[3]]
        for record in records
    ]

    return result


@sql_command
def get_teachers(
    cursor,
) -> list:
    """ Достает данные о преподавателях """

    command = "SELECT t.full_name, t.date_of_birth, t.phone_number, t.teaching_experience, r.title, s.name FROM teacher as t, rank as r, teacher_subject_area as ts, subject as s WHERE ts.id_subject = s.id AND ts.id_teacher = t.id AND r.id = t.rank"
    cursor.execute(command)
    records = cursor.fetchall()
    result = [
        [
            record[0],
            str(record[1]),
            record[2],
            int(record[3].days / 365.25) + 1,
            record[4],
            record[5],
        ]
        for record in records
    ]

    return result
