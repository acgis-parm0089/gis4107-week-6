from code_parser import get_db_link

def test_get_db_link():
    test_cases = [
        ("20-RVP-104225-809", "VP-225"),
        ("13-VAR-123456-789", "AR-456"),
        ("99-PRI-857139-123", "RI-139")
    ]

    for building_code, expected in test_cases:
        result = get_db_link(building_code)
        print(f"Building Code: {building_code} -> Expected: {expected}, Got: {result}")
        assert result == expected, f"Test failed for {building_code}"


