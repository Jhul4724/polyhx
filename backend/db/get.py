import psycopg2
from typing import List, Tuple

from config.loader import config, ConfigSchema
from db.db import connect, disconnect

def get_user_sales(email: str) -> Tuple[int, List[Tuple[str, str, str, bool, float, int]]]:
    '''
    Fetch all listings from the user.
    
    Args:
        - email (str): The email of the user.
        
    Returns:
        - tuple:
            - int: 0 if listings fetched successfully, -1 if email doesn't exist, -2 otherwise
            - list: (sale1, sale2, ..., saleN) if fetching successful, () otherwise
                - sale (tuple): (name, description, image, is_fruit, price, quantity)
    '''
    try:
        # Connect
        conn, cursor = connect()

        # Check if the user exists
        cursor.execute("SELECT 1 FROM users WHERE email = %s", (email,))
        if not cursor.fetchone():
            return (-1, ())

        # Fetch listings for the user
        cursor.execute("SELECT name, description, image, is_fruit, price, quantity FROM listings WHERE user_id = (SELECT user_id FROM users WHERE email = %s)", (email,))
        sales = cursor.fetchall()

        # Return the result
        return 0, sales
    except Exception:
        return (-2, ())
    finally:
        # Close the cursor and connection
        disconnect(conn, cursor)

def get_listings(email: str) -> Tuple[int, List[Tuple[str, str, str, bool, float, int]]]:
    '''
    Fetch all listings for the user to buy.
    
    Args:
        - email (str): The email of the user.
        
    Returns:
        - tuple:
            - int: 0 if listings fetched successfully, -1 if email doesn't exist, -2 otherwise
            - tuple: (sale1, sale2, ..., saleN) if fetching successful, () otherwise
                - sale (tuple): (name, description, image, is_fruit, price, quantity)
    '''
    try:
        # Connect
        conn, cursor = connect()

        # Check if the user exists
        cursor.execute("SELECT 1 FROM users WHERE email = %s", (email,))
        if not cursor.fetchone():
            return (-1, ())

        # Fetch listings for the user
        cursor.execute("SELECT name, description, image, is_fruit, price, quantity FROM listings WHERE user_id != (SELECT user_id FROM users WHERE email = %s)", (email,))
        sales = cursor.fetchall()

        # Return the result
        return 0, sales
    except Exception:
        return (-2, ())
    finally:
        # Close the cursor and connection
        disconnect(conn, cursor)

def get_vegetables(email: str) -> Tuple[int, List[Tuple[str, str, str, float, int]]]:
    '''
    Fetch all vegetable listings for the user to buy.
    
    Args:
        - email (str): The email of the user.
        
    Returns:
        - tuple:
            - int: 0 if listings fetched successfully, -1 if email doesn't exist, -2 otherwise
            - tuple: (vegetable1, vegetable2, ..., vegetableN) if fetching successful, () otherwise
                - vegetable (tuple): (name, description, image, price, quantity)
    '''
    result_code, sales = get_listings(email)
    
    if result_code == -1 or result_code == -2:
        return result_code, ()

    # Filter out fruits from the listings
    vegetables = [(name, description, image, price, quantity) for name, description, image, is_fruit, price, quantity in sales if not is_fruit]

    return 0, vegetables

def get_fruits(email: str) -> Tuple[int, List[Tuple[str, str, str, float, int]]]:
    '''
    Fetch all fruit listings for the user to buy.
    
    Args:
        - email (str): The email of the user.
        
    Returns:
        - tuple:
            - int: 0 if listings fetched successfully, -1 if email doesn't exist, -2 otherwise
            - tuple: (fruit1, fruit2, ..., fruitN) if fetching successful, () otherwise
                - fruit (tuple): (name, description, image, price, quantity)
    '''
    result_code, sales = get_listings(email)
    
    if result_code == -1 or result_code == -2:
        return result_code, ()

    # Filter out vegetables from the listings
    fruits = [(name, description, image, price, quantity) for name, description, image, is_fruit, price, quantity in sales if is_fruit]

    return 0, fruits
