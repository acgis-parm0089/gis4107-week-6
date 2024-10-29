def is_valid_phone_number(phone_number):
    # Check if the length is exactly 12 characters
    if len(phone_number) != 12:
        return False
    
    # Check if the format is NNN-NNN-NNNN
    if phone_number[3] != '-' or phone_number[7] != '-':
        return False
    
    # Check if all characters except the dashes are digits
    for i in range(len(phone_number)):
        if i == 3 or i == 7:  # Skip the dashes
            continue
        if not phone_number[i].isdigit():
            return False
    
    return True
