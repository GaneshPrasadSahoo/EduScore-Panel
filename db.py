# db.py

import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ganesh", 
        database="student_db"  
    )

def create_table(table_name, columns):
    db = connect_db()
    cursor = db.cursor()

    col_defs = []
    primary_keys = []

    for col in columns:
        col_name = col['name'].strip().replace(" ", "_")
        data_type = col['type']
        col_defs.append(f"`{col_name}` {data_type}")
        if col['primary']:
            primary_keys.append(f"`{col_name}`")

    if "regd_no" not in [col['name'].strip().replace(" ", "_") for col in columns]:
        col_defs.insert(0, "`regd_no` VARCHAR(50)")
        primary_keys.insert(0, "`regd_no`")

    if "student_name" not in [col['name'].strip().replace(" ", "_") for col in columns]:
        col_defs.insert(1, "`student_name` VARCHAR(100)")

    pk_clause = f", PRIMARY KEY ({', '.join(primary_keys)})" if primary_keys else ""
    safe_table = table_name.strip().replace(" ", "_")

    query = f"CREATE TABLE IF NOT EXISTS `{safe_table}` ({', '.join(col_defs)}{pk_clause})"

    try:
        cursor.execute(query)
        db.commit()
    except mysql.connector.Error as err:
        print("❌ SQL Error:", err)
    finally:
        db.close()

def insert_student(table, regd_no, name, marks):
    db = connect_db()
    cursor = db.cursor()

    columns = ", ".join([f"`{k.strip()}`" for k in marks.keys()])
    placeholders = ", ".join(["%s"] * len(marks))
    safe_table = table.strip().replace(" ", "_")

    query = f"""
    INSERT INTO `{safe_table}` (regd_no, student_name, {columns})
    VALUES (%s, %s, {placeholders})
    """

    try:
        cursor.execute(query, (regd_no, name, *marks.values()))
        db.commit()
    except mysql.connector.Error as err:
        print("❌ Insert Error:", err)
    finally:
        db.close()

def get_student_marks(table, regd_no):
    db = connect_db()
    cursor = db.cursor(dictionary=True)
    safe_table = table.strip().replace(" ", "_")

    try:
        print(f"Looking for regd_no: {regd_no} in table: {safe_table}")
        cursor.execute(f"SELECT * FROM `{safe_table}` WHERE regd_no = %s", (regd_no,))
        result = cursor.fetchone()
        print("Fetched result:", result)
    except mysql.connector.Error as err:
        print("❌ Fetch Error:", err)
        result = None
    finally:
        db.close()

    return result

def fetch_all_students(table):
    db = connect_db()
    cursor = db.cursor()
    safe_table = table.strip().replace(" ", "_")

    try:
        cursor.execute(f"SELECT * FROM `{safe_table}`")
        rows = cursor.fetchall()
    except mysql.connector.Error as err:
        print("❌ Fetch All Error:", err)
        rows = []
    finally:
        db.close()

    return rows
