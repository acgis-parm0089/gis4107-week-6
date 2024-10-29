from phone_utils import is_valid_phone_number

# Test cases
def test_is_valid_phone_number():
    # Test valid format
    assert is_valid_phone_number("123-456-7890") == True, "Should be True"

    # Test invalid formats
    assert is_valid_phone_number("1234567890") == False, "Should be False"
    assert is_valid_phone_number("123-45-67890") == False, "Should be False"
    assert is_valid_phone_number("123-4567-890") == False, "Should be False"

    # Test non-numeric characters
    assert is_valid_phone_number("123-ABC-7890") == False, "Should be False"
    assert is_valid_phone_number("123-456-78A0") == False, "Should be False"

    print("All tests passed.")

# Run tests
test_is_valid_phone_number()
