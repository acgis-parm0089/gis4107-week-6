from code_parser import get_db_link

def test_get_db_link():
    # Valid input
    result = get_db_link("20-WBO-109642-809")
    print(result)  # Expected: "BO-642"

    # Valid input with expected result for YZ-456
    result = get_db_link("55-XYZ-123456-234")
    print(result)  # Expected: "YZ-456"

    # Test with invalid format (missing parts)
    result = get_db_link("20-WB-109642-809")
    print(result)  # Expected: None

    # Test with non-standard letter/number lengths
    result = get_db_link("10-ABC-1234-98")
    print(result)  # Expected: None

# Run the tests
test_get_db_link()
