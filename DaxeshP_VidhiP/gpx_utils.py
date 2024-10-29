def get_coords_from_gpx(gpx):
    # Check if 'trkpt' tag is present in the GPX string
    if 'trkpt' not in gpx:
        return None, None  # Return None if 'trkpt' is missing

    # Locate and extract latitude value
    lat_start = gpx.find('lat="') + len('lat="')
    lat_end = gpx.find('"', lat_start)
    latitude = gpx[lat_start:lat_end]

    # Locate and extract longitude value
    lon_start = gpx.find('lon="') + len('lon="')
    lon_end = gpx.find('"', lon_start)
    longitude = gpx[lon_start:lon_end]

    # Attempt to convert latitude and longitude to floats
    try:
        return float(longitude), float(latitude)
    except ValueError:
        return None, None  # Return None if conversion fails
