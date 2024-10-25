import DaxeshP_VidhiP.phone_utils as phone_utils

def test_is_valid_phone_number():
    # Test cases for valid phone numbers
    assert phone_utils.is_valid_phone_number("012-345-6789") == True
    assert phone_utils.is_valid_phone_number("672-673-3673") == True

    # Test cases for invalid phone numbers
    assert phone_utils.is_valid_phone_number("839-45-9789") == False
    assert phone_utils.is_valid_phone_number("89825271819") == False
    # Contains a letter 'O'
    assert phone_utils.is_valid_phone_number("O19-272-7436") == False 
    # Incorrect format
    assert phone_utils.is_valid_phone_number("734-5692-961") == False  
    
    print("All tests passed!")

