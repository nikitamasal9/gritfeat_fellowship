import mysql.connector
import pandas as pd
from IPython.display import FileLink

class MySQLCRUD:
    def __init__(self, host: str, port: str, user: str, password: str, database: str):
        """
        Initializiing MySQLCRUD object with connection details.

        Args:
            host (str): MySQL server hostname.
            port (str): MySQL server port.
            user (str): Username for connecting to the MypythonSQL server.
            password (str): Password for connecting to the MySQL server.
            database (str): Name of the MySQL database to connect to.
        """
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        """
        Establishing a connection to the MySQL database server.
        """
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Connected to MySQL database successfully.")
        except mysql.connector.Error as e:
            print(f"Error connecting to MySQL database: {e}")

    

    def create_table(self, table_name: str, columns: dict):
        """
        Creating a table in the MySQL database.

        Args:
            table_name (str): Name of the table to create.
            columns (dict): Dictionary containing column names and their data types.
                            Example: {'ID': 'INT', 'NAME': 'VARCHAR(255)', 'ADDRESS': 'VARCHAR(255)', 'AGE': 'INT'}
        """
        try:
            cursor = self.connection.cursor()
            column_definitions = ', '.join([f"{column} {data_type}" for column, data_type in columns.items()])
            query = f"CREATE TABLE {table_name} ({column_definitions})"
            cursor.execute(query)
            self.connection.commit()
            cursor.close()
            print(f"Table '{table_name}' created successfully.")
        except mysql.connector.Error as e:
            print(f"Error creating table: {e}")



    def insert_record(self, table: str, values: tuple):
        """
        Inserting a record into the specified table.

        Args:
            table (str): Name of the table to insert into.
            values (tuple): Values to insert into the table.
        """
        try:
            cursor = self.connection.cursor()
            # Construct the SQL query with values embedded
            query = f"INSERT INTO {table} VALUES {values}"
            cursor.execute(query)
            self.connection.commit()
            cursor.close()
            print("Record inserted successfully.")
        except mysql.connector.Error as e:
            print(f"Error inserting record into table: {e}")


    def read_all(self, table:str):
        """
            Reading records from the specified table.

            Args:
            table (str): Name of the table to delete from.
        """
        try:
            cursor = self.connection.cursor()
            query = f"SELECT * FROM {table}"
            cursor.execute(query)
            b = cursor.fetchall()
            cursor.close()
            print("Records printed successfully.")
            return b
        except mysql.connector.Error as e:
            print(f"Error printing records from table: {e}")

    def read_record_where(self, table:str, where_condition: str):
        """
            Reading records from the specified table as per the condition.

        Args:
            table (str): Name of the table to delete from.
            where_condition (str): WHERE clause to specify which records to delete.
        """
        
        try:
            cursor = self.connection.cursor()
            query = f"SELECT * FROM {table} WHERE {where_condition}"
            cursor.execute(query)
            a = cursor.fetchall()
            cursor.close()
            # self.connection.commit()
            print("Records selected successfully.")
            return a
        except mysql.connector.Error as e:
            print(f"Error selecting records from table: {e}")

    
    def update_record(self, table: str, set_values: dict, where_condition: str):
        """
            Updating records in the specified table.

        Args:
            table (str): Name of the table to update.
            set_values (dict): Dictionary of column names and their new values.
            where_condition (str): WHERE clause to specify which records to update.
        """
        try:
            cursor = self.connection.cursor()
            set_clause = ', '.join([f"{column} = '{value}'" for column, value in set_values.items()])
            query = f"UPDATE {table} SET {set_clause} WHERE {where_condition}"
            cursor.execute(query)
            self.connection.commit()
            cursor.close()
            print("Records updated successfully")
        except mysql.connector.Error as e:
            print(f"Error updating records of table: {e}")


    def delete_record(self, table:str, where_condition: str):
        """
        Deleting records from the specified table.

        Args:
            table (str): Name of the table to delete from.
            where_condition (str): WHERE clause to specify which records to delete.
        """
        
        try:
            cursor = self.connection.cursor()
            query = f"DELETE FROM {table} WHERE {where_condition}"
            cursor.execute(query)
            self.connection.commit()
            cursor.close()
            print("Records deleted successfully.")
        except mysql.connector.Error as e:
            print(f"Error deleting records from table: {e}")


    def export_to_csv(self, table: str, file_name: str):
        """
        Exporting data from the specified table to a CSV file.

        Args:
            table (str): Name of the table to export data from.
            file_name (str): Name of the CSV file to export data to.
        """
        try:
            cursor = self.connection.cursor()
            query = f"SELECT * FROM {table}"
            cursor.execute(query)
            data = cursor.fetchall()
            cursor.close()

            # Convert data to DataFrame
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])

            # Export DataFrame to CSV
            df.to_csv(file_name, index=False)
            print(f"Data exported to {file_name} successfully.")
        except mysql.connector.Error as e:
            print(f"Error exporting data to CSV: {e}")

    def export_to_excel(self, table: str, file_name: str):
        """
        Exporting data from the specified table to an Excel file.

        Args:
            table (str): Name of the table to export data from.
            file_name (str): Name of the Excel file to export data to.
        """
        try:
            cursor = self.connection.cursor()
            query = f"SELECT * FROM {table}"
            cursor.execute(query)
            data = cursor.fetchall()
            cursor.close()

            # Convert data to DataFrame
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])

            # Export DataFrame to Excel
            df.to_excel(file_name, index=False, engine='openpyxl')
            print(f"Data exported to {file_name} successfully.")
            c = FileLink(file_name)
            print("Download excel file ", c)

        except mysql.connector.Error as e:
            print(f"Error exporting data to Excel: {e}")




# Testing:
if __name__ == "__main__":
    # Initializing MySQLCRUD object with connection details
    crud = MySQLCRUD(host='localhost', port='3307', user='root', password='12345', database='gritfeat_assignment')

    # Connecting to MySQL database
    crud.connect()

    # Creating a table
    table_name = 'student_table'
    columns = {'ID': 'INT AUTO_INCREMENT PRIMARY KEY', 'NAME': 'VARCHAR(255)', 'ADDRESS': 'VARCHAR(255)', 'AGE': 'INT', }
    crud.create_table(table_name, columns)

    # Executing a query and print the results
    print(crud.read_all('student_table'))

    # Inserting a record into the table
    crud.insert_record(table='student_table', values=(1, 'Bipin', 'Gaushala', 24))
    crud.insert_record(table='student_table', values=(2, 'Nikita', 'Lainchaur', 23))
    crud.insert_record(table='student_table', values=(3, 'Aarya', 'Baneshwor', 25))
    crud.insert_record(table='student_table', values=(4, 'Eru', 'Balaju', 22))

    #Reading record from the table as per where condition
    print(crud.read_record_where('student_table', 'AGE > 23'))
    

    #Updating a record in the table
    crud.update_record(table='student_table', set_values={'ADDRESS': 'Lainchaur-26'}, where_condition="ID = 3")

    # Deleting records from the table
    crud.delete_record(table='student_table', where_condition="ADDRESS = 'Balaju'")

    # Exporting data to CSV
    crud.export_to_csv(table='student_table', file_name='student_data.csv')

     # Exporting data to CSV
    crud.export_to_excel(table='student_table', file_name='student_data.xlsx')

