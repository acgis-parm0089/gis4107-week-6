from dms_converter import dms2dd

def test_dms2dd():
    # Valid input
    result = dms2dd("075 45 03 W 45 23 05 N\n")
    print(result)  # Expected: (-75.7508333, 45.3847222)

    # Test with S direction for latitude
    result = dms2dd("075 45 03 E 45 23 05 S\n")
    print(result)  # Expected: (75.7508333, -45.3847222)

    # Test invalid longitude degrees
    result = dms2dd("181 00 00 W 45 23 05 N\n")
    print(result)  # Expected: (None, None)

    # Test invalid latitude degrees
    result = dms2dd("075 45 03 W 91 00 00 N\n")
    print(result)  # Expected: (None, None)

    # Test invalid minutes
    result = dms2dd("075 60 00 W 45 23 05 N\n")
    print(result)  # Expected: (None, None)

    # Test invalid seconds
    result = dms2dd("075 45 61 W 45 23 05 N\n")
    print(result)  # Expected: (None, None)

# Run the tests
test_dms2dd()