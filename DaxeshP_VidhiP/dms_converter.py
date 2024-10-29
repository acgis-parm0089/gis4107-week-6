def dms2dd(dms_record):
    # Remove any trailing newline characters
    dms_record = dms_record.strip()
    
    # Split the record into components
    components = dms_record.split()
    if len(components) != 8:
        return None, None  # Return None if format is incorrect

    # Parse longitude and latitude components
    lon_deg, lon_min, lon_sec, lon_dir = components[0], components[1], components[2], components[3].upper()
    lat_deg, lat_min, lat_sec, lat_dir = components[4], components[5], components[6], components[7].upper()

    # Convert degrees, minutes, and seconds to integers
    try:
        lon_deg, lon_min, lon_sec = int(lon_deg), int(lon_min), int(lon_sec)
        lat_deg, lat_min, lat_sec = int(lat_deg), int(lat_min), int(lat_sec)
    except ValueError:
        return None, None  # Return None if conversion fails

    # Validate ranges
    if not (0 <= lon_deg <= 180 and 0 <= lat_deg <= 90):
        return None, None
    if not (0 <= lon_min < 60 and 0 <= lon_sec < 60 and 0 <= lat_min < 60 and 0 <= lat_sec < 60):
        return None, None

    # Convert DMS to Decimal Degrees
    lon_dd = lon_deg + lon_min / 60 + lon_sec / 3600
    lat_dd = lat_deg + lat_min / 60 + lat_sec / 3600

    # Apply direction for W and S
    if lon_dir == 'W':
        lon_dd = -lon_dd
    if lat_dir == 'S':
        lat_dd = -lat_dd

    return lon_dd, lat_dd
