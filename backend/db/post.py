import psycopg2

from config.loader import config, ConfigSchema
from db.db import connect, disconnect

def create_new_sale(email: str, name: str, description: str, image: str, is_fruit: bool, price: float, quantity: int) -> int:
    '''
    Fetch all listings from the user.
    
    Args:
        - email (str): The email of the user.
        - name (str): The name of the listing item.
        - description (str): The description of the listing item.
        - image (str): The image url of the listing item.
        - is_fruit (bool): Whether the listing item is a fruit.
        - price (float): The price of the listing item.
        - quantity (int): The quantity of the listing item.
        
    Returns:
        - int:
            - int: the listing ID if listings created successfully, -1 if email doesn't exist, -2 otherwise
    '''
    try:
        conn, cursor = connect()

        # Check if the user exists
        cursor.execute('SELECT user_id FROM users WHERE email = %s', (email,))
        user_id_result = cursor.fetchone()
        if not user_id_result:
            return -1  # User does not exist

        user_id = user_id_result[0]

        # Insert the new listing and return the ID
        cursor.execute('INSERT INTO listings (user_id, name, description, image, is_fruit, price, quantity) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING listing_id',
                       (user_id, name, description, image, is_fruit, price, quantity))
        listing_id = cursor.fetchone()[0]  # Fetch the returned ID
        conn.commit()
        return listing_id  # Return the listing ID
    except Exception as e:
        print(e)  # For debugging
        return -2  # Error occurred
    finally:
        disconnect(conn, cursor)
