from .utils import sql_command


@sql_command
def delete_equipment(cursor, params: dict) -> None:

    get_id = f"SELECT id FROM equipment WHERE denomination like '%{params['name']}%'"
    cursor.execute(get_id)
    id = cursor.fetchall()[0][0]
    command1 = f"DELETE FROM equipment_for_subject WHERE id_equipment = {id}"
    command2 = f"DELETE FROM equipment WHERE id = {id}"
    cursor.execute(command1)
    cursor.execute(command2)


@sql_command
def delete_subject(cursor, params: dict) -> None:

    get_id = f"SELECT id FROM subject WHERE name like '%{params['name']}%'"
    cursor.execute(get_id)
    id = cursor.fetchall()[0][0]
    command1 = f"DELETE FROM subject_of_platoon WHERE id_subject = {id}"

    get_teacher_id = (
        f"SELECT id_teacher FROM teacher_subject_area WHERE id_subject = {id}"
    )
    cursor.execute(get_teacher_id)
    teacher_id = cursor.fetchall()[0][0]
    command2 = f"DELETE FROM teacher_subject_area WHERE id_subject = {id}"
    command3 = f"DELETE FROM teacher_subject_area WHERE id_teacher = {teacher_id}"
    command4 = f"DELETE FROM teacher_contacts WHERE id_teacher = {teacher_id}"
    command5 = f"DELETE FROM teacher WHERE id = {teacher_id}"
    command6 = f"DELETE FROM equipment_for_subject WHERE id_subject = {id}"
    command7 = f"DELETE FROM subject WHERE id = {id}"
    cursor.execute(command1)
    cursor.execute(command2)
    cursor.execute(command3)
    cursor.execute(command4)
    cursor.execute(command5)
    cursor.execute(command6)
    cursor.execute(command7)


@sql_command
def delete_student(cursor, params: dict) -> None:

    get_id = f"SELECT id FROM student WHERE first_name like '%{params['first_name']}%' AND last_name like '%{params['last_name']}%' AND passport_num like '{str(params['passport'])}'"
    cursor.execute(get_id)
    id_raw = cursor.fetchall()[0][0]
    command1 = f"DELETE FROM student_contacts WHERE id_student = {id}"
    command2 = f"DELETE FROM student WHERE id = {id}"

    cursor.execute(command1)
    cursor.execute(command2)


@sql_command
def delete_teacher(cursor, params: dict) -> bool:

    get_id = f"SELECT id FROM teacher WHERE first_name like '%{params['first_name']}%' AND last_name like '%{params['last_name']}%' AND passport_num like '{str(params['passport'])}'"
    cursor.execute(get_id)
    id = cursor.fetchall()[0][0]
    check_platoon = f"SELECT count(*) FROM platoon WHERE manager = {id}"
    cursor.execute(check_platoon)
    flag = int(cursor.fetchall()[0][0])
    if flag == 0:
        command1 = f"DELETE FROM teacher_contacts WHERE id_teacher = {id}"
        command2 = f"DELETE FROM teacher_subject_area WHERE id_teacher = {id}"
        command3 = f"DELETE FROM platoon WHERE manager = {id}"
        command4 = f"DELETE FROM teacher WHERE id = {id}"

        cursor.execute(command1)
        cursor.execute(command2)
        cursor.execute(command3)
        cursor.execute(command4)
        return True
    else:
        return False
