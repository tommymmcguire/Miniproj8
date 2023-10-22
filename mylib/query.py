"""Query the database"""

from databricks import sql

your_access_token = input("Enter your access token: ")

def query():
    """Query the database for the top 5 rows of the IMDB-Movie-Data table"""
    
    # Establish a connection to the MySQL database
    connection = sql.connect(
                        server_hostname = "adb-8593837241049271.11.azuredatabricks.net",
                        http_path = "/sql/1.0/warehouses/cc52d88b332e98e3",
                        access_token = "{}".format(your_access_token))
    
    cursor = connection.cursor()
    
    # Modify the SQL query to match your MySQL table and database structure
    cursor.execute("SELECT * FROM IMDB_Movie_Data LIMIT 5")
    
    print("Top 5 rows of the IMDB_Movie_Data table:")
    print(cursor.fetchall())
    
    # Close the cursor and the database connection
    cursor.close()
    connection.close()
    return "Success"

def query_best():
    """Query the database for the best movies based on the genre"""
    movie_genre = input("Enter a movie genre: ")
    
    # Establish a connection to the MySQL database
    connection = sql.connect(
                        server_hostname = "adb-8593837241049271.11.azuredatabricks.net",
                        http_path = "/sql/1.0/warehouses/cc52d88b332e98e3",
                        access_token = "{}".format(your_access_token))

    
    cursor = connection.cursor()
    
    # Modify the SQL query to match your MySQL table and database structure
    cursor.execute("""
        SELECT rating, metascore, title, genre, description, actors
        FROM IMDB_Movie_Data
        WHERE genre LIKE %s
        ORDER BY rating DESC
        LIMIT 3
    """, (f'%{movie_genre}%',))
    
    print(f"Best movie based on genre {movie_genre}:")
    print(cursor.fetchall())
    
    # Close the cursor and the database connection
    cursor.close()
    connection.close()
    return "Success"


