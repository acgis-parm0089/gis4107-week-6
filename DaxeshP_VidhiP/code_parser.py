def get_db_link(building_code):
    # Split the building code into parts
    parts = building_code.split('-')
    
    # Check that the code has the correct number of parts
    if len(parts) != 4:
        return None  # Return None if format is incorrect
    
    # Extract the required parts
    letters_part = parts[1]
    numbers_part = parts[2]  # Change this to the second numeric part
    
    # Check if parts meet expected format lengths
    if len(letters_part) < 3 or len(numbers_part) < 3:
        return None  # Return None if any part is too short

    # Get last two letters of the LLL part and last three digits of the second numeric part
    last_two_letters = letters_part[-2:]
    last_three_numbers = numbers_part[-3:]
    
    # Concatenate the two parts to form the database link
    db_link = f"{last_two_letters}-{last_three_numbers}"
    return db_link