import psycopg2

create_table_query = """
CREATE TABLE IF NOT EXISTS listings (
    listing_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(500),
    image VARCHAR(300) NOT NULL,
    is_fruit BOOLEAN NOT NULL,
    price DOUBLE PRECISION NOT NULL,
    quantity INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
"""

dbname = 'polyhx'
user = 'polyhx'
password = 'polyhx'
host = 'localhost'

conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

# Create a cursor object
cur = conn.cursor()

# Execute the SQL statement
cur.execute(create_table_query)

# Commit the changes to the database
conn.commit()

# Close the cursor and the connection
cur.close()
conn.close()