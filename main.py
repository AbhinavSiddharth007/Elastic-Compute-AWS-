from sharding_maneger import get_db_connection

def create_shift(user_id, shift_time):
    connection = get_db_connection(user_id)
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO shifts (user_id, shift_time) VALUES (%s, %s)"
            cursor.execute(sql, (user_id, shift_time))
        connection.commit()
        print(f"Shift created for user {user_id}")
    finally:
        connection.close()

# Example usage
create_shift(user_id=42, shift_time='2025-06-23 09:00:00')
