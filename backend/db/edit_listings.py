import psycopg2

from config.loader import config, ConfigSchema
from db.db import connect, disconnect

def remove_listing(email: str, listing_id: int) -> int:
    '''
    Removes a listing from the database if it belongs to the specified user.

    Args:
        - email (str): The email of the user.
        - listing_id (int): The id of the listing to be removed.

    Returns:
        - int: 0 for success, -1 if the email does not match the listing owner or the user does not exist, -2 if the listing does not exist, -3 for other errors.
    '''
    try:
        conn, cursor = connect()
        
        # Verify that the listing belongs to the user
        cursor.execute('SELECT user_id FROM listings WHERE listing_id = %s', (listing_id,))
        listing = cursor.fetchone()
        if not listing:
            return -2  # Listing does not exist
        
        cursor.execute('SELECT user_id FROM users WHERE email = %s', (email,))
        user = cursor.fetchone()
        if not user or listing[0] != user[0]:
            return -1  # Emails do not match or user does not exist
        
        # Delete the listing
        cursor.execute('DELETE FROM listings WHERE listing_id = %s', (listing_id,))
        conn.commit()
        return 0  # Success
    except Exception as e:
        print(e)  # For debugging
        return -3  # Other errors
    finally:
        disconnect(conn, cursor)

def sell_from_listing(listing_id: int, qty_sold: int) -> int:
    '''
    Sells a certain quantity from a listing if there is enough quantity available.

    Args:
        - listing_id (int): The ID of the listing.
        - qty_sold (int): The quantity to be sold.

    Returns:
        - int: The updated quantity after the sale, -1 if the listing does not exist, -2 if not enough quantity available, -3 for other errors.
    '''
    try:
        conn, cursor = connect()
        
        # Fetch the current quantity of the listing
        cursor.execute('SELECT quantity FROM listings WHERE listing_id = %s', (listing_id,))
        listing = cursor.fetchone()
        if not listing:
            return -1  # Listing does not exist
        
        current_quantity = listing[0]
        if qty_sold > current_quantity:
            return -2  # Not enough quantity available
        
        # Update the listing with the new quantity
        new_quantity = current_quantity - qty_sold
        cursor.execute('UPDATE listings SET quantity = %s WHERE listing_id = %s', (new_quantity, listing_id))
        conn.commit()
        return new_quantity  # Return the updated quantity
    except Exception as e:
        print(e)  # For debugging
        return -3  # Other errors
    finally:
        disconnect(conn, cursor)
