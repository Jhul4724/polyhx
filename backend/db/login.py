import psycopg2
import re
from typing import Tuple

from config.loader import config, ConfigSchema
from db.db import connect, disconnect

def is_valid_email(email):
    '''
    Basic email validation.
    '''
    return re.match(r'[^@]+@[^@]+\.[^@]+', email) is not None

def is_valid_password(password):
    '''
    Checks if password has enough characters.
    '''
    return len(password) >= config[ConfigSchema.MIN_PASSWORD_LENGTH]

def login(email: str, password: str) -> Tuple[int, Tuple[str, str, str]]:
    '''
    Fetch user info from database.
    
    Args:
        - email (str): The email of the user.
        - password (str): The password of the user.
        
    Returns:
        - tuple:
            - int: 0 if authentication successful, -1 otherwise
            - tuple: (first_name, last_name, email) if authentication successful, ('', '', '') otherwise
    '''
    try:
        # Connect
        conn, cursor = connect()
        
        # Check if the email exists
        cursor.execute("SELECT 1 FROM users WHERE email = %s", (email,))
        if cursor.fetchone():
            # Check if the password matches
            cursor.execute("SELECT 1 FROM users WHERE email = %s AND password = %s", (email, password))
            if cursor.fetchone():
                # Return user information if email and password match
                cursor.execute("SELECT first_name, last_name, email FROM users WHERE email = %s", (email,))
                return (0, cursor.fetchone())
            else:
                # Password doesn't match
                return (-1, ('', '', ''))
        else:
            # Email doesn't exist
            return (-1, ('', '', ''))
    except Exception:
        return (-1, ('', '', ''))
    finally:
        # Close the cursor and connection
        disconnect(conn, cursor)

def signup(email: str, password: str, first_name: str, last_name: str) -> int:
    '''
    Create a user.
    
    Args:
        - email (str): The email of the user.
        - password (str): The password of the user.
        - first_name (str): The first name of the user.
        - last_name (str): The last name of the user.
        
    Returns:
        - int: 0 if signup successful, -1 if email already exists, -2 otherwise
    '''
    try:
        # Connect
        conn, cursor = connect()

        # Check if the email already exists
        cursor.execute("SELECT 1 FROM users WHERE email = %s", (email,))
        if cursor.fetchone():
            return -1
        else:
            # Insert the new user into the users table
            cursor.execute("INSERT INTO users (email, password, first_name, last_name) VALUES (%s, %s, %s, %s)",
                           (email, password, first_name, last_name))
            conn.commit()
            return 0
    except Exception:
        return -2
    finally:
        # Close the cursor and connection
        disconnect(conn, cursor)
