from gpx_utils import get_coords_from_gpx

def test_get_coords_from_gpx():
    # Test with a valid GPX string
    gpx_str = '<trkpt lat="45.3888995" lon="-75.7472631">'
    lon, lat = get_coords_from_gpx(gpx_str)
    print(f"Longitude: {lon}, Latitude: {lat}")  # Expected: -75.7472631, 45.3888995
    
    # Test with missing 'trkpt' tag
    gpx_str_missing_tag = '<some_other_tag lat="45.3888995" lon="-75.7472631">'
    lon, lat = get_coords_from_gpx(gpx_str_missing_tag)
    print(f"Longitude: {lon}, Latitude: {lat}")  # Expected: None, None
    
    # Test with missing latitude and longitude
    gpx_str_no_coords = '<trkpt>'
    lon, lat = get_coords_from_gpx(gpx_str_no_coords)
    print(f"Longitude: {lon}, Latitude: {lat}")  # Expected: None, None

    # Test with incorrect coordinates format
    gpx_str_invalid_coords = '<trkpt lat="invalid" lon="invalid">'
    lon, lat = get_coords_from_gpx(gpx_str_invalid_coords)
    print(f"Longitude: {lon}, Latitude: {lat}")  # Expected: None, None

# Run tests
test_get_coords_from_gpx()
