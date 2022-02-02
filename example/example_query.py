
class ExampleQuery:

    select_count_row_in_teacher_table = """
        SELECT count(*) 
        FROM teacher;
    """

    create_teacher_table = """
    CREATE TABLE IF NOT EXISTS teacher (
        teacher_id INT PRIMARY KEY,
        first_name VARCHAR(40) NOT NULL,
        last_name VARCHAR(40) NOT NULL,
        language_1 VARCHAR(3) NOT NULL,
        language_2 VARCHAR(3),
        dob DATE,
        tax_id INT UNIQUE,
        phone_no VARCHAR(20)
    );
    """

    populate_teacher_table = """
    INSERT INTO teacher (
        teacher_id, 
        first_name, 
        last_name, 
        language_1, 
        language_2, 
        dob, 
        tax_id, 
        phone_no
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """

