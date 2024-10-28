from gpx_utils import get_coords_from_gpx

def coordinate_test():
    test_cases = [
        ('<trkpt lat="45.3888995" lon="-75.7472631">', (-75.7472631, 45.3888995)),
        ('<trkpt lat="12.3456789" lon="98.7654321">', (98.7654321, 12.3456789)),
        ('<trkpt lat="0.0" lon="0.0">', (0.0, 0.0)),
        ('<trkpt lat="45.3888995">', (None, None)),
        ('<trkpt lon="-75.7472631">', (None, None)),
        ('<trkpt>', (None, None)),
        ('<nottrkpt lat="45.3888995" lon="-75.7472631">', (None, None))
    ]

    for gpx, expected in test_cases:
        result = get_coords_from_gpx(gpx)
        print(f"GPX: {gpx} -> Expected: {expected}, Got: {result}")
        assert result == expected, f"Test failed for {gpx}"

coordinate_string = "075 45 03 W 45 23 05 N\n"
cleaned_string = coordinate_string.strip()
print(cleaned_string) 