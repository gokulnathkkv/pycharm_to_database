import psycopg2

# Establish the database connection and cursor
connection = psycopg2.connect(
    dbname="Gokulnath",
    user="postgres",
    password="gokul",
    host="localhost",
    port="5432"
)
cursor = connection.cursor()

try:
    table_name = "teacher_management"

    # Create the table if it doesn't exist
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            teacher_id SERIAL PRIMARY KEY,
            id_card_no int,
            teacher_name VARCHAR(255),
            teacher_age INT,
            teacher_subject VARCHAR(255),
            teacher_position VARCHAR(255),
            teacher_salary DECIMAL(10, 2),
            teacher_contact BIGINT,
            teacher_address VARCHAR(1000)
        );
    """)
    connection.commit()

    print(f"Table '{table_name}' created")

    while True:
        # Print the menu options and get user choice
        print("Press 1 to insert data into the table")
        print("Press 2 to view data from the table")
        print("Press 3 to delete data from the table")
        print("Press 4 to edit data in the table")
        print("Press 5 to exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            # Get input values from the user
            id_card_no = input("Enter your id card number: ")
            teacher_name = input("Enter teacher's name: ")
            teacher_age = input("Enter teacher's age: ")
            teacher_subject = input("Enter teacher's subject: ")
            teacher_position = input("Enter teacher's position: ")
            teacher_salary = input("Enter teacher's salary: ")
            teacher_contact = input("Enter teacher's contact number: ")
            teacher_address = input("Enter teacher's address: ")

            # Define and execute the insert query
            insert_query = f"""
                INSERT INTO {table_name} (id_card_no, teacher_name, teacher_age, teacher_subject, 
                teacher_position, teacher_salary, teacher_contact, teacher_address)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
            """
            data_values = (id_card_no, teacher_name, teacher_age, teacher_subject, teacher_position,
                           teacher_salary, teacher_contact, teacher_address)

            cursor.execute(insert_query, data_values)
            connection.commit()
            print("Data inserted successfully")

        elif choice == '2':
            print("Press 1 to view all data")
            print("Press 2 to view specific data")
            sub_choice = input("Enter your sub-choice: ")

            if sub_choice == '1':
                cursor.execute(f"SELECT * FROM {table_name};")
                rows = cursor.fetchall()

                if rows:
                    for row in rows:
                        print(row)
                else:
                    print("No data to view")

            elif sub_choice == '2':
                cursor.execute(f"SELECT * FROM {table_name} LIMIT 0")
                headings = [desc[0] for desc in cursor.description]
                while True:
                    if headings:
                        print("Heading columns:", ', '.join(headings))
                        input_heading = input("Enter heading column to match: ")
                        input_value = input(f"Enter value for '{input_heading}' to match: ")

                        if input_heading in headings:
                            view_query = f"SELECT * FROM {table_name} WHERE {input_heading} = %s;"
                            cursor.execute(view_query, (input_value,))
                            rows = cursor.fetchall()

                            if rows:
                                for row in rows:
                                    print(row)
                            else:
                                print("No matching data found")
                        else:
                            print(f"'{input_heading}' is not a valid column")

                else:
                    print("Table does not exist")
        if choice == '3':
            cursor.execute(f"SELECT * FROM {table_name} LIMIT 0")
            headings = [desc[0] for desc in cursor.description]

            if headings:
                print("Heading columns:", ', '.join(headings))
                delete_column = input("Enter column name for deletion condition: ")
                delete_value = input(f"Enter value for '{delete_column}' for deletion: ")

                delete_query = f"DELETE FROM {table_name} WHERE {delete_column} = %s;"
                cursor.execute(delete_query, (delete_value,))
                connection.commit()
                if cursor.rowcount > 0:
                    print("Data deleted successfully")
                else:
                    print("No data matching the deletion condition")

            else:
                print("Table does not exist")


        elif choice == '4':
            table_name = "school_management"  # Initial table name
            headings = []
            try:
                cursor.execute(f"SELECT * FROM {table_name} LIMIT 0")
                headings = [desc[0] for desc in cursor.description]
                ("Column names:", ', '.join(headings))
            except psycopg2.ProgrammingError:
                print("Table does not exist")
            if headings:
                print("Heading columns:", ', '.join(headings))
                edit_column = input("Enter column name for editing condition: ")

                if edit_column in headings:
                    student_id = input("Enter student_id for editing: ")

                    if student_id:
                        cursor.execute(f"SELECT * FROM {table_name} WHERE student_id = %s;", (student_id,))
                        row = cursor.fetchone()

                        if row:
                            print(f"Data for student ID {student_id}:\n{row}")
                            new_value = input(f"Enter new value for '{edit_column}': ")

                            update_query = f"UPDATE {table_name} SET {edit_column} = %s WHERE student_id = %s;"
                            cursor.execute(update_query, (new_value, student_id))
                            connection.commit()
                            print("Data updated successfully")
                        else:
                            print(f"No data found for student ID {student_id}")
                    else:
                        print("Student ID cannot be empty")
                else:
                    print(f"'{edit_column}' is not a valid column")


        elif choice == '5':
            print("Exiting the program")
            break

except Exception as e:
    ("error",e)
finally:
    if connection:
        connection.close()
