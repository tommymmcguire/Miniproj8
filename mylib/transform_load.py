"""
Transforms and Loads data 
"""
import csv
import os
from databricks import sql

your_access_token = input("Enter your access token: ")

def load(dataset="/workspaces/MiniProj6/master/IMDB-Movie-Data.csv"):
    """Transforms and Loads data into a MySQL database"""

    # Establish a connection to the MySQL database
    connection = sql.connect(
                        server_hostname = "adb-8593837241049271.11.azuredatabricks.net",
                        http_path = "/sql/1.0/warehouses/cc52d88b332e98e3",
                        access_token = "{}".format(your_access_token))

    
    cursor = connection.cursor()

    # Prints the full working directory and path
    print(os.getcwd())

    # Drop the table if it exists (optional)
    cursor.execute("DROP TABLE IF EXISTS IMDB_Movie_Data")

    create_table_query = """
        CREATE TABLE IF NOT EXISTS IMDB_Movie_Data (
            rank INT,
            title TEXT,
            genre TEXT,
            description TEXT,
            director TEXT,
            actors TEXT,
            year INT,
            runtime_minutes INT,
            rating FLOAT,
            votes INT,
            revenue_millions FLOAT,
            metascore INT
        )
    """
    cursor.execute(create_table_query)

    # Load data from the CSV file and insert it into the MySQL database
    with open(dataset, 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)  # Skip the header row

        for row in csvreader:
            insert_query = """
                INSERT INTO IMDB_Movie_Data 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, tuple(row))

    connection.commit()
    connection.close()
    return "IMDB_Movie_Data table created and data loaded successfully"
