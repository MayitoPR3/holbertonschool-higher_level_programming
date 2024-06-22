#!/usr/bin/python3

"""
lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


def list_states(username, password, database):
    # Connect to MySQL database
    try:
        db = MySQLdb.connect(host='localhost',
                            port=3306,
                            user=username,
                            passwd=password, 
                            db=database)

        cursor = db.cursor()

        # Execute the query
        cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

        # Fetch all the rows
        states = cursor.fetchall()

        # Print results as specified
        for state in states:
            print(state)

        # Close cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./list_states.py database_name")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
