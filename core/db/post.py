from .utils import sql_command

# INSERT INTO fruits(name)
# VALUES('Banana')
# RETURNING id;


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


@sql_command
def post_subject() -> None:
    """ Добавление предметов """
    print("test")
