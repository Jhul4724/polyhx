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
                - sale (dict):  {name, description, image, price, quantity}
    '''
    try:
        # Connect
        conn, cursor = connect()

        # Check if the user exists
        cursor.execute('SELECT 1 FROM users WHERE email = %s', (email,))
        if not cursor.fetchone():
            return (-1, ())

        # Fetch listings for the user
        cursor.execute('SELECT name, description, image, price, quantity FROM listings WHERE user_id = (SELECT user_id FROM users WHERE email = %s)', (email,))
        sales = cursor.fetchall()

        # Return the result
        sales = [{'name': name, 'description': description, 'image': image, 'price': price, 'quantity': quantity} for name, description, image, price, quantity in sales]
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
            - list: (sale1, sale2, ..., saleN) if fetching successful, () otherwise
                - sale (dict): {name, description, image, is_fruit, price, quantity}
    '''
    try:
        # Connect
        conn, cursor = connect()

        # Check if the user exists
        cursor.execute('SELECT 1 FROM users WHERE email = %s', (email,))
        if not cursor.fetchone():
            return (-1, ())

        # Fetch listings for the user
        cursor.execute('SELECT name, description, image, is_fruit, price, quantity FROM listings WHERE user_id != (SELECT user_id FROM users WHERE email = %s)', (email,))
        sales = cursor.fetchall()

        # Return the result
        sales = [{'name': name, 'description': description, 'image': image, 'is_fruit': is_fruit, 'price': price, 'quantity': quantity} for name, description, image, is_fruit, price, quantity in sales]
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
            - list: (vegetable1, vegetable2, ..., vegetableN) if fetching successful, () otherwise
                - vegetable (dict): {name, description, image, price, quantity}
    '''
    result_code, sales = get_listings(email)
    
    if result_code == -1 or result_code == -2:
        return result_code, ()

    # Filter out fruits from the listings
    vegetables = [sale for sale in sales if not sale['is_fruit']]

    return 0, vegetables

def get_fruits(email: str) -> Tuple[int, List[Tuple[str, str, str, float, int]]]:
    '''
    Fetch all fruit listings for the user to buy.
    
    Args:
        - email (str): The email of the user.
        
    Returns:
        - tuple:
            - int: 0 if listings fetched successfully, -1 if email doesn't exist, -2 otherwise
            - list: (fruit1, fruit2, ..., fruitN) if fetching successful, () otherwise
                - fruit (dict): {name, description, image, price, quantity}
    '''
    result_code, sales = get_listings(email)
    
    if result_code == -1 or result_code == -2:
        return result_code, ()

    # Filter out vegetables from the listings
    fruits = [sale for sale in sales if sale['is_fruit']]

    return 0, fruits
