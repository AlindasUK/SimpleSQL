import sqlite3

class SimpleSQL:
    def __init__(self, database_name):
        self.database_name = database_name
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def create_table(self, table_name, columns):
        create_table_query = f"CREATE TABLE {table_name} ({', '.join(columns)})"
        self.cursor.execute(create_table_query)
        self.connection.commit()

    def insert_data(self, table_name, columns, values):
        insert_query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['?' for _ in values])})"
        self.cursor.execute(insert_query, values)
        self.connection.commit()

    def query_data(self, table_name, columns, condition=None):
        select_query = f"SELECT {', '.join(columns)} FROM {table_name}"
        if condition:
            select_query += f" WHERE {condition}"
        self.cursor.execute(select_query)
        results = self.cursor.fetchall()
        return results

    def update_data(self, table_name, set_values, condition):
        update_query = f"UPDATE {table_name} SET {', '.join([f'{column}=?' for column in set_values])} WHERE {condition}"
        self.cursor.execute(update_query, list(set_values.values()))
        self.connection.commit()

    def delete_data(self, table_name, condition):
        delete_query = f"DELETE FROM {table_name} WHERE {condition}"
        self.cursor.execute(delete_query)
        self.connection.commit()

    def create_index(self, index_name, table_name, columns):
        create_index_query = f"CREATE INDEX {index_name} ON {table_name} ({', '.join(columns)})"
        self.cursor.execute(create_index_query)
        self.connection.commit()

    def view_tables(self):
        self.cursor.execute(".tables")
        tables = self.cursor.fetchall()
        return tables

    def describe_table(self, table_name):
        self.cursor.execute(f".schema {table_name}")
        schema = self.cursor.fetchall()
        return schema

    def backup_database(self, backup_file_name):
        self.cursor.execute(f".backup {backup_file_name}")
        self.connection.commit()

    def restore_database(self, backup_file_name):
        self.cursor.execute(f".restore {backup_file_name}")
        self.connection.commit()

    def close_connection(self):
        self.connection.close()

