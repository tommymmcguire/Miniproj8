"""
Test goes here

"""

import unittest
import sqlite3


class TestQueryBest(unittest.TestCase):
    def test_query_best(self):
        # Create an SQLite in-memory database for testing
        conn = sqlite3.connect("IMDB_Movie_Data.db")
        cursor = conn.cursor()

        # Define the SQL query that you want to test
        query = """
            SELECT rating, metascore, title, genre, description, actors
            FROM IMDB_Movie_Data
            WHERE genre LIKE '%Action%'
            ORDER BY rating DESC
            LIMIT 3
        """

        # Execute the SQL query
        cursor.execute(query)

        # Check if the query result is as expected
        result = cursor.fetchall()
        self.assertTrue(result, "SQL query did not return any results.")

        # Close the database connection
        conn.close()


if __name__ == "__main__":
    unittest.main()
