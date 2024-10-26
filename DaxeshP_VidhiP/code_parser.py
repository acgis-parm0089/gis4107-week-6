def get_db_link(building_code):
    # Split the building code into parts
    parts = building_code.split('-')
    
    # Extract parts
    lll_part = parts[1]
    number_part = parts[2]
    
    # Get the last two letters of the LLL part
    last_two_letters = lll_part[-2:]
    
    # Get the last three numbers of the second numbered part
    last_three_numbers = number_part[-3:]
    
    # Combine them to form the link
    db_link = f"{last_two_letters}-{last_three_numbers}"
    
    return db_link
