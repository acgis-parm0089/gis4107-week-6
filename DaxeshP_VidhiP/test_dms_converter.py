from dms_converter import dms2dd

def test_dms2dd():
    assert dms2dd("40 26 46 N") == (None, 40.44611111111111)
    assert dms2dd("79 58 56 W") == (-79.98222222222222, None)
    assert dms2dd("0 0 0 N") == (None, 0.0)
    assert dms2dd("0 0 0 E") == (0.0, None)
    assert dms2dd("91 0 0 N") == (None, None)  # Invalid latitude
    assert dms2dd("181 0 0 E") == (None, None)  # Invalid longitude
    assert dms2dd("40 60 0 N") == (None, None)  # Invalid minutes
    assert dms2dd("40 0 60 N") == (None, None)  # Invalid seconds
    assert dms2dd("40 26 46 X") == (None, None)  # Invalid direction
    assert dms2dd("invalid input") == (None, None)  # Invalid format

    print("All tests passed!")

# Run the tests
test_dms2dd()
