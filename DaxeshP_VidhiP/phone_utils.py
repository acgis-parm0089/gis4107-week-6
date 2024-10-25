def is_valid_phone_number(phone_number):
    # Check length is exactly 12 characters
    if len(phone_number) != 12:
        return False
    
    # Check 4th and 8th characters are dashes
    if phone_number[3] != '-' or phone_number[7] != '-':
        return False
    
    # Check all other characters are digits
    for i in range(12):
        if i != 3 and i != 7:  # Skip the dash positions
            if not phone_number[i].isdigit():
                return False
    
    return True
