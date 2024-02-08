# example_usage.py

from easysql import SimpleSQL  # Assuming the class is in a file named easysql.py

def main():
    # Create an instance of SQLiteManager and specify the database name
    db_manager = SimpleSQL("example.db")

    # Create a table named "users"
    db_manager.create_table("users", ["id INTEGER PRIMARY KEY", "name TEXT", "age INTEGER"])

    # Insert data into the "users" table
    db_manager.insert_data("users", ["name", "age"], ["Alice", 28])
    db_manager.insert_data("users", ["name", "age"], ["Bob", 35])
    db_manager.insert_data("users", ["name", "age"], ["Charlie", 22])

    # Query and print all data from the "users" table
    result = db_manager.query_data("users", ["id", "name", "age"])
    print("All Users:")
    print(result)

    # Update data in the "users" table
    db_manager.update_data("users", {"age": 30}, "name='Alice'")

    # Query and print updated data from the "users" table
    result_after_update = db_manager.query_data("users", ["id", "name", "age"])
    print("\nUsers after update:")
    print(result_after_update)

    # Delete data from the "users" table
    db_manager.delete_data("users", "name='Bob'")

    # Query and print data after deletion from the "users" table
    result_after_delete = db_manager.query_data("users", ["id", "name", "age"])
    print("\nUsers after deletion:")
    print(result_after_delete)

    # Create an index on the "age" column of the "users" table
    db_manager.create_index("age_index", "users", ["age"])

    # View tables in the database
    tables = db_manager.view_tables()
    print("\nTables in the database:")
    print(tables)

    # Describe the structure of the "users" table
    table_schema = db_manager.describe_table("users")
    print("\nSchema of the 'users' table:")
    print(table_schema)

    # Backup the database to a file named "backup.db"
    db_manager.backup_database("backup.db")

    # Restore the database from the backup file
    db_manager.restore_database("backup.db")

    # Close the database connection
    db_manager.close_connection()

if __name__ == "__main__":
    main()
