def get_coords_from_gpx(gpx):
    # Check gpx string contains 'trkpt'
    if 'trkpt' not in gpx:
        return None, None
    
    # Extract latitude and longitude values
    try:
        lat_start = gpx.index('lat="') + 5
        lat_end = gpx.index('"', lat_start)
        lon_start = gpx.index('lon="') + 5
        lon_end = gpx.index('"', lon_start)
        
        latitude = float(gpx[lat_start:lat_end])
        longitude = float(gpx[lon_start:lon_end])
        
        return longitude, latitude
    except ValueError:
        return None, None
